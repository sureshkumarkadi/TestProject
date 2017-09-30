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

import unittest
import os
import sys
import datetime
import HTMLTestRunner

dirpath = os.path.dirname(os.path.realpath(__file__))
folderpath = os.path.abspath(os.path.join(dirpath,os.pardir))

sys.path.insert(0,folderpath+'\Testscripts')
sys.path.insert(0,folderpath+'\Testreport')

from Validatebrowserclass import validatebrowserclass
from Validategmailclass import validategmailclass


suite = unittest.TestSuite()

suite.addTest(validatebrowserclass('test_validatebrowsermethod'))
suite.addTest(validategmailclass('test_validategmailmethod'))

todaysdate = datetime.datetime.today().strftime('%Y-%m-%d')
outfile = file(folderpath+'\Testreport\Regressionsuitereport-%s.html' %todaysdate,'w')
Testreport = HTMLTestRunner.HTMLTestRunner(stream=outfile,verbosity=2,title='Testproject Automation report',description='Regression report')
Testreport.run(suite)
outfile.close()
