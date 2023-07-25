```python
import os
import sys
import logging
from scapy.all import sniff, ARP

# Intrusion Detection System
class IntrusionDetectionSystem:
    def __init__(self):
        self.logger = logging.getLogger('IntrusionDetectionSystem')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def detect_intrusion(self, pkt):
        if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
            self.logger.info(f"ARP Probe from: {pkt[ARP].psrc} to: {pkt[ARP].pdst}")

    def start_detection(self):
        self.logger.info("Starting Intrusion Detection System...")
        sniff(prn=self.detect_intrusion, filter="arp", store=0)

# Initialize and start the intrusion detection system
intrusion_detection_system = IntrusionDetectionSystem()
intrusion_detection_system.start_detection()
```