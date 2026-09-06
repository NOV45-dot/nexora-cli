import unittest
from nexora.modules.network import dns_lookup
from nexora.modules.scanner import COMMON_PORTS


class TestNEXORA(unittest.TestCase):

    def test_common_ports_exist(self):
        self.assertIn(22, COMMON_PORTS)
        self.assertIn(80, COMMON_PORTS)
        self.assertIn(443, COMMON_PORTS)

    def test_common_ports_are_services(self):
        for port, service in COMMON_PORTS.items():
            self.assertIsInstance(port, int)
            self.assertIsInstance(service, str)
            self.assertTrue(service)


if __name__ == "__main__":
    unittest.main()
