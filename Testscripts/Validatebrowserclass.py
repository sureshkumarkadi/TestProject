#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     30-09-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os
import unittest
import traceback
import datetime

dirpath = os.path.dirname(os.path.realpath(__file__))
folderpath = os.path.abspath(os.path.join(dirpath,os.pardir))

sys.path.insert(0,folderpath+'\Setupenv')
sys.path.insert(0,folderpath+'\Library')

from environment import browsersetup
from Login import Loginclass

login = Loginclass()



class validatebrowserclass(unittest.TestCase):
    def test_validatebrowsermethod(self):
        try:
            browserlaunch=browsersetup()
            browser = browserlaunch.setupbrowser()
            assert browser.title == 'New Tab'
        except Exception:
            todaysdate = datetime.datetime.today().strftime('%Y-%m-%d')
            browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase001-%s.png' %todaysdate)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No:Testcase001 is failed")
        finally:
            login.closebrowsermethod(browser)



