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

dirpath = os.path.dirname(os.path.realpath(__file__))
folderpath = os.path.abspath(os.path.join(dirpath,os.pardir))

sys.path.insert(0,folderpath+'\Syslibrary')
sys.path.insert(0,folderpath+'\Datarepository')

from datadriver import readxmldata


Datadriver=readxmldata()

class Loginclass():
    def enterURLmethod(self,browser):
        url = Datadriver.readxml(folderpath+'\Datarepository\Data.xml','testproject','URL')
        print url
        browser.get(url)

    def closebrowsermethod(self,browser):
        browser.close()
