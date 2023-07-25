```python
import os
from scapy.all import *

class Firewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, ip_address=None, port=None, protocol=None):
        rule = {}
        if ip_address:
            rule['ip_address'] = ip_address
        if port:
            rule['port'] = port
        if protocol:
            rule['protocol'] = protocol
        self.rules.append(rule)

    def block(self, packet):
        for rule in self.rules:
            if 'ip_address' in rule and packet[IP].src == rule['ip_address']:
                return True
            if 'port' in rule and packet[TCP].sport == rule['port']:
                return True
            if 'protocol' in rule and packet[IP].proto == rule['protocol']:
                return True
        return False

    def apply(self):
        def packet_filter(packet):
            if self.block(packet):
                print(f"Blocked packet from {packet[IP].src}")
            else:
                send(packet)
        sniff(filter="ip", prn=packet_filter)

firewall_configuration = Firewall()

def configure_firewall(ip_address=None, port=None, protocol=None):
    firewall_configuration.add_rule(ip_address, port, protocol)
    print(f"Firewall configured with rule - IP: {ip_address}, Port: {port}, Protocol: {protocol}")

def FirewallConfigured():
    print("Firewall configuration completed successfully.")
```
