import os


class LangueFrancaise:
    BIEN_DIT = os.linesep + "Bien dit"
    BONJOUR_AM = "Bonjour am" + os.linesep
    AU_REVOIR_AM = os.linesep + "Au revoir am" + os.linesep
    BONJOUR_PM = "Bonjour pm" + os.linesep
    AU_REVOIR_PM = os.linesep + "Au revoir pm" + os.linesep

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == 0:
            return [cls.BONJOUR_AM, cls.AU_REVOIR_AM]
        else:
            return [cls.BONJOUR_PM, cls.AU_REVOIR_PM]
