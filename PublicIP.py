from APIProxy import *
import requests
from Log import *


class PublicIP(APIProxy):
    def __init__(self):
        self.log = Log()
        self.log.update('PublicIP')
        self.success = False

    def get(self):
        try:
            ip = requests.get('https://api.ipify.org').text
            self.success = True

        except:
            print("Unable to get public IP")
            ip = "8.8.8.8"

        self.log.write('PublicIP', self.success)

        return ip
