""" Perform tests defore creating 
    the really script of project.
    Folling TDD thecnique    
"""

import unittest
from ijpydatetime import IJDateTimeRecover


class TestDatetimeRecover(unittest.TestCase):
    
    def __init__(self):
        self.dtr = IJDateTimeRecover()


    def test_numeric_date_recover(self):
        numeric_date = self.dtr.numeric_date_recover()
        self.assertEqual(numeric_date, '01/11/2019')






if __name__=='__main__':
    unittest.main()

