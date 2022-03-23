from datetime import datetime
from django.utils.timezone import utc




class time_diference():
    def __init__(self, now , timediff):
        self.now = now
        self.timediff = timediff


def get_time_diff(self):
        if self.otp_generated_time:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.time_posted
            return timediff.total_seconds()
        