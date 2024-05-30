from moment import Moment


class LangueFrancaise:
    BIEN_DIT = " Bien dit"
    BONJOUR_AM = "Bonjour am "
    AU_REVOIR_AM = " Au revoir am\r\n"
    BONJOUR_PM = "Bonjour pm "
    AU_REVOIR_PM = " Au revoir pm\r\n"

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == 0:
            return [cls.BONJOUR_AM, cls.AU_REVOIR_AM]
        else:
            return [cls.BONJOUR_PM, cls.AU_REVOIR_PM]
