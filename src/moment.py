from datetime import datetime
import enum

class Moment(enum.Enum):
    Matin = 1
    Soir = 0

    @classmethod
    def matin_soir(self):
        if heure < 12:
            return Moment.Matin

        return Moment.Soir


