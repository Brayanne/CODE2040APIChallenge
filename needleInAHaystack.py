import json

import requests

from json import dumps, loads

from urllib2 import Request, urlopen

#putting token in dictionary
info = {'token':'1kupFjlEc9'}
token = dumps(info)
getNeedleHaystack = Request('http://challenge.code2040.org/api/haystack', token) #The url gets string and array of strings in json

#This following line will get the string from json into the variable declared
needleHaystack = loads(urlopen(getNeedleHaystack).read())['result']
print(needleHaystack) # print original string to check afterwards

#gets the value of needle from the string
needle = needleHaystack['needle']
#gets the value of the array for haystack from the string
haystack = needleHaystack['haystack']

#loop to check at what index the needle was found in the haystack
index = 0
for x in haystack:
        if(x == needle):
            break
        else:
            index += 1
print(index)

#put token and needle index into json dictionaries
returnResult = {'token':'1kupFjlEc9', 'needle':index}

#this line will send the token and needle index to the provided url and will
#return result in json
response = Request('http://challenge.code2040.org/api/validateneedle', data = dumps(returnResult))

#get result from json to string
result = loads(urlopen(response).read())['result']

#print result
print(result)
