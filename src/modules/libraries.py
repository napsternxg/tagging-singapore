import pprint

from google.appengine.ext import db

class coordinates():
    latitude=float();
    longitude=float();
    def __init__(self,lat=1.362083,long=103.819836):
        self.latitude=lat
        self.longitude=long

    def setCoordinates(self,lat,long):
        self.latitude=lat
        self.longitude=long
        
    def getCoordinates(self):
        return self

class location():
    name=str()
    coordinates=coordinates()
    address=str()
    tags=[]
    def __init__(self,name,coordinates):
        self.name=name
        self.coordinates=coordinates
        
    def setLocation(self,name,coordinates):
        self.name=name
        self.coordinates.latitude=coordinates.latitude
        self.coordinates.longitude=coordinates.longitude
    
    def setTag(self,tag):
        self.tags.append(tag)
    
    def getLocation(self):
        return self
    
    def getName(self):
        return self.name
    
    def getCoordinates(self):
        return self.coordinates

class directoryDb(db.Model):
    locationName=db.StringProperty()  #  stores the name of the location which is unique to all locations.
    locationAddress=db.StringProperty()  #  stores the address of the location.
    locationLatitude=db.FloatProperty()  #  stores the latitude of the place.
    locationLongitude=db.FloatProperty()  #  stores the longitude of the place. 
    locationTag=db.StringListProperty()  #  stores all the tags associated with the location.
    
    # you can add other properties to the location by defining them above. 
    
    def updateDb(self):
        query=db.GqlQuery("SELECT * FROM directoryDb WHERE locationName=:1", self.locationName)
        updateEntry=query.get()
        self.checkDuplicate(updateEntry.locationTag)
        if updateEntry and self.checkLen()>0:
            updateEntry.locationTag.extend(self.locationTag)
            db.put(updateEntry)
            return self.locationTag
        else:
            return self.locationTag
        
    def checkLen(self):
        for tag in self.locationTag:
             if str(tag)=="":
                 self.locationTag.remove(tag)
        return len(self.locationTag)
    def checkDuplicate(self,tagList):
        for tag in tagList:
            if tag in self.locationTag:
                self.locationTag.remove(tag)
    """
    def getLocation(self):
        location=location()
        location.name=self.locationName
        location.coordinates.latitude=self.locationLatitude
        location.coordinates.longitude=self.locationLongitude
        location.tags=self.locationTag
        return location
    """
class dbControls():
    locationList=[]
    
    def __init__(self,locationList):
        self.locationList=locationList
        
    def updateDb(self):
        for location in self.locationList:
            self.addEntry(location)
            
    def addEntry(self, location):
        dbDir=directoryDb(key_name=location['name'])
        dbDir.locationName=str(location['name'])
        dbDir.locationAddress=(str(location['address']),str(location['name']))[str(location['address'])!=None]
        dbDir.locationLatitude=float(location['latitude'])
        dbDir.locationLongitude=float(location['longitude'])
        tagList=[]
        if location['tags']:
            tagList=location['tags'].split(",")
            for tag in tagList:
                tag=str(tag).strip()                
        dbDir.locationTag=tagList
        dbDir.put() 
        print "Updated Database with the following entries.<br />"  
        print str(dbDir)

        
class TagGen(list):
    def __init__(self,tagListStr):
        tagList=tagListStr.split(",")
        for tag in tagList:
            if str(tag):
                self.append(str(tag).strip())# print self  