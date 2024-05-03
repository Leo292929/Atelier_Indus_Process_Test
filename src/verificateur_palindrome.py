class VerificateurPalindrome:

    def verif(chaine):
        if(chaine==chaine[::-1]):
            return (chaine[::-1]+" Bien dit")
        else:
            return chaine[::-1]
            
    