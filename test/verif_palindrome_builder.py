from src.langue_stub import LangueStub
from src.verificateur_palindrome import VerificateurPalindrome


class VerificateurPalindromeBuilder:

    __langue = LangueStub()
    __moment = None

    def build(self) -> VerificateurPalindrome:
        return VerificateurPalindrome(self.__langue, self.__moment)
    
    @classmethod
    def par_defaut(cls):
        return VerificateurPalindromeBuilder().build()
    
    def avec_langue(self, langue):
        self.__langue = langue
        return self

    def avec_moment(self, moment):
        self.__moment = moment
        return self
