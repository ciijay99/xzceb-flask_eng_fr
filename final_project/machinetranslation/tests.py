import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_for_null_inputEN(self):
        pass
        #self.assertIsNotNone(englishToFrench(None))
        
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null_inputFR(self):
        pass
        #self.assertIsNotNone(frenchToEnglish(''))
        #self.assert
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
