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
		
	def key_value(self, tag):
		self.keyValue = []
		count = self.toParse.count('</'+tag+'>')
		for i in range(0,count):
			toScan = self.insideValue(tag)[i]
			#print toScan
			j = len(tag)
			length = len(toScan)
			while j<length:
			
				x = j
				
				token = True
				while token:
					if toScan[x]==(" "):
						x = x+1
					else:
						token = False
					
				y = x
			
				gate = True
				while gate:
					if toScan[y].isalpha():
						y = y+1
					else:
						gate = False
					
				key = toScan[x:y]
				#print key
				
				equal = toScan.find('=',y)
				z = equal+1
			
				next = True
				while next:
					if toScan[z]==(" "):
						z = z+1
					else:
						next = False
					
				holder = toScan[z]
				closer = toScan.find(holder,z+1)
			
				value  = toScan[z+1:closer]
				#print value
				toAdd = key+", "+value
				self.keyValue.append(toAdd)
				
				j = closer+1
				
			# returns the key-value array after searching all available pairs
			if i==(count-1):
				return self.keyValue
				
		
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
