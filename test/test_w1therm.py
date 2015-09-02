import unittest
from mock import Mock
import io

from SensorMonitor.w1therm import *
from SensorMonitor.w1therm import W1Therm


class W1ThermFileTests(unittest.TestCase):
    def test_minimal_OK(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'YES\nt=20000\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), 20.000)

    def test_minimal_NOK(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'NO\nt=20000\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), None)

    def test_OK_detailed_file(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=27625\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), 27.625)

    def test_NOK_detailed_file(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 aa : crc=0a NO\n'
            u'ba 01 55 00 7f ff 0c 10 aa t=27625\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), None)

    def test_extended_file_ignores_extra_lines(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=27625\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=30000\n'
            u'ba 01 55 00 7f ff 0c 10 0a t=32000\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), 27.625)

    def test_truncated_file(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 aa : crc=0a NO\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), None)

    def test_truncated_file_is_NOK(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), None)

    def test_missing_temperature(self):
        mock_file = Mock(interface.FileAccessWrapper)
        mock_file.open.return_value = io.StringIO(
            u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
            u'ba 01 55 00 7f ff 0c 10 0a\n')

        obj = interface.FileInterface(file_access=mock_file)
        sens = W1Therm(obj)
        self.assertEqual(sens.get_measurement(), None)


if __name__ == '__main__':
    unittest.main()
