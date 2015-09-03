import unittest
from hamcrest import *
from mock import Mock
from datetime import datetime

from SensorMonitor.time import *
from SensorMonitor.time import Time, Factory


class TestTime(unittest.TestCase):
    def test_calls_interface_once(self):
        mock_interface = Mock(interface.SystemInterface)
        mock_interface.read_data.return_value = datetime(2000, 1, 1, 12, 0, 0)

        sens = Time(mock_interface)
        meas = sens.get_measurement()

        mock_interface.read_data.assert_called_once_with()
        assert_that(meas, is_(equal_to(datetime(2000, 1, 1, 12, 0, 0))))


class TestTimeFactory(unittest.TestCase):
    def test_can_create_with_factory(self):
        factory = Factory()
        obj = factory.create(interface='fake')
        assert_that(obj, is_(instance_of(Time)))

    def test_can_set_properties_with_factory(self):
        factory = Factory()
        obj = factory.create(interface='fake', output=datetime(2000, 1, 1, 12, 0, 0))
        assert_that(obj.get_measurement(), is_(equal_to(datetime(2000, 1, 1, 12, 0, 0))))
