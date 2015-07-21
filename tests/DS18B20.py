import unittest

from SensorMonitor.sensor import DS18B20


class TestDS18B20(unittest.TestCase):
    def test_OK(self):
        obj = DS18B20()
        self.assertEqual(obj.parse_data('YES\nt=20000\n'), 20)

    def test_NOK(self):
        obj = DS18B20()
        self.assertEqual(obj.parse_data('NO\nt=20000\n'), None)

    def test_FromFile(self):
        obj = DS18B20()
        obj.device_file = 'DS18B20_TEST_1'
        self.assertEqual(obj.read_sensor(), 27.625)


if __name__ == '__main__':
    unittest.main()
