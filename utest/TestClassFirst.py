from BaseTest import BaseTest
import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestClassFirst))
    return suite


class TestClassFirst(BaseTest):
    test_variable_one = '*************'
    test_variable_two = '############'

    @classmethod
    def setUpClass(cls):
        super(TestClassFirst, cls).setUpClass()
        cls.test_variable_one = super(TestClassFirst, cls).method_return_string('String returned from Test setUpClass')
        cls.test_variable_two = super(TestClassFirst, cls).method_echo_string('String echo from Test setUpClass')
        cls.parent_variable_one = 'new_value_for_parent_variable_one'
        cls.doc_name = 'new_value_for_parent_doc_name'
        print 'End of Test setUpClass'

    def test_01_first(self):
        print self.test_variable_one
        print self.parent_variable_one
        print self.doc_name
        str = 'first_string'
        result = self.method_return_string(str)
        print result
        self.assertEqual(str, result, 'No string %s in result' % str)

    def test_02_second(self):
        print self.test_variable_two
        str = 'second_string'
        result = self.method_echo_string(str)
        print result
        self.assertTrue(str in result, 'No string %s in result' % str)


if __name__ == '__main__':
    unittest.main()