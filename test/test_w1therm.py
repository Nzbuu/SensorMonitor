import unittest
import io

from SensorMonitor.w1therm import *


class W1ThermFileTests(unittest.TestCase):
    def test_minimal_OK(self):
        text = u'YES\nt=20000\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), 20000)

    def test_minimal_NOK(self):
        text = u'NO\nt=20000\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), None)

    def test_OK_detailed_file(self):
        text = u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n' \
               u'ba 01 55 00 7f ff 0c 10 0a t=27625\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), 27625)

    def test_NOK_detailed_file(self):
        text = u'ba 01 55 00 7f ff 0c 10 0a : crc=0a NO\n' \
               u'ba 01 55 00 7f ff 0c 10 0a t=27625\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), None)

    def test_extended_file_ignores_extra_lines(self):
        text = u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n' \
               u'ba 01 55 00 7f ff 0c 10 0a t=27625\n' \
               u'ba 01 55 00 7f ff 0c 10 0a t=30000\n' \
               u'ba 01 55 00 7f ff 0c 10 0a t=32000\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), 27625)

    def test_truncated_file(self):
        text = u'ba 01 55 00 7f ff 0c 10 0a : crc=0a NO\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), None)

    def test_truncated_file_is_NOK(self):
        text = u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), None)

    def test_missing_temperature(self):
        text = u'ba 01 55 00 7f ff 0c 10 0a : crc=0a YES\n' \
               u'ba 01 55 00 7f ff 0c 10 0a\n'
        obj = interface.FileInterface(
            file_access=FakeAccessWrapper(text))
        self.assertEqual(obj.read_data(), None)


class FakeAccessWrapper:
    def __init__(self, text):
        self.text = text

    def open(self):
        return io.StringIO(self.text)


if __name__ == '__main__':
    unittest.main()
