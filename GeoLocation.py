import requests
import json
from APIProxy import APIProxy
from PublicIP import *
import socket
from Log import *



class GeoLocation(APIProxy):
    def __init__(self):
        self.IP = PublicIP().get()
        self.coordinate = {'lat': 0.0, 'long': 0.0}
        self.success = False
        self.log = Log()
        self.log.update('GeoLocation')

    def get(self):
        try:
            req = requests.get('https://ipvigilante.com/json/' + self.IP)
            req = req.json()
            self.coordinate['lat'] = float(req['data']['latitude'])
            self.coordinate['long'] = float(req['data']['longitude'])
            self.success = True


        except:
            print("Unable to get Longitude and Latitude of your IP")
            self.coordinate['lat'] = 40.7141667
            self.coordinate['long'] = -74.0063889 #NYC

        self.log.write('GeoLocation', self.success)
        return self.coordinate
