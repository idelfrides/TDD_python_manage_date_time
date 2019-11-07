from datetime import datetime, timedelta, timezone
from pytz import timezone as pytz_timezone


class ManageDateTime(object):

    def setup_datetime(self):
        current_date_time = datetime.now()
        timezone_diference = timedelta(hours=-3)
        return timezone(timezone_diference), current_date_time
    
    def setup_pytzdatetime(self):
        current_date_time = datetime.now()
        return pytz_timezone('America/Sao_Paulo'), current_date_time
    
    
