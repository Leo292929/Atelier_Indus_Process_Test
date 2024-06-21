import os


class LangueAnglaise:
    BIEN_DIT = os.linesep + "Well said"
    BONJOUR_AM = "Hello am" + os.linesep
    AU_REVOIR_AM = os.linesep + "Good bye am" + os.linesep
    BONJOUR_PM = "Hello pm" + os.linesep
    AU_REVOIR_PM = os.linesep + "Good bye pm" + os.linesep

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == 0:
            return [cls.BONJOUR_AM, cls.AU_REVOIR_AM]
        else:
            return [cls.BONJOUR_PM, cls.AU_REVOIR_PM]


