""" Perform tests defore creating 
    the really script of project,
    Folling TDD thecnique. 
"""

import unittest
from utils import IJDateTimeRecover
from managers import ManageDateTime


class TestDateTimeRecover(unittest.TestCase):

    def __init__(self):
        self.dtr_obj = IJDateTimeRecover()
        self.dtm_obj = ManageDateTime()
    

    def test_numeric_date_recover(self):
        numeric_date = self.dtr_obj.numeric_date_recover()
        self.assertEqual(numeric_date, '07/11/2019')
    

    def test_string_date_recover(self):
        string_date = self.dtr_obj.string_date_recover()
        self.assertEqual(string_date, 'Thursday, November 2019')
    

    def test_numeric_date_time_recover(self):
        sp_time_zone, current_datetime = self.dtm_obj.setup_pytzdatetime()
        converted2sptimezone = current_datetime.astimezone(sp_time_zone)
        expected_numeric_datetime = converted2sptimezone.strftime(
            '%d/%m/%Y %H:%M')

        numeric_datetime = self.dtr_obj.numeric_date_time_recover()
        
        self.assertEqual(numeric_datetime, expected_numeric_datetime)
    


if __name__=='__main__':
    unittest.main()


