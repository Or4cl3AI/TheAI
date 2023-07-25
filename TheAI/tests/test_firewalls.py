```python
import unittest
from TheAI.src.firewalls import Firewall

class TestFirewall(unittest.TestCase):

    def setUp(self):
        self.firewall = Firewall()

    def test_configure_firewall(self):
        ip_address = "192.168.1.1"
        port = 8080
        protocol = "TCP"
        self.firewall.configure_firewall(ip_address, port, protocol)
        self.assertEqual(self.firewall.firewall_configuration, {"ip_address": ip_address, "port": port, "protocol": protocol})

    def test_block_ip_address(self):
        ip_address = "192.168.1.2"
        self.firewall.block_ip_address(ip_address)
        self.assertIn(ip_address, self.firewall.blocked_ip_addresses)

    def test_unblock_ip_address(self):
        ip_address = "192.168.1.2"
        self.firewall.block_ip_address(ip_address)
        self.firewall.unblock_ip_address(ip_address)
        self.assertNotIn(ip_address, self.firewall.blocked_ip_addresses)

    def test_block_port(self):
        port = 8081
        self.firewall.block_port(port)
        self.assertIn(port, self.firewall.blocked_ports)

    def test_unblock_port(self):
        port = 8081
        self.firewall.block_port(port)
        self.firewall.unblock_port(port)
        self.assertNotIn(port, self.firewall.blocked_ports)

    def test_block_protocol(self):
        protocol = "UDP"
        self.firewall.block_protocol(protocol)
        self.assertIn(protocol, self.firewall.blocked_protocols)

    def test_unblock_protocol(self):
        protocol = "UDP"
        self.firewall.block_protocol(protocol)
        self.firewall.unblock_protocol(protocol)
        self.assertNotIn(protocol, self.firewall.blocked_protocols)

if __name__ == "__main__":
    unittest.main()
```