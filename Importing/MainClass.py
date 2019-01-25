from utils.UtilClass import UtilClass


class MainClass(object):

    def setUp(self):
        print("\n" + self._testMethodName)

    @classmethod
    def setUpClass(cls):
        cls.util = UtilClass()

    def go(self):
        self.util.run()


if __name__ == '__main__':
    var = MainClass
    var.go()
