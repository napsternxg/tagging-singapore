import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class SiteProperties():
    sitename=str()
    author=str()
    homepage=str()
    blogs=[]
    apps=[]
    def __init__(self):
        self.sitename="NapsterNXG's Google Apps"
        self.author="Shubhanshu Mishra"
        self.homepage="http://www.napsternxg.0fees.net"
        self.blogs={
            "Tech Blog":"http://napsternxghacked.spaces.live.com/" ,
            "Personal Blog":"http://napsternxg.blogspot.com",
            "Follow me on Twitter":"http://www.twitter.com/napsternxg/"
            }
        self.apps={
            "Home":"/home/",
            "Hello World Application":"/hello/",
            "Gothere Maps API":"/maps/"
            }

class MainPage(webapp.RequestHandler):
    def get(self):
        site=SiteProperties()
        template_values={
            'name':site.sitename,
            'author':site.author,
            'homepage':site.homepage,
            'blogs':site.blogs,
            'apps':site.apps
            }
        print template_values
        path = os.path.join(os.path.dirname(__file__), 'home.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/home/', MainPage),
                                      ('/',MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()