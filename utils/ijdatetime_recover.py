""" Recover date, time and datetime .
date and time can be numric e string.
"""
from managers import ManageDateTime


class IJDateTimeRecover(ManageDateTime):
    """ Date, time and Dadetime Recover Object """

    def __init__(self):
        self.dtm_obj = ManageDateTime()

    def numeric_date_recover(self):
        """ Return a numeric current date  in the 
            format 00/00/0000 """
       
        sp_time_zone, current_datetime = self.dtm_obj.setup_datetime()   
        converter2sptimezone = current_datetime.astimezone(sp_time_zone)
        
        return converter2sptimezone.strftime('%d/%m/%Y')
    
    def string_date_recover(self):
        """ Return a string current date in the
            format day, month, year """

        sp_time_zone, current_datetime = self.dtm_obj.setup_pytzdatetime()
        converter2sptimezone = current_datetime.astimezone(sp_time_zone)
        
        return converter2sptimezone.strftime('%A, %B %Y')
    
    def numeric_date_time_recover(self):
        """ Return a numeric current date and hour 
            int the format XX/YY/20ZZ HH:MM """
        
        sp_time_zone, current_datetime = self.dtm_obj.setup_pytzdatetime()
        converter2sptimezone = current_datetime.astimezone(sp_time_zone)
        
        return converter2sptimezone.strftime('%d/%m/%Y %H:%M')
    
