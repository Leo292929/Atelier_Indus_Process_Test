from moment import Moment


class langueDefaut:
    BIEN_DIT = " x x"
    BONJOUR_AM = "x x "
    AU_REVOIR_AM = " x x x\r\n"
    BONJOUR_PM = "x x "
    AU_REVOIR_PM = " x x x\r\n"


    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == 0:
            return [cls.BONJOUR_AM, cls.AU_REVOIR_AM]
        else:
            return [cls.BONJOUR_PM, cls.AU_REVOIR_PM]

