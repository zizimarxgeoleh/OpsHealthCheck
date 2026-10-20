import unittest
from opsbase_utils.policy import alert
class Smoke(unittest.TestCase):
    def test_healthy_does_not_alert(self):
        self.assertFalse(alert({"critical":False,"maintenance":False},{"healthy":True}))
if __name__ == "__main__": unittest.main()
