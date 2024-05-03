import unittest
from src.verificateur_palindrome import VerificateurPalindrome
import random
import string


class Palindrome(unittest.TestCase):

    def motaleatoire(cls, length):
        lettres = string.ascii_lowercase
        return ''.join(random.choice(lettres) for i in range(length))


    def test_palindrome(self):
        
    # ETANT DONNE 1 liste de mots

        cas  = ["epsi","test","palindrome",self.motaleatoire(10),self.motaleatoire(100)]

    # QUAND on verifie si se sont des palindrome
        

        for chaine in cas:

            resultat = VerificateurPalindrome.verif(chaine)


    # ALORS la chaîne est renvoyée en miroir

            attendu = chaine[::-1]

            self.assertEqual(attendu, resultat)




if __name__ == '__main__':
    unittest.main()