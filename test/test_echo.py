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
                self.assertEqual(attendu," ".join(resultat.split(" ")[1:-2]))


    def test_est_palindrome(self):

    # ETANT DONNE un palindrome
        cas  = ["kayak","lol","palindromemordnilap",self.palindromealeatoire(7)]
    #QUAND on l'ecrit
        for chaine in cas:
            with self.subTest(chaine):
                resultat = VerificateurPalindrome.verif(chaine)
    #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                self.assertEqual(chaine + " Bien dit",  " ".join(resultat.split(" ")[1:-2]))
    

    def test_bonjour_aurevoir(self):

    # ETANT DONNE une chaine de caractere
        cas  = ["kayak","epsi",self.motaleatoire(10)]
    #QUAND on la saisie
        for chaine in cas:
            with self.subTest(chaine):
                resultat = VerificateurPalindrome.verif(chaine)
    #ALORS « Bonjour » est envoyé avant toute réponse #ET « au revoir » est envoyé a la fin
            bonjour = [resultat.split(" ")[0]]
            aurevoir = resultat.split(" ")[-2:]
            result = bonjour+aurevoir
            self.assertEqual(["Bonjour", "Au", "revoir"], result)



if __name__ == '__main__':
    unittest.main()