import unittest
from src.verificateur_palindrome import VerificateurPalindrome
import random
import string


class Palindrome(unittest.TestCase):

    def motaleatoire(cls, length):
        lettres = string.ascii_lowercase
        return ''.join(random.choice(lettres) for i in range(length))
    def palindromealeatoire(cls, length):
        lettres = string.ascii_lowercase
        moitie = ''.join(random.choice(lettres) for i in range(length))
        return (moitie+moitie[::-1])
    
    

    def test_pas_palindrome(self):
        
    # ETANT DONNE 1 liste de mots

        cas  = ["epsi","test","palindrome",self.motaleatoire(10),self.motaleatoire(100)]

    # QUAND on verifie si se sont des palindrome
        

        for chaine in cas:
            with self.subTest(chaine):
                resultat = VerificateurPalindrome.verif(chaine)


    # ALORS la chaîne est renvoyée en miroir

                attendu = chaine[::-1]

                self.assertEqual(attendu, resultat)

    def test_est_palindrome(self):

    # ETANT DONNE un palindrome
        cas  = ["kayak","lol","palindromemordnilap",self.palindromealeatoire(5),self.palindromealeatoire(50)]
    #QUAND on l'ecrit
        for chaine in cas:
            with self.subTest(chaine):
                resultat = VerificateurPalindrome.verif(chaine)
    #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                self.assertEqual(chaine + " Bien dit", resultat)
    

if __name__ == '__main__':
    unittest.main()