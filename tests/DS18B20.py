import unittest
from mock import mock_open, patch

from SensorMonitor.sensor import DS18B20


class TestDS18B20(unittest.TestCase):
    @patch('__builtin__.open', mock_open(read_data='YES\nt=20000\n'))
    def test_minimal_OK(self):
        obj = DS18B20()
        obj.device_file = 'DS18B20_TEST'
        self.assertEqual(obj.read_sensor(), 20)

    @patch('__builtin__.open', mock_open(read_data='NO\nt=20000\n'))
    def test_minimal_NOK(self):
        obj = DS18B20()
        obj.device_file = 'DS18B20_TEST'
        self.assertEqual(obj.read_sensor(), None)

    @patch('__builtin__.open', mock_open(
        read_data='ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\nba 01 55 00 7f ff 0c 10 0a t=27625\n'))
    def test_OK_detailed_file(self):
        obj = DS18B20()
        obj.device_file = 'DS18B20_TEST'
        self.assertEqual(obj.read_sensor(), 27.625)


if __name__ == '__main__':
    unittest.main()
