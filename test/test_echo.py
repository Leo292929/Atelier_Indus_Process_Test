import unittest
import random
import string
from src.verificateur_palindrome import VerificateurPalindrome
from src.langue_anglaise import LangueAnglaise
from src.langue_francaise import LangueFrançaise
from verif_palindrome_builder import VerificateurPalindromeBuilder

class Palindrome(unittest.TestCase):

    def motaleatoire(cls, length):
        lettres = string.ascii_lowercase
        return ''.join(random.choice(lettres) for i in range(length))
    def palindromealeatoire(cls, length):
        lettres = string.ascii_lowercase
        moitie = ''.join(random.choice(lettres) for i in range(length))
        return (moitie+moitie[::-1])
    
    MOT_ORDINAIRE = "palindrome"
    MOT_PALINDROME = "kayak"

    LIST_LANGUE = [LangueAnglaise,LangueFrançaise]

    def test_pas_palindrome(self):
        
      # ETANT DONNE 1 liste de mots
        cas  = [self.MOT_ORDINAIRE,self.motaleatoire(10),self.motaleatoire(100)]
        verificateur = VerificateurPalindromeBuilder().par_defaut()


      # QUAND on verifie si se sont des palindrome
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)

      # ALORS la chaîne est renvoyée en miroir
                attendu = chaine[::-1]
                self.assertEqual(attendu," ".join(resultat.split(" ")[1:-2]))

   
    def test_est_palindrome(self):

      # ETANT DONNE un palindrome
        list_langue = self.LIST_LANGUE
        cas  = [self.MOT_PALINDROME,self.palindromealeatoire(10)]
        

      #QUAND on l'ecrit
        for langue in list_langue:

            verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()

            for chaine in cas:
                with self.subTest(chaine):
                    resultat = verificateur.verif(chaine)

      #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                    self.assertEqual(chaine + langue.feliciter(), " ".join(resultat.split(" ")[1:-2]))
        


    def test_bonjour_aurevoir(self):

      # ETANT DONNE une chaine de caractere
        list_langue = self.LIST_LANGUE
        cas  = [self.MOT_ORDINAIRE,self.MOT_PALINDROME]
        

      #QUAND on la saisie
        for langue in list_langue:

            verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()

            for chaine in cas:
                with self.subTest(chaine):
                    resultat = verificateur.verif(chaine)

      #ALORS « Bonjour » est envoyé avant toute réponse #ET « au revoir » est envoyé a la fin
                bonjour = resultat.split(" ")[0]
                aurevoir = " ".join(resultat.split(" ")[-2:])
                result = [bonjour+" "," "+aurevoir]
                self.assertEqual(langue.saluer(), result)

if __name__ == '__main__':
    unittest.main()