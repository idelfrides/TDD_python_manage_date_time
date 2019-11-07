
""" Date, time and Dadetime Recover Object """

from managers import ManageDateTime 


class IJDateTimeShow(ManageDateTime):
    """ Date, time and Dadetime Show Object """
    
    def __init__(self):
        self.dtm_obj = ManageDateTime()

    def numeric_date_show(self):
        sp_timezone, current_date_time = self.dtm_obj.setup_datetime()
        converter2spdatetime = current_date_time.astimezone(sp_timezone)
        
        print('\n {}'.format(
            converter2spdatetime.strftime('%d/%m/%Y'))
        )

    def string_date_show(self):
        sp_timezone, current_date_time = self.dtm_obj.setup_pytzdatetime()
        sp_date_time = current_date_time.astimezone(sp_timezone)
            
        print('\n {}'.format(
            sp_date_time.strftime('%A, %B %Y')
        ))

    def numeric_date_time_show(self):
        sp_timezone, current_date_time = self.dtm_obj.setup_pytzdatetime()
        sp_date_time = current_date_time.astimezone(sp_timezone)
            
        print('\n {}'.format(
            sp_date_time.strftime('%d/%m/%Y  %H:%M')
        ))
    

