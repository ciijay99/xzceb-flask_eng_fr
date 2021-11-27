import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_for_null_inputEN(self):
        self.assertEqual(english_to_french(None), None)
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null_inputFR(self):
        self.assertEqual(french_to_english(None), None)
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
