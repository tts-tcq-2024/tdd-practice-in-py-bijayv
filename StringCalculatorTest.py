import unittest
from StringCalculator import add1
class TestStringCalculator(unittest.TestCase):
    def test_add_returns_zero_for_emptyString(self):
        self.assertEqual(add1(""), 0)
        self.assertEqual(add1("0"), 0)
                
    def test_add_returns_zero_for_singleString(self):
        self.assertEqual(add1("0"), 0)
                
    def test_expectSumForTwoNumberst(self):
        self.assertEqual(add1("1,2"), 3)
                
    def test_ignoreNumbersGreaterThan1000(self):
        self.assertEqual(add1("1,1001"), 1)
                
    def test_expectSumWithCustomDelimiter(self):
        self.assertEqual(add1("//;\n1;2"), 3)
                
    def test_expectSumWithNewlineDelimiter(self):
        self.assertEqual(add1("1\n2,3"),6);
if __name__ == '__main__':
    unittest.main()
