class VerificateurPalindrome:
    def __init__(self, langue):
        self.langue = langue
        pass

    def verif(self,chaine):
        if(chaine==chaine[::-1]):
            chaine =  (chaine[::-1]+" Bien dit")
        else:
            chaine = chaine[::-1]
        return "Bonjour " + chaine + " Au revoir"
            
    