import unittest
import random
import string
from src.verificateur_palindrome import VerificateurPalindrome
from src.langue_anglaise import LangueAnglaise
from src.langue_francaise import LangueFrancaise
from src.moment import Moment
from verif_palindrome_builder import VerificateurPalindromeBuilder
import os

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

    LIST_LANGUE = [LangueAnglaise,LangueFrancaise]





    def test_pas_palindrome(self):
        
      # ETANT DONNE 1 liste de mots
        cas  = [self.MOT_ORDINAIRE,self.motaleatoire(10),self.motaleatoire(100)]
        verificateur = VerificateurPalindromeBuilder().par_defaut()


      # QUAND on verifie si ce sont des palindrome
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)

      # ALORS la chaîne est renvoyée en miroir
                attendu = chaine[::-1]
                self.assertEqual(attendu," ".join(resultat.split(" ")[2:-3]))

   
    def test_est_palindrome(self):

      # ETANT DONNE un palindrome
        list_langue = self.LIST_LANGUE
        cas  = [self.MOT_PALINDROME,self.palindromealeatoire(10)]
        

      #QUAND on l'ecrit
        for langue in list_langue:
            for chaine in cas:
                with self.subTest(chaine):
                    
                    verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()

                    resultat = verificateur.verif(chaine)

      #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                    self.assertEqual(chaine + langue.feliciter(), " ".join(resultat.split(" ")[2:-3]))
        


    def test_bonjour_aurevoir_matin(self):

      # ETANT DONNE une chaine de caractere
      # ET un moment de la journée
        list_langue = self.LIST_LANGUE
        cas  = [self.MOT_ORDINAIRE,self.MOT_PALINDROME]
        moment_de_la_journee = Moment

      #QUAND on la saisie
        for langue in list_langue:

            for chaine in cas:
                with self.subTest(chaine):
                    verificateur = VerificateurPalindromeBuilder().avec_langue(langue).avec_moment(moment_de_la_journee).build()
                    resultat = verificateur.verif(chaine)

      #ALORS « Bonjour am » est envoyé avant toute réponse #ET « au revoir am » est envoyé a la fin
                bonjour = resultat.split(" ")[0]+" "+resultat.split(" ")[1]
                aurevoir = " ".join(resultat.split(" ")[-3:])
                result = [bonjour+" "," "+aurevoir]
                self.assertEqual(langue.saluer(moment_de_la_journee), result)

    def test_saut_de_ligne_a_la_fin(self):

      # ETANT DONNE une chaine de caractere
      # (ET tout les parametre par defaut)
      cas = cas  = [self.MOT_ORDINAIRE,self.MOT_PALINDROME]
      verificateur = VerificateurPalindromeBuilder().par_defaut()

      # QUAND on arrive a la derniere ligne
      for chaine in cas:
          with self.subTest(chaine):
              resultat = verificateur.verif(chaine)
              resultat =resultat[-len(os.linesep):]
      # ALORS on trouve un saut de ligne
              attendu = os.linesep
              self.assertEqual(attendu, resultat)

if __name__ == '__main__':
    unittest.main()