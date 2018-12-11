from RandomUserProxy import *
from FaceDectectProxy import *
from GeoLocation import *
from geopy import distance

class Model:
    def __init__(self):
        self.maleBeautyRanking = ""
        self.femaleBeautyRanking = ""
        self.randoCoordinate = {}
        self.randoName = ""

    def getImage(self):
        rando = RandomUserProxy()
        img = rando.get()
        self.randoCoordinate = rando.coordinate
        self.randoName = rando.name
        return img



    def getBeautyScore(self, image):

        detect = FaceDetectProxy()
        detect.get(image)
        self.maleBeautyRanking = str(detect.maleScore)
        self.femaleBeautyRanking = str(detect.femaleScore)

    def getDistance(self):

        tracker = GeoLocation()
        userCoord = tracker.get()
        userLocation = (userCoord['lat'], userCoord['long'])
        randoLocation = (self.randoCoordinate['lat'], self.randoCoordinate['long'])

        return distance.distance(userLocation, randoLocation).miles






