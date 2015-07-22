import unittest
from mock import mock_open, patch

from SensorMonitor.sensor import DS18B20


class TestDS18B20(unittest.TestCase):
    def test_OK(self):
        obj = DS18B20()
        obj.device_file = 'mock'
        m = mock_open(read_data='YES\nt=20000\n')
        with patch('__builtin__.open', m):
            self.assertEqual(obj.read_sensor(), 20)

    def test_NOK(self):
        obj = DS18B20()
        obj.device_file = 'mock'
        m = mock_open(read_data='NO\nt=20000\n')
        with patch('__builtin__.open', m):
            self.assertEqual(obj.read_sensor(), None)

    def test_FromFile(self):
        obj = DS18B20()
        obj.device_file = 'DS18B20_TEST_1'
        self.assertEqual(obj.read_sensor(), 27.625)


if __name__ == '__main__':
    unittest.main()
