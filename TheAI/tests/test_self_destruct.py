```python
import unittest
from TheAI.src.self_destruct import SelfDestruct

class TestSelfDestruct(unittest.TestCase):

    def setUp(self):
        self.self_destruct = SelfDestruct()

    def test_self_destruct_sequence(self):
        self.assertEqual(self.self_destruct.self_destruct_sequence(), "SelfDestructActivated")

    def test_data_purge(self):
        data = {"user": "test", "password": "test123"}
        self.self_destruct.data = data
        self.self_destruct.self_destruct_sequence()
        self.assertEqual(self.self_destruct.data, {})

    def test_self_destruct_status(self):
        self.assertEqual(self.self_destruct.self_destruct_status, False)
        self.self_destruct.self_destruct_sequence()
        self.assertEqual(self.self_destruct.self_destruct_status, True)

if __name__ == '__main__':
    unittest.main()
```