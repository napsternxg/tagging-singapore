import cgi
import urllib
import os

from modules import libraries, mapHelper
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    mapType="coord"
    coords=mapHelper.mapCoord()
    mName=mapHelper.mapName()
    locationList=[]
    
    def get(self):
        self.locationList=libraries.directoryDb.all().fetch(10)
        #print self.locationList
        self.setLocation()            
        self.template()

    def post(self):
        mapType=self.request.get('posted')
        if mapType=='coord': 
            mapType=0           
            self.coords.latitude=float(self.request.get('latitude'))
            self.coords.longitude=float(self.request.get('longitude'))
            self.coords.tag=self.request.get('tag')
            self.setLocation()

        elif mapType=='name':
            mapType=1
            self.mName.location=self.request.get('location')
            self.setCoords()
        self.locationList=libraries.directoryDb.all().fetch(10)
        self.template()

    def setCoords(self):
        self.coords=self.mName.returnCoordsFormatted()
        """
        latLong=latLong.split(",")
        self.coords.latitude=float(latLong[2])
        self.coords.longitude=float(latLong[3])"""

    def setLocation(self):
        self.mName.location=self.coords.returnName()
                
    def template(self):
        template_values={
            'mapType':self.mapType,
           'latitude':self.coords.latitude,
           'longitude':self.coords.longitude,
           'tag':self.coords.tag,
           'location':self.mName.location,
           'locationDir':self.locationList
           }
        path = os.path.join(os.path.dirname(__file__), 'mapTemp.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/maps/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()