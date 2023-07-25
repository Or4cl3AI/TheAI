```python
import unittest
from TheAI.src.intrusion_detection import IntrusionDetectionSystem, IntrusionDetected

class TestIntrusionDetection(unittest.TestCase):

    def setUp(self):
        self.ids = IntrusionDetectionSystem()
        self.sample_traffic = {
            "source_ip": "192.168.1.1",
            "destination_ip": "192.168.1.2",
            "source_port": 12345,
            "destination_port": 80,
            "protocol": "TCP",
            "payload": "Some suspicious payload"
        }

    def test_detect_intrusion(self):
        intrusion_detected = self.ids.detect_intrusion(self.sample_traffic)
        self.assertIsInstance(intrusion_detected, IntrusionDetected)

    def test_intrusion_details(self):
        intrusion_detected = self.ids.detect_intrusion(self.sample_traffic)
        self.assertEqual(intrusion_detected.source_ip, self.sample_traffic["source_ip"])
        self.assertEqual(intrusion_detected.destination_ip, self.sample_traffic["destination_ip"])
        self.assertEqual(intrusion_detected.source_port, self.sample_traffic["source_port"])
        self.assertEqual(intrusion_detected.destination_port, self.sample_traffic["destination_port"])
        self.assertEqual(intrusion_detected.protocol, self.sample_traffic["protocol"])
        self.assertEqual(intrusion_detected.payload, self.sample_traffic["payload"])

if __name__ == '__main__':
    unittest.main()
```