#!/usr/bin/env python
# -*- encoding: utf-8 -*-

""" Main module holds main method """

from utils import IJDateTimeRecover, IJDateTimeShow
from textwrap import dedent
import time


def main():
    """ Main method """

    dtr_obj = IJDateTimeRecover()
    dts_obj = IJDateTimeShow()

    print(dedent("""
    
        I AM THE MAIN METHOD 

    """))

    
    print("\n\n Numeric Date:  {} ".format(
        dtr_obj.numeric_date_recover()
    ))
    print("\n\n String Date:  {} ".format(
         dtr_obj.string_date_recover()
    ))
    print('\n\n Numeric date and time: {}'.format(
        dtr_obj.numeric_date_time_recover())
    )
    
    dts_obj.numeric_date_show()
    dts_obj.string_date_show()
    dts_obj.numeric_date_time_show()

    print('\n\n\n')


if __name__ == '__main__':
    while True:
        minutes = 1
        main()
        print('\n\n SLEEPING...\n\n {} MINUTES'.format(minutes))
        print('\n\n\n')

        try:
            time.sleep(minutes * 60)
        except KeyboardInterrupt as kbi:
            print('\n Programm interrupted by user \n\n {}'.format(kbi.__class__))
            print('\n Execution gonna be quited... \n\n\n')
            time.sleep(10)
            exit(0)
        finally:
            pass
        
        
