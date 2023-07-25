```python
import unittest
from TheAI.src.antivirus import scan_for_virus, VirusFound

class TestAntivirus(unittest.TestCase):

    def setUp(self):
        self.virus_database = {
            "Trojan": "A type of malicious software that acts as a backdoor in a computer system.",
            "Worm": "A standalone malware that replicates itself in order to spread to other computers.",
            "Ransomware": "A type of malware that threatens to publish the victim's data or perpetually block access to it unless a ransom is paid."
        }

    def test_scan_for_virus(self):
        # Test case: A file with a known virus
        infected_file = "infected_file.txt"
        with self.assertRaises(VirusFound):
            scan_for_virus(infected_file, self.virus_database)

        # Test case: A clean file
        clean_file = "clean_file.txt"
        try:
            scan_for_virus(clean_file, self.virus_database)
        except VirusFound:
            self.fail("scan_for_virus() raised VirusFound unexpectedly!")

if __name__ == '__main__':
    unittest.main()
```