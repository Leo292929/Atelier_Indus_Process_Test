class VerificateurPalindrome:
    def __init__(self, langue):
        self.__langue = langue
        self.felicitations = self.__langue.feliciter()
        pass

    def verif(self,chaine):
        if(chaine==chaine[::-1]):
            chaine =  (chaine[::-1]+self.felicitations)
        else:
            chaine = chaine[::-1]
        return "Bonjour " + chaine + " Au revoir"
            
    