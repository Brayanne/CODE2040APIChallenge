import json

import requests

from json import dumps, loads

from urllib2 import Request, urlopen

#putting token in dictionary
info = {'token':'1kupFjlEc9'}
token = dumps(info)
getstring = Request('http://challenge.code2040.org/api/getstring', token) #The url provide to get string in json

#This following line will get the string from json into the variable declared
unreversedString = loads(urlopen(getstring).read())['result']
print(unreversedString) # print original string to check afterwards

string = unreversedString[::-1] # reverse string

print(string) #print reversed string to compare to original string

#put token and string into json dictionaries
returnResult = {'token':'1kupFjlEc9', 'string':string}

#this line will send the reversed string to the provided url and will
#return result in json
response = Request('http://challenge.code2040.org/api/validatestring', data = dumps(returnResult))

#get result from json to string
result = loads(urlopen(response).read())['result']

#print result
print(result)
