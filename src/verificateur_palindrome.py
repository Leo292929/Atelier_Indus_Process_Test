class VerificateurPalindrome:

    def __init__(self, langue):
        self.__langue = langue
        pass


    def verif(self,chaine):

        felicitations = self.__langue.feliciter()
        salutations = self.__langue.saluer()
        bonjour = salutations[0]
        aurevoir = salutations[1]

        if(chaine==chaine[::-1]):
            chaine =  (chaine[::-1]+felicitations)
        else:
            chaine = chaine[::-1]
        return bonjour + chaine + aurevoir
            
    