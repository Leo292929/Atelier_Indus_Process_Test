import unittest
from src.verificateur_palindrome import VerificateurPalindrome



class Palindrome(unittest.TestCase):

    def test_palindrome(self):
        
        # ETANT DONNE un mot normal

        chaîne = "epsi"

         # QUAND 

        resultat = VerificateurPalindrome.verif(chaîne)

         # ALORS

        self.assertEqual("ispe", resultat)


if __name__ == '__main__':
    unittest.main()