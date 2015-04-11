import urllib

from google.appengine.api import urlfetch

class mapCoord():
    latitude=float(1.362083)
    longitude=float(103.819836)
    tag=str("Origin")
      
    def returnName(self):
        url=str("http://tinygeocoder.com/create-api.php?g=")
        url=url+str(self.latitude)+","+str(self.longitude)
        result=urlfetch.fetch(url)
        if result.status_code==200 :
            return result.content
        return 0

class mapName():
    API_KEY={"global":"ABQIAAAAvyOReQFIpPKo-tk11gPZQRRH2DKi8ToSbdT325pHvaGgxm1UCRRPNYrWPnVkZEpKDiahvipXnYOgLg",
             "local":"ABQIAAAAvyOReQFIpPKo-tk11gPZQRT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSH2sCudhTKsfwEqBg3D0NMnIR4CA"}
    location=str()

    def __init__(self,location=""):
        self.location=location

    def returnCoords(self):
        #"http://maps.google.com/maps/geo?q=1600+Amphitheatre+Parkway,+Mountain+View,+CA&output=csv&oe=utf8&sensor=true_or_false&key=ABQIAAAAvyOReQFIpPKo-tk11gPZQRT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSH2sCudhTKsfwEqbg3D0NMnIR4CA"
        url=str("http://tinygeocoder.com/create-api.php?q=")
        """
        url=str("http://maps.google.com/maps/geo?q=")
        self.location=self.location.replace(" ", "+")
        url=url+urllib.quote(self.location+",Singapore")
        url=url+"&output=csv&oe=utf8&sensor=true_or_false&key="+self.API_KEY['local']
        """
        url=url+urllib.quote(self.location+",Singapore")
        #print url
        result=urlfetch.fetch(url)
        if result.status_code==200 :
            return result.content
            #return url
        return 0 
    
    def returnCoordsFormatted(self):
        coords=mapCoord()
        latLong=self.returnCoords()
        try:            
            #print latLong
            latLong=latLong.split(",")
            coords.latitude=float(latLong[0])
            coords.longitude=float(latLong[1])
        except:
            print latLong
        return coords      
