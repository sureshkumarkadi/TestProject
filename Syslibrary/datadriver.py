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


import xml.etree.ElementTree as ET

class readxmldata():
    def readxml(self,filename,rootnode,finalnode):
        test = ET.parse(filename)
        test1 = test.getroot()
        for root1 in test1.findall(rootnode):
            value = root1.find(finalnode).text
            return value

