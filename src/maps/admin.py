import os

from modules import libraries,mapHelper
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from django.contrib.sites.models import Site

class MainPage(webapp.RequestHandler):
    LocationList=[]
    def fetchAll(self):
        self.LocationList=libraries.directoryDb.all()
        self.LocationList.order("-locationName")
        
    def get(self):
        self.fetchAll()
        self.template()
        
    def post(self):
        error=""
        locationName=self.request.get('locationName')
        tagListStr=self.request.get('locationTag')
        tagList=libraries.TagGen(tagListStr)
        #print "PostList"
        #print str(tagList)
        error = []
        if tagList:
            dbObj=libraries.directoryDb()
            dbObj.locationName=locationName
            dbObj.locationTag=tagList
            error=dbObj.updateDb()
        tagLen=len(error)
        error=",".join(error)
        error=str(tagLen)+","+error
            
        self.response.out.write(locationName+","+error+",Error:"+error)
        
    def template(self):
        template_values={
            "locations": self.LocationList,
           }
        path = os.path.join(os.path.dirname(__file__), 'admin1.html')
        self.response.out.write(template.render(path, template_values))
        
class addEntry(webapp.RequestHandler):
    
    def post(self):
        locationName=self.request.get("locationName")
        locObj=libraries.directoryDb(key_name=locationName)        
        locObj.locationName=locationName        
        locObj.locationAddress=self.request.get("locationAddress")
        locName=mapHelper.mapName()
        locName.location=(locObj.locationName,locObj.locationAddress)[locObj.locationAddress==None]
        #print "Location Name:"+locName.location
        locCoords=locName.returnCoordsFormatted()
        locObj.locationLatitude=locCoords.latitude
        locObj.locationLongitude=locCoords.longitude
        locObj.locationTag.extend(libraries.TagGen(self.request.get("locationTags")))
        locObj.put()
        template_values={
            "location": locObj,
           }
        path = os.path.join(os.path.dirname(__file__), 'addEntity.html')
        self.response.out.write(template.render(path, template_values))
        
        

application = webapp.WSGIApplication(
                                     [('/maps/admin/', MainPage), ('/maps/admin/add/', addEntry)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()