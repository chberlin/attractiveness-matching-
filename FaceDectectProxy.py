from APIProxy import APIProxy
import requests
import json
import base64
from Log import *


class FaceDetectProxy(APIProxy):
    def __init__(self):
        self.__faceToken = ""
        self.maleScore = 0
        self.femaleScore = 0
        self.log = Log()
        self.log.update('FaceDetectProxy')
        self.success = False


    def get(self, img):

        img_str = self.convertToBase64(img)
        try:
            data = {'api_key': "f_hn_mk49Ual99S09KwCyAVX0aVa27eD",
                    'api_secret': "BAZwz8nl9k-RESEBVYMYRJt3IP_o7kYy",
                    'image_base64': img_str,
                    'return_attributes': "beauty"
                    }
            req = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', data)
            req = req.json()
            self.maleScore = req['faces'][0]['attributes']['beauty']['male_score']
            self.femaleScore = req['faces'][0]['attributes']['beauty']['female_score']

            self.success = True

        except:
            print("Unable to analyze beauty at this time. User's beauty is perfect by default")
            self.maleScore = 100
            self.femaleScore = 100

        self.log.write('FaceDetectProxy', self.success)

    def convertToBase64(self, image):

        with open(image, "rb") as imageFile:
            img_str = base64.b64encode(imageFile.read())
        return img_str

