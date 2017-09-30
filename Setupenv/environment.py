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
from selenium import webdriver
import time


dirpath = os.path.dirname(os.path.realpath(__file__))
folderpath = os.path.abspath(os.path.join(dirpath,os.pardir))

sys.path.insert(0,folderpath+'\Syslibrary')
sys.path.insert(0,folderpath+'\Setupenv')

from datadriver import readxmldata

Datadriver=readxmldata()

class browsersetup():
    def setupbrowser(self):
        env = Datadriver.readxml(folderpath+'\Setupenv\setup.xml','testproject','browser')
        if env == 'firefox':
            browser = webdriver.Firefox()
            return browser

        if env == 'chrome':
            env = Datadriver.readxml(folderpath+'\Setupenv\setup.xml','testproject','browser')
            browser = websriver.Chrome("C:\Users\suresh.kumar\Downloads\chromedriver_win32\chromedriver.exe")
            return browser


