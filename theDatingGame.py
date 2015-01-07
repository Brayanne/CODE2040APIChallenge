import json

import requests

import datetime

from json import dumps, loads

from urllib2 import Request, urlopen

#putting token in dictionary
info = {'token':'1kupFjlEc9'}
token = dumps(info)
#The url gets datestamp and inverrval as a string in json
getDatestampInterval = Request('http://challenge.code2040.org/api/time', token) 

#This following line will get the string from json into the variable declared
datestampInterval = loads(urlopen(getDatestampInterval).read())['result']
print(datestampInterval) # print original string 

#gets the value of datestamp from string
datestamp = datestampInterval['datestamp']
#gets the value of interval from the string
interval = datestampInterval['interval']

#disects datestamp into its different components
year = datestamp[:4]
month = datestamp[5:7]
day = datestamp[8:10]
hour = datestamp[11:13]
minute = datestamp[14:16]
sec = datestamp[17:19]
microsec = datestamp[20:23]


time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(sec), int(microsec))

newTime = time + datetime.timedelta(seconds=interval)

resTime = newTime.isoformat()

#prints result to check 
print(resTime)


#put token and datestamp into json dictionaries
returnResult = {'token':'1kupFjlEc9', 'datestamp':resTime}

#this line will send the token and new array to the provided url and will
#return result in json
response = Request('http://challenge.code2040.org/api/validatetime', data = dumps(returnResult))

#get result from json to string
result = loads(urlopen(response).read())['result']

#print result
print(result)
