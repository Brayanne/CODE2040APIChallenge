import json

import requests

from json import dumps, loads

from urllib2 import Request, urlopen

#putting token in dictionary
info = {'token':'1kupFjlEc9'}
token = dumps(info)
getPrefixArray = Request('http://challenge.code2040.org/api/prefix', token) #The url gets prefix and array of strings as a string in json

#This following line will get the string from json into the variable declared
prefixArray = loads(urlopen(getPrefixArray).read())['result']
print(prefixArray) # print original string 

#gets the value of prefix from string
prefix = prefixArray['prefix']
#gets the array from the string
array = prefixArray['array']

#loop that will check the prefix of the words in array and add to new array
#the strings that do not have the indicated prefix into it
newArray = []
for x in array:
        if(x[:len(prefix)] != prefix):
            newArray.append(x)
print(newArray)

#put token and new array into json dictionaries
returnResult = {'token':'1kupFjlEc9', 'array':newArray}

#this line will send the token and new array to the provided url and will
#return result in json
response = Request('http://challenge.code2040.org/api/validateprefix', data = dumps(returnResult))

#get result from json to string
result = loads(urlopen(response).read())['result']

#print result
print(result)
