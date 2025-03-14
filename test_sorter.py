import unittest
from sorter import Sorter

class TestSorter(unittest.TestCase):
    def test_rejected_due_to_mass_and_size(self):
        self.assertEqual(Sorter.sort(200, 100, 100, 25), "REJECTED")
        self.assertEqual(Sorter.sort(100, 200, 100, 30), "REJECTED")
        self.assertEqual(Sorter.sort(100, 100, 200, 25), "REJECTED")
        self.assertEqual(Sorter.sort(200, 200, 200, 20), "REJECTED")
    
    def test_special_due_to_mass_or_size(self):
        self.assertEqual(Sorter.sort(150, 100, 100, 10), "SPECIAL")
        self.assertEqual(Sorter.sort(100, 150, 100, 10), "SPECIAL")
        self.assertEqual(Sorter.sort(100, 100, 150, 10), "SPECIAL")
        self.assertEqual(Sorter.sort(100, 100, 100, 19), "SPECIAL")
        self.assertEqual(Sorter.sort(200, 200, 200, 10), "SPECIAL")
    
    def test_standard(self):
        self.assertEqual(Sorter.sort(100, 100, 99, 10), "STANDARD")
        self.assertEqual(Sorter.sort(50, 50, 50, 5), "STANDARD")

if __name__ == "__main__":
    unittest.main()
