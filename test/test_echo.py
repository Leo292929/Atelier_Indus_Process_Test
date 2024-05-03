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


    def test_pas_palindrome(self):
        
      # ETANT DONNE 1 liste de mots
        cas  = [self.MOT_ORDINAIRE,self.motaleatoire(10),self.motaleatoire(100)]
        verificateur = VerificateurPalindromeBuilder.par_defaut()


      # QUAND on verifie si se sont des palindrome
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)

      # ALORS la chaîne est renvoyée en miroir
                attendu = chaine[::-1]
                self.assertEqual(attendu," ".join(resultat.split(" ")[1:-2]))



    def test_est_palindrome_fr(self):

      # ETANT DONNE un palindrome
        langue = LangueFrançaise
        cas  = [self.MOT_PALINDROME,self.palindromealeatoire(10)]
        verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()

      #QUAND on l'ecrit
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)

      #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                self.assertEqual(chaine + " Bien dit", " ".join(resultat.split(" ")[1:-2]))
    
    def test_est_palindrome_ang(self):

      # ETANT DONNE un palindrome
        langue = LangueAnglaise
        cas  = [self.MOT_PALINDROME,self.palindromealeatoire(10)]
        verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()

      #QUAND on l'ecrit
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)

      #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                self.assertEqual(chaine + " Well said", " ".join(resultat.split(" ")[1:-2]))
    


    def test_bonjour_aurevoir(self):

      # ETANT DONNE une chaine de caractere
        cas  = [self.MOT_ORDINAIRE,self.MOT_PALINDROME]
        verificateur = VerificateurPalindromeBuilder.par_defaut()

      #QUAND on la saisie
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)

      #ALORS « Bonjour » est envoyé avant toute réponse #ET « au revoir » est envoyé a la fin
            bonjour = [resultat.split(" ")[0]]
            aurevoir = resultat.split(" ")[-2:]
            result = bonjour+aurevoir
            self.assertEqual(["Bonjour", "Au", "revoir"], result)



if __name__ == '__main__':
    unittest.main()