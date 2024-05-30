
class VerificateurPalindrome:

    def __init__(self, langue,moment):
        self.__langue = langue
        self.__moment = moment
        pass

    def verif(self, chaine):

        felicitations = self.__langue.feliciter()
        salutations = self.__langue.saluer(self.__moment)
        bonjour = salutations[0]
        aurevoir = salutations[1]

        if chaine == chaine[::-1]:
            chaine = (chaine[::-1]+felicitations)
        else:
            chaine = chaine[::-1]

        return bonjour + chaine + aurevoir
            
