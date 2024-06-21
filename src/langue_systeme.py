import locale
from domaine.langue_anglaise import LangueAnglaise
from domaine.langue_francaise import LangueFrancaise


class LangueSysteme:
    def __init__(self):
        langue_systeme = locale.getlocale()[0]
        self.__langueUtilisateur = LangueAnglaise() if langue_systeme == "en_GB" else LangueFrancaise()

    def feliciter(self):
        return self.__langueUtilisateur.feliciter()

    def saluer(self, moment):
        return self.__langueUtilisateur.saluer(moment)
