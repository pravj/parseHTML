    class parseHTML:
  	def __init__(self, input):
		self.toParse = input
	
	def count(self, tag):
		return self.toParse.count('</'+tag+'>')
		
	def insideValue(self, tag):
		self.Value = []
		count = self.toParse.count('</'+tag+'>')
		x = 0
		start = 0
		while x<count:
			first = self.toParse.find('<'+tag,start)
			end   = self.toParse.find('>',first+1)
			inner = self.toParse[first+1:end]
			self.Value.append(inner)
			x=x+1
			start = end+1
		return self.Value
		
	def tag_Data(self, tag):
		self.Data = []
		count = self.toParse.count('</'+tag+'>')
		x = 0
		start = 0
		while x<count:
			first = self.toParse.find('<'+tag,start)
			end   = self.toParse.find('>',first+1)
			last  = self.toParse.find('</'+tag+'>',end+1)
			x = x+1
			start = last+len('</'+tag+'>')
			data  = self.toParse[end+1:last]
			self.Data.append(data)
		return self.Data
		
	def isAttr(self, toCheck, attr=""):
		if attr=="":
			return "you have not entered any attribute"
		elif attr!="":
			where = toCheck.find(attr)
			
			if where!=-1:
				return True
			else:
				return False
			
	def isValue(self, toCheck, value=""):
		if value=="":
			return "you have not entered any attribute-value"
		elif value!="":
			where = toCheck.find(value)
			
			if where!=-1:
				return True
			else:
				return False
	
	def Attr_Value(self, toCheck ,attr=""):
		if attr=="":
			return "you have not entered any attribute"
		elif attr!="":
			where = toCheck.find(attr)
			
			if(where!=-1):
				x = where+1
				while toCheck[x]!="=":
					x = x+1
				
				y = x+1
				go = True
				while go:
					if toCheck[y]==(" "):
						y = y+1
					else:
						go = False
					
				starter = toCheck[y]
				closer  = toCheck.find(starter,y+1)
				return toCheck[y+1:closer]
				
			else:
				return False
