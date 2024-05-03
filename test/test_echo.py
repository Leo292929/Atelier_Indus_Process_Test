import unittest
from src.verificateur_palindrome import VerificateurPalindrome



class Palindrome(unittest.TestCase):

    def test_palindrome(self):
        
    # ETANT DONNE 1 liste de mots

        cas  = ["epsi","test"]

    # QUAND on verifie si se sont des palindrome
        

        for chaine in cas:

            resultat = VerificateurPalindrome.verif(chaine)


    # ALORS la chaîne est renvoyée en miroir

            attendu = chaine[::-1]

            self.assertEqual(attendu, resultat)




if __name__ == '__main__':
    unittest.main()