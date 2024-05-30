class langueDefaut:
    BIEN_DIT = " x x"
    BONJOUR = "x "
    AU_REVOIR = " x x"

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls):
        return [cls.BONJOUR, cls.AU_REVOIR]
