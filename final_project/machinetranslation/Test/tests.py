import unittest
from machinetranslation.translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_for_null_inputEN(self):
        self.assertNotEqual(english_to_french(''), 'Bonjour')
    def test_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null_inputFR(self):
        self.assertNotEqual(french_to_english(''), 'Hello')
    def test_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
