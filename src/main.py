from langue_systeme import LangueSysteme
from moment import Moment
from verificateur_palindrome import VerificateurPalindrome


if __name__ == '__main__':
    langue = LangueSysteme()
    moment = Moment()

    verificateur = VerificateurPalindrome(langue, moment)

    resultat = verificateur.verif("test")
    print(resultat)

    print("________")

    resultat = verificateur.verif("kayak")
    print(resultat)

