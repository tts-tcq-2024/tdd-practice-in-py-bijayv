import unittest
from StringCalculator import add1
class TestStringCalculator(unittest.TestCase):
    def expectZeroForEmptyInput(self):
        self.assertEqual(add1(""), 0)
        self.assertEqual(add1("0"), 0)
                
    def expectZeroForSingleZero(self):
        self.assertEqual(add1("0"), 0)
                
    def expectSumForTwoNumberst(self):
        self.assertEqual(add1("1,2"), 3)
                
    def ignoreNumbersGreaterThan1000(self):
        self.assertEqual(add1("1,1001"), 1)
                
    def expectSumWithCustomDelimiter(self):
        self.assertEqual(add1("//;\n1;2"), 3)
                
    def expectSumWithNewlineDelimiter(self):
        self.assertEqual(add1("1\n2,3"),6);
if __name__ == '__main__':
    unittest.main()
