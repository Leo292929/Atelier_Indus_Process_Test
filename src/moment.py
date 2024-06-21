from datetime import datetime


class Moment:
    def __init__(self):
        now = datetime.now()
        self.current_hour = now.hour

    def matin_soir(self):
        if self.current_hour < 12:
            moment = 0
        else:
            moment = 1

        return moment


