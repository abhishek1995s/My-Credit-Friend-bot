import os, json, sys
import requests
from bs4 import BeautifulSoup

str1=""
li=[]
#print type(li)
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"}
response = requests.get('https://www.bankbazaar.com/home-loan.html', headers=header)
#print(response)
soup = BeautifulSoup(response.text, 'html.parser')
n=1
mover=[]
#for h in soup.findAll('div' ,attrs={"class" : "offer-section-column col-same-height col-middle card"}):
	# i=0
	# t=soup.find('span' ,attrs={"class" : "js-title js-format-string value-title"})
	# # mover[i]["name"]=t.getText()
	# print(t.getText())
	# i=i+1
for r in soup.findAll('div' ,attrs={"class" : "offer-section-column col-same-height col-middle interest-rate-range"}):
	 i=0
	 # mover[i]["range"]=r.getText()
	 print r.getText() 
	 i=i+1
# for rt in soup.findAll('div' ,attrs={"class" : "offer-section-column col-same-height col-middle tenure-range"}):
# 	 i=0
# 	 print(rt.getText())
# 	 mover[i]["tenure"]=rt.getText()
# 	 i=i+1
# for rq in soup.findAll('div' ,attrs={"class" : "offer-section-column col-same-height col-middle processing-fee-range"}):
# 	 i=0
# 	 tel=rq.getText()
# 	 print(tel)
# 	 mover[i]["pfee"]=rq.getText()	
# 	 i=i+1 
     
	 
# for rf in soup.findAll('div' ,attrs={"class" : "offer-section-column col-same-height col-middle loan-amount-range"}):
# 	i=0
	 
# 	mover[i]["arange"]=rf.getText()
# 	print(rf.getText())	 
# 	i=i+1
# count = 0
# for i in mover:
# 	name = "name"+str(count)
# 	range = "range"+str(count)
# 	results[name] = i['name']
# 	results[range] = i['range']
# 	print("name --> "+str(count)+str(i['name']))
# 	print("range --> "+str(count)+str(i['range']))         	
# 	count += 1







