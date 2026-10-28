import unittest
from src.notes import moyenne, mention


class TestNotes(unittest.TestCase):
    def test_moyenne(self):
        self.assertEqual(moyenne([10, 20]), 15)

    def test_une_seule_note(self):
        self.assertEqual(moyenne([12]), 12)

    def test_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])

    def test_mention_tres_bien(self):
        self.assertEqual(mention(17), "Très bien")

    def test_mention_passable(self):
        self.assertEqual(mention(10), "Passable")

    def test_mention_ajourne(self):
        self.assertEqual(mention(8), "Ajourné")
    
    def test_moyenne_decimale(self):
        self.assertEqual(moyenne([10, 11]), 10.5)
