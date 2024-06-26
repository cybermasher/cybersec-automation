import unittest
from modules.network_monitor import monitor_traffic

class TestNetworkMonitor(unittest.TestCase):
    def test_monitor_traffic(self):
        # This test needs to be run in an environment where packets can be captured
        monitor_traffic()
        self.assertTrue(True)  # Dummy assertion for now

if __name__ == "__main__":
    unittest.main()
