from moment import Moment


class LangueAnglaise:
    BIEN_DIT = " Well said"
    BONJOUR_AM = "Hello am "
    AU_REVOIR_AM = " Good bye am\r\n"
    BONJOUR_PM = "Hello pm "
    AU_REVOIR_PM = " Good bye pm\r\n"

    @classmethod
    def feliciter(cls):
        return cls.BIEN_DIT

    @classmethod
    def saluer(cls, moment):
        if moment == 0:
            return [cls.BONJOUR_AM, cls.AU_REVOIR_AM]
        else:
            return [cls.BONJOUR_PM, cls.AU_REVOIR_PM]


