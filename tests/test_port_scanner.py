import unittest
from modules.port_scanner import scan_ports

class TestPortScanner(unittest.TestCase):
    def test_scan_ports(self):
        open_ports = scan_ports("127.0.0.1")
        self.assertIsInstance(open_ports, list)

if __name__ == "__main__":
    unittest.main()
