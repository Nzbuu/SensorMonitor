import unittest
from hamcrest import *
from mock import Mock
import io

from SensorMonitor.w1therm import *


class TestW1Therm(unittest.TestCase):
    def test_calls_interface_once_OK(self):
        mock_interface = Mock(interface.FileInterface)
        mock_interface.read_data.return_value = 20000

        sens = W1Therm(mock_interface)
        meas = sens.get_measurement()

        mock_interface.read_data.assert_called_once_with()
        assert_that(meas, is_(equal_to(20.000)))

    def test_calls_interface_once_NOK(self):
        mock_interface = Mock(interface.FileInterface)
        mock_interface.read_data.return_value = None

        sens = W1Therm(mock_interface)
        meas = sens.get_measurement()

        mock_interface.read_data.assert_called_once_with()
        assert_that(meas, is_(none()))


class TestW1ThermFactory(unittest.TestCase):
    def test_can_create_with_factory(self):
        factory = Factory()
        obj = factory.create(interface='fake')
        assert_that(obj, is_(instance_of(W1Therm)))

    def test_can_set_properties_with_factory(self):
        factory = Factory()
        obj = factory.create(interface='fake', output=30000)
        assert_that(obj.get_measurement(), is_(equal_to(30.0)))


class TestW1ThermFile(unittest.TestCase):
    def test_minimal_OK(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'YES\nt=20000\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(equal_to(20.000)))

    def test_minimal_NOK(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'NO\nt=20000\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(none()))

    def test_OK_detailed_file(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=27625\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(equal_to(27.625)))

    def test_NOK_detailed_file(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 aa : crc=0a NO\n'
            u'ba 01 55 00 7f ff 0c 10 aa t=27625\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(none()))

    def test_extended_file_ignores_extra_lines(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=27625\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=30000\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=32000\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(equal_to(27.625)))

    def test_truncated_file(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 aa : crc=0a NO\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(none()))

    def test_truncated_file_is_NOK(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(none()))

    def test_missing_temperature(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
            u'ba 01 55 00 7f ff 0c 10 0a\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        meas = sens.get_measurement()

        assert_that(meas, is_(none()))


if __name__ == '__main__':
    unittest.main()
