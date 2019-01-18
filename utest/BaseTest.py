import unittest
from AppInvoker import AppInvoker


class BaseTest(unittest.TestCase):

    def setUp(self):
        print("\n" + self._testMethodName)

    @classmethod
    def setUpClass(cls):
        cls.executor = AppInvoker()
        cls.doc_name = 'some_document'
        print cls.method_return_string('String from Parent setUpClass')

    @staticmethod
    def method_return_string(string_arg):
        return string_arg

    @classmethod
    def method_echo_string(cls, string_arg):
        command = 'echo %s' % string_arg
        return cls.executor.bash(command)

    def sub_method_echo(self, string_arg):
        command = 'echo %s' % string_arg
        return self.executor.bash(command)

