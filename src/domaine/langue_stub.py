import os


class LangueStub:
    BIEN_DIT = os.linesep + "x x"
    BONJOUR_AM = "x x " + os.linesep
    AU_REVOIR_AM = os.linesep + "x x x" + os.linesep
    BONJOUR_PM = "x x " + os.linesep
    AU_REVOIR_PM = os.linesep + "x x x" + os.linesep

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == 0:
            return [cls.BONJOUR_AM, cls.AU_REVOIR_AM]
        else:
            return [cls.BONJOUR_PM, cls.AU_REVOIR_PM]

