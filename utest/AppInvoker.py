import subprocess


class AppInvoker(object):
    def __init__(self, app_path='docker', parallel=False):
        self.parallel = False
        self.docker = app_path
        self.parallel = parallel
        self.cmd = None
        self.exitcode = None
        self.proc = None

    def bash(self, cmd):
        self.cmd = cmd
        # print('command: ' + self.cmd)
        self.proc = subprocess.Popen(
            self.cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        res = self.proc.communicate()
        self.exitcode = self.proc.returncode
        return res[0]
