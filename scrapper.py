import os, json, sys
import requests

pin='680008'
str1=""
li=[]

response = requests.get('http://postalpincode.in/api/pincode/'+pin)
data=response.json()
data = json.loads(data)
n=0;
for i in data: 
	print(data['circle'])
	n=n+1