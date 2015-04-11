import urllib

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class MainPage(webapp.RequestHandler):
    location="Farrer Park"
    def get(self):
        API_KEY={"global":"ABQIAAAAvyOReQFIpPKo-tk11gPZQRRlOb26qSyU154aZeLwOrF4C7-DphSGwTbdcC0e38aRFadwYwuVnrVyfg",
             "local":"ABQIAAAAvyOReQFIpPKo-tk11gPZQRT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSH2sCudhTKsfwEqBg3D0NMnIR4CA"}
        url=str("http://maps.google.com/maps/geo?q=")
        self.location=self.location.replace(" ", "+")
        url=url+urllib.quote(self.location+",Singapore")
        url=url+"&output=csv&oe=utf8&sensor=true_or_false&key=ABQIAAAAvyOReQFIpPKo-tk11gPZQRRlOb26qSyU154aZeLwOrF4C7-DphSGwTbdcC0e38aRFadwYwuVnrVyfg"
        #print url
        result=urlfetch.fetch(url)
        if result.status_code==200 :
            self.response.out.write(result.content+"<br />API_KEY Global is "+ API_KEY['global'])
        
application = webapp.WSGIApplication(
                                     [('/maps/test/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()