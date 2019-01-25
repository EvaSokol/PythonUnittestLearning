import unittest
from ConnectorOne import ConnectorOne
from ConnectorTwo import ConnectorTwo
from FirstInvoker import FirstInvoker


class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con_one = ConnectorOne()
        cls.con_two = ConnectorTwo()
        cls.first_invoker = FirstInvoker(cls.con_one)
        cls.second_invoker = FirstInvoker(cls.con_two)

    def automation_specific_method(self):
        par1 = 'string1'
        par2 = 'string2'
        self.first_invoker.run_some_command(par1, par2)
