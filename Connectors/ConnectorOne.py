class ConnectorOne(object):
    app_path = 'Connector One path'

    @classmethod
    def con_one_method(cls):
        print 'con_one_method'

    def run(self, command):
        print 'Running command using connection one: %s' % command
