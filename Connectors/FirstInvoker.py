class FirstInvoker(object):
    def __init__(self, connector):
        self.connector = connector

    def run_some_command(self, par1, par2):
        command = 'echo par1=%s par2=%s' % (par1, par2)
        res = self.connector.run(command)
        return res
