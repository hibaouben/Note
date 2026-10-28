import unittest
from src.notes import moyenne


class TestNotes(unittest.TestCase):
    def test_moyenne(self):
        self.assertEqual(moyenne([10, 20]), 15)

    def test_une_seule_note(self):
        self.assertEqual(moyenne([12]), 12)

    def test_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])