from flask import Flask,request,jsonify
import json
import requests
app = Flask(__name__)

@app.route("/api")
def hello():
	param1 = request.args.get('q')
	pin=param1
	str1=""
	results={}
   
	response = requests.get('http://postalpincode.in/api/pincode/'+pin)
	data=response.json()
 	

	n=0;
	for i in data: 
		ni=data['PostOffice'][0]['Circle']
		break
	response2=requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=banks+in+'+ni+'&key=AIzaSyDXorUkteB_1Nd7mJnbdkuX4aDOMI7xMag')
	data2= response2.json()
	count = 0
	for i in data2['results']:
		name = "name"+str(count)
		address = "address"+str(count)
		results[name] = i['name']
		results[address] = i['formatted_address']
		print("name --> "+str(count)+str(i['name']))
		print("address --> "+str(count)+str(i['formatted_address']))         	
		#results.append({'name': i['name'], 'address' : i['formatted_address']})
		count += 1

	return json.dumps(results, ensure_ascii=False, encoding='utf8')

if __name__ == "__main__":
    app.run()	
