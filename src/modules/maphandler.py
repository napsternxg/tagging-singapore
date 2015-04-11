import xml.sax.handler

class mapHandler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.inLocation=0
		self.mapping=list()
		self.tagList=["location", "name", "address", "latitude", "longitude", "tags"]
		
	def startElement(self,name,attributes):
		if name=="location":
			self.buffer={}
			for i in range(len(self.tagList)):
			 self.buffer[self.tagList[i]]=""
		else:
			for i in range(1,len(self.tagList)):
				if name==self.tagList[i]:
					self.inLocation=i
			
	def characters(self,data):
		i=self.inLocation
		if ((i)>0 and i<len(self.tagList)):
			self.buffer[self.tagList[i]]=data  
			

	def endElement(self, name):
		if self.inLocation>0 and self.inLocation<len(self.tagList)-1:
		  for i in range(1,len(self.tagList)-1):
				if name==self.tagList[i]:
					self.inLocation=0
		elif name==self.tagList[len(self.tagList)-1]:
		  self.inLocation = 0
		  print self.buffer
		  self.mapping.append(self.buffer)
			