from src.langue_defaut import langueDefaut
from src.verificateur_palindrome import VerificateurPalindrome


class VerificateurPalindromeBuilder:

    __langue = langueDefaut()

    def build(self) -> VerificateurPalindrome:
        return VerificateurPalindrome(self.__langue)
    
    @classmethod
    def par_defaut(cls):
        return VerificateurPalindromeBuilder().build()
    
    def avec_langue(self, langue):
        self.__langue = langue
        return self
