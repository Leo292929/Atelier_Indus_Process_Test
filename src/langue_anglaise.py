class LangueAnglaise:
    WELL_SAID = " Well said"
    HELLO = "Hello "
    GOOD_BYE = " Good bye"

    @classmethod
    def feliciter(cls):
        return cls.WELL_SAID
    @classmethod
    def saluer(cls):
        return [cls.HELLO,cls.GOOD_BYE]

