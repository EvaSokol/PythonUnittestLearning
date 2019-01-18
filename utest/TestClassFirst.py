from BaseTest import BaseTest
import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestClassFirst))
    return suite


class TestClassFirst(BaseTest):

    # @classmethod
    # def setUpClass(cls):
    #     # print cls.method_return_string('String returned from Test setUpClass')
    #     # print cls.method_echo_string('String echo from Test setUpClass')
    #     print 'End of Test setUpClass'

    def test_01_first(self):
        str = 'first_string'
        result = self.method_return_string(str)
        print result
        self.assertEqual(str, result, 'No string %s in result' % str)

    def test_02_second(self):
        str = 'second_string'
        result = self.method_echo_string(str)
        print result
        self.assertTrue(str in result, 'No string %s in result' % str)


if __name__ == '__main__':
    unittest.main()