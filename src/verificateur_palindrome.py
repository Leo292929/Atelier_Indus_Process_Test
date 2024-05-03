class VerificateurPalindrome:

    def verif(chaine):
        if chaine[::-1]!=chaine:
            return chaine[::-1]
        else :
            return "kayak Bien dit"
    