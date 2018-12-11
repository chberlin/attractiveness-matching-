import os
import datetime

class Log:

    def __init__(self):
        self.logs = {}

    def update(self, proxy):
        f_report = open(os.path.join(proxy + 'log.txt'), 'a')
        self.logs[proxy] = f_report

    def write(self, proxy, success):
        if success:
            self.logs[proxy].write(str(datetime.datetime.now()) + " " + proxy + " Request SUCCESSFUL \n")
        else:
            self.logs[proxy].write(str(datetime.datetime.now()) + " " + proxy + " Request FAILED \n")
        self.logs[proxy].flush()


