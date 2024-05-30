class LangueFrancaise:
    BIEN_DIT = " Bien dit"
    BONJOUR = "Bonjour "
    AU_REVOIR = " Au revoir"
    
    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls):
        return [cls.BONJOUR, cls.AU_REVOIR]
    