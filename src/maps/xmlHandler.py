import xml.sax
import os
import cgi
import pprint

from modules import libraries
from modules import maphandler
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class saveXML():
    def __init__(self):
        self.parser=xml.sax.make_parser()
        self.handler=maphandler.mapHandler()
        self.parser.setContentHandler(self.handler)
        path = os.path.join(os.path.dirname(__file__), '../xmlFiles/mapDir.xml')
        self.parser.parse(path)
        self.locationList=self.handler.mapping
        print "XML Initialized"
        pprint.pprint(self.locationList)
        
    def updateDb(self):
        dbHandle=libraries.dbControls(self.locationList)
        dbHandle.updateDb()

class MainPage(webapp.RequestHandler):
  def get(self):
    xmlNew=saveXML()
    xmlNew.updateDb()
    
application = webapp.WSGIApplication([('/maps/updatedb/', MainPage)],debug=True)
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()