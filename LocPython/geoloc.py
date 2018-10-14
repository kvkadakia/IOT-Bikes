import time
import requests
import json

while True:
	response = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyB0777xG5WuMDor6fvoADVa6oCoO1IT__k')
	resp = response.json()
	print(resp["location"]["lat"], resp["location"]["lng"])
	headers = {'content-type': 'application/json'}
	data = {"lat":resp["location"]["lat"],"longi":resp["location"]["lng"],"authuser":"user123","cycleID":"MH1015"}
	#print(type(data))
	json_data = json.dumps(data)		
	#data = json.loads(""" {"newLatitude":"41.8698","newLongitude":"-95.6496","oldLatitude":"41.662977","oldLongitude":"-91.53831799","deviceId":"2"}""")
	response = requests.post('http://35.1.78.12:3000/geoData',json_data, headers = headers )
	#print(response)
	time.sleep(5)