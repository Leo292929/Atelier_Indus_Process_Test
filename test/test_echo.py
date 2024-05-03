import unittest
from src.verificateur_palindrome import VerificateurPalindrome



class Palindrome(unittest.TestCase):

    def test_palindrome1(self):
        
        # ETANT DONNE un mot normal

        chaîne = "epsi"

         # QUAND on test si c'est un palindrome

        resultat = VerificateurPalindrome.verif(chaîne)

         # ALORS on a le mot en miroir

        self.assertEqual("ispe", resultat)

    def test_palindrome2(self):
        
        # ETANT DONNE un 2eme mot normal

        chaîne = "test"

         # QUAND on test si c'est un palindrome

        resultat = VerificateurPalindrome.verif(chaîne)

         # ALORS on à le mot en miroir

        self.assertEqual("tset", resultat)



if __name__ == '__main__':
    unittest.main()