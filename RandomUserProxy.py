import requests
import json
from APIProxy import APIProxy
import image
from Log import *




class RandomUserProxy(APIProxy):
    def __init__(self):
        self.image = ""
        self.name = ""
        self.coordinate = {'lat': 0.0, 'long': 0.0}
        self.female = False
        self.success = False
        self.log = Log()
        self.log.update('RandomUserProxy')

    def get(self):
        try:
            req = requests.get('https://randomuser.me/api/?nat=us')
            req = req.json()

            self.coordinate['lat'] = req['results'][0]['location']['coordinates']['latitude']
            self.coordinate['long'] = req['results'][0]['location']['coordinates']['longitude']

            if req['results'][0]['gender'] == 'male':
                self.female = False

            self.name = req['results'][0]['name']['first'].capitalize() + " " + req['results'][0]['name']['last'].capitalize()


            pictureURL = req['results'][0]['picture']['large'] #medium, thumbnail
            filename = 'userPic.jpg'
            r = requests.get(pictureURL, timeout=0.5)

            if r.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(r.content)

            self.image = 'userPic.jpg'
            self.success = True

        except:
            print("Unable to collect random user information")
            self.image = 'defaultPic.jpg'
            self.name = "Alex Smith"

        self.log.write('RandomUserProxy', self.success)
        return self.image
