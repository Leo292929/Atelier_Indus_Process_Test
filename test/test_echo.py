import unittest
import random
import string
from domaine.langue_anglaise import LangueAnglaise
from domaine.langue_francaise import LangueFrancaise
from moment import Moment
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


    def assertLine(self,attendu,resultat,ligne):
        ligneResult = resultat.split(os.linesep)
        return self.assertEqual(attendu,ligneResult[ligne])



    def test_pas_palindrome(self):
        
      # ETANT DONNE 1 liste de mots
        cas  = [self.MOT_ORDINAIRE,self.motaleatoire(10),self.motaleatoire(100)]
        verificateur = VerificateurPalindromeBuilder().par_defaut()

      # QUAND on verifie si ce sont des palindrome
        for chaine in cas:
            with self.subTest(chaine):
                resultat = verificateur.verif(chaine)
                attendu = chaine[::-1]

      # ALORS la chaîne est renvoyée en miroir
                self.assertLine(attendu,resultat,1)

   
    def test_est_palindrome(self):

      # ETANT DONNE un palindrome
        list_langue = self.LIST_LANGUE
        cas  = [self.MOT_PALINDROME,self.palindromealeatoire(10)]

      #QUAND on l'ecrit
        for langue in list_langue:
            for chaine in cas:
                with self.subTest(chaine = chaine, langue = langue):
                    
                    verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()
                    resultat= verificateur.verif(chaine)
                    attendu1 = chaine
                    attendu2 = langue.feliciter().split(os.linesep)[1]

      #ALORS celui-ci est renvoyé #ET « Bien dit » est envoyé ensuite
                    self.assertLine(attendu1, resultat, 1)
                    self.assertLine(attendu2, resultat, 2)


    def test_bonjour_aurevoir_matin(self):

      # ETANT DONNE une chaine de caractere
      # ET un moment de la journée
        list_langue = self.LIST_LANGUE
        cas  = [self.MOT_ORDINAIRE,self.MOT_PALINDROME]
        moment_de_la_journee = Moment

      #QUAND on la saisie
        for langue in list_langue:

            for chaine in cas:
                with self.subTest(chaine = chaine, langue = langue):
                    verificateur = VerificateurPalindromeBuilder().avec_langue(langue).avec_moment(moment_de_la_journee).build()
                    resultat = verificateur.verif(chaine)

      #ALORS « Bonjour am » est envoyé avant toute réponse #ET « au revoir am » est envoyé a la fin
                    attendu1 = langue.saluer(Moment)[0].rstrip(os.linesep)
                    attendu2 = langue.saluer(Moment)[1].lstrip(os.linesep).rstrip(os.linesep)
                    self.assertLine(attendu1, resultat, 0)
                    self.assertLine(attendu2, resultat, -2)


    def test_saut_ligne_fin(self):

      # ETANT DONNE une chaine de caractere
      # (ET tout les parametre par defaut)
      cas = cas  = [self.MOT_ORDINAIRE,self.MOT_PALINDROME]
      list_langue = self.LIST_LANGUE

      # QUAND on arrive a la derniere ligne
      for langue in list_langue:
          verificateur = VerificateurPalindromeBuilder().avec_langue(langue).build()
          for chaine in cas:
              with self.subTest(chaine = chaine, langue = langue):
                  resultat = verificateur.verif(chaine)
                  resultat =resultat[-len(os.linesep):]
          # ALORS on trouve un saut de ligne
                  attendu = os.linesep
                  self.assertEqual(attendu, resultat)


if __name__ == '__main__':
    unittest.main()