from BaseTestClass import BaseTestClass
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SomeTestClass))
    return suite


class SomeTestClass(BaseTestClass):

    def test_first(self):
        print 'Test First'
        self.automation_specific_method()
