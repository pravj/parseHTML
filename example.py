# imports parseHTML class
from parseHTML import parseHTML

# HTML data to parse
data  = "<html><head></head><body><a class ='sds' href='cs'>here</a><div>this is a div</div><a href='img' id='ec'>here</a><a href='edc' id='ee'>there</a></body></html>"

# initialize the parseHTML class with 'data'
parse = parseHTML(data)

# counts total number of anchor('a') tag
count = parse.count('a')
print count
# here it will print 3

# print data inside a tag
print parse.tag_Data('a')
# here it will return this array ['here', 'here', 'there']

# inside data
inside = parse.insideValue('a')
print inside
# here it will return this array ["a class ='sds' href='cs'", "a href='img' id='ec'", "a href='edc' id='ee'"]

# returns attribute value
print parse.Attr_Value(inside[0],"href")
# here it will 'cs'

# returns array of attribute key-value pair
print parse.key_value('a')
# here it will return ['class, sds', 'href, cs', 'href, img', 'id, ec', 'href, edc', 'id, ee']

# use of 'isValue' and 'isAttr' methods
for i in range(0,count):
  if parse.isValue(inside[i],"img") and parse.isAttr(inside[i],"href"):
    print parse.Attr_Value(inside[i], "id")
# will print 'ec'


