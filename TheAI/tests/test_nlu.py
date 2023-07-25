```python
import unittest
from TheAI.src.nlu import understand_language

class TestNLU(unittest.TestCase):

    def setUp(self):
        self.nlu_model = understand_language.NLUModel()

    def test_understand_intent(self):
        test_sentence = "What is the status of the firewall?"
        expected_intent = "firewall_status"
        result = self.nlu_model.understand_intent(test_sentence)
        self.assertEqual(result, expected_intent)

    def test_extract_entities(self):
        test_sentence = "Block IP address 192.168.1.1"
        expected_entities = {"IP": "192.168.1.1"}
        result = self.nlu_model.extract_entities(test_sentence)
        self.assertEqual(result, expected_entities)

    def test_understand_language(self):
        test_sentence = "Scan for viruses in the system"
        expected_result = {"intent": "virus_scan", "entities": {"target": "system"}}
        result = self.nlu_model.understand_language(test_sentence)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
```