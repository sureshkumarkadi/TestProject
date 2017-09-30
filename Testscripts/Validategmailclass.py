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

import os
import sys
import unittest
import datetime
import traceback
import time

dirpath = os.path.dirname(os.path.realpath(__file__))
folderpath = os.path.abspath(os.path.join(dirpath,os.pardir))

sys.path.insert(0,folderpath+'\Library')
sys.path.insert(0,folderpath+'\Setupenv')
sys.path.insert(0,folderpath+'\Screenshots')
sys.path.insert(0,folderpath+'\Objectrepository')

from Login import Loginclass
from environment import browsersetup
from datadriver import readxmldata

readdata = readxmldata()
browserlaunch=browsersetup()
login=Loginclass()
class validategmailclass(unittest.TestCase):
    def test_validategmailmethod(self):
        try:
            browser = browserlaunch.setupbrowser()
            time.sleep(1)
            login.enterURLmethod(browser)
            time.sleep(5)
            logotitlevalidate_object = readdata.readxml(folderpath+'\Objectrepository\Objects.xml','testproject','Logo')
            #logotitlevalidate = browser.find_element_by_id(logotitlevalidate_object)
            logotitlevalidate = browser.find_element_by_id(logotitlevalidate_object)
            time.sleep(2)
            print logotitlevalidate
            time.sleep(2)
            print logotitlevalidate.text
            time.sleep(1)
            #assert browser.title == 'Gmail'
            self.assertEqual(logotitlevalidate.text,'Sign in')
        except Exception:
            todaysdate = datetime.datetime.today().strftime('%Y-%m-%d')
            browser.get_screenshot_as_file(folderpath+'\Screenshots\Testcase002-%s.png' %todaysdate)
            traceback.print_exc(file=sys.stdout)
            self.fail("Test Case No:Testcase002 is failed")
        finally:
            login.closebrowsermethod(browser)

if __name__ == '__main__':
    unittest.main()



