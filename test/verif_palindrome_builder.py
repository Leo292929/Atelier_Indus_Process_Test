from src.langue_defaut import langueDefaut
from src.verificateur_palindrome import VerificateurPalindrome

class VerificateurPalindromeBuilder:
    def build(self) -> VerificateurPalindrome:
        return VerificateurPalindrome(langueDefaut())
    
    @classmethod
    def par_defaut(cls):
        return VerificateurPalindromeBuilder().build()