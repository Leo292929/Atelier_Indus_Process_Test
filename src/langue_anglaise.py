class LangueAnglaise:
    BIEN_DIT = " Well said"
    BONJOUR = "Hello "
    AU_REVOIR = " Good bye"

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls):
        return [cls.BONJOUR, cls.AU_REVOIR]

