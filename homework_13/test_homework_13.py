import unittest
from config_logging import setup_logging
from config_logging import log_event

setup_logging()

class MyTestLogEvent(unittest.TestCase):
    def test_log_event_success(self):
        print("test_log_event_success")

        with self.assertLogs(logger='log_event', level="INFO") as log:
            log_event('user', 'success')
            print(log.output)

    def test_log_event_expired(self):
        print("test_log_event_expired")

        with self.assertLogs(logger='log_event', level="WARNING") as log_log:
            log_event('user', 'expired')
            print(log_log.output)

    def test_log_event_failed(self):
        print("test_log_event_failed")

        with self.assertLogs(logger='log_event', level="ERROR") as log_log_log:
            log_event('user', 'failed')
            print(log_log_log.output)

if __name__ == "__main__":
    unittest.main(verbosity=2)