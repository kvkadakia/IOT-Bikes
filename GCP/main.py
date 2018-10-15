# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request
import firebase_admin
import urllib3
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from flask import render_template
import json
from os import system
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.

app = Flask(__name__)


# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'smart-bike-share',
})

fdb = firestore.client()

'''
@app.route('/updateLocation', methods=['GET'])
def updateDB():
    """Return a friendly HTTP greeting."""
    #v = request.form.get('authuser')
    #query = parse.parse_qs(parse.urlsplit(request.url).query)
    #http = urllib3.PoolManager()
    #r = http.request('GET',request.base_url)
    #parsed = urlparse.urlparse()
    #query = urlparse.parse_qs(parsed.query)
    
    safeLat = 40
    minLat = safeLat-2
    maxLat = safeLat + 2
    
    safeLongi = 90
    minLongi = safeLongi-2
    maxLongi = safeLongi + 2
    
    userID = request.args.get('authuser')
    if userID is None:
    	userID = '0'
    lat = request.args.get('lat')
    longitude = request.args.get('longi')
    cycleID = request.args.get('cycleID')
    if cycleID is None:
    	cycleID = '0'
        
    doc_ref = fdb.collection(u'Location').document(userID+"_"+cycleID)
    doc_ref.set({
    	u'lat':lat,
    	u'longi':longitude,
    	
    })
    
    out_of_range = False;
    if int(lat)<minLat or int(lat)>maxLat:
    	out_of_range = True;
    if int(longitude)<minLongi or int(longitude)>maxLongi:
    	out_of_range=True;
    	
    #return 'test'+request.args.get('authuser')
    
    if out_of_range:
    	return "{'away':true}"
    return "{'away':false}"
'''    

@app.route('/updateLocations',methods=['POST'])
def updateDB():
	req_data = request.get_json()
	
	safeLat = 40.0
	minLat = safeLat-2.0
	maxLat = safeLat + 2.0
	
	safeLongi = 90.0
	minLongi = safeLongi-2.0
	maxLongi = safeLongi + 2.0
	
	userID = req_data['authuser']
	cycleID = req_data['cycleID']
	lat = req_data['lat']
	longi = req_data['longi']
	
	doc_ref = fdb.collection(u'Location').document(userID+"_"+cycleID)
	doc_ref.set({
		u'lat':lat,
		u'longi':longi
	})
	
	out_of_range = False;
	if float(lat)<minLat or float(lat)>maxLat:
		out_of_range = True
		merchantAuth = apicontractsv1.merchantAuthenticationType()
		merchantAuth.name = '4t8eNZ3F'
		merchantAuth.transactionKey = '8PL4aPbeCj6334pH'

		creditCard = apicontractsv1.creditCardType()
		creditCard.cardNumber = "4111111111111111"
		creditCard.expirationDate = "2020-12"

		payment = apicontractsv1.paymentType()
		payment.creditCard = creditCard

		transactionrequest = apicontractsv1.transactionRequestType()
		transactionrequest.transactionType = "authCaptureTransaction"
		transactionrequest.amount = Decimal ('1.55')
		transactionrequest.payment = payment


		createtransactionrequest = apicontractsv1.createTransactionRequest()
		createtransactionrequest.merchantAuthentication = merchantAuth
		createtransactionrequest.refId = "MerchantID-0001"

		createtransactionrequest.transactionRequest = transactionrequest
		createtransactioncontroller = createTransactionController(createtransactionrequest)
		createtransactioncontroller.execute()

		response = createtransactioncontroller.getresponse()

		if (response.messages.resultCode=="Ok"):
			print "Transaction ID : %s" % response.transactionResponse.transId
		else:
			print "response code: %s" % response.messages.resultCode
	if float(longi)<minLongi or float(longi)>maxLongi:
		out_of_range = True
		merchantAuth = apicontractsv1.merchantAuthenticationType()
		merchantAuth.name = '5KP3u95bQpv'
		merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

		creditCard = apicontractsv1.creditCardType()
		creditCard.cardNumber = "4111111111111111"
		creditCard.expirationDate = "2020-12"

		payment = apicontractsv1.paymentType()
		payment.creditCard = creditCard

		transactionrequest = apicontractsv1.transactionRequestType()
		transactionrequest.transactionType = "authCaptureTransaction"
		transactionrequest.amount = Decimal ('1.55')
		transactionrequest.payment = payment


		createtransactionrequest = apicontractsv1.createTransactionRequest()
		createtransactionrequest.merchantAuthentication = merchantAuth
		createtransactionrequest.refId = "MerchantID-0001"

		createtransactionrequest.transactionRequest = transactionrequest
		createtransactioncontroller = createTransactionController(createtransactionrequest)
		createtransactioncontroller.execute()

		response = createtransactioncontroller.getresponse()

		if (response.messages.resultCode=="Ok"):
			print "Transaction ID : %s" % response.transactionResponse.transId
		else:
			print "response code: %s" % response.messages.resultCode
		
	if out_of_range:
		return "{'away':true}"
	return "{'away':false}"
	

@app.route('/triggerCall',methods=['GET'])
def makeCall():
	system('python autoCall.py')
	return "Called"

@app.route('/getLocations',methods=['GET','POST'])
def fetchLocs():
	
	
	#try:
	coll = fdb.collection(u'Location')#.document(u'2312_0)
	docs = coll.get()
	results = "["
	i=0
	for doc in docs:
	    results += (u'{}'.format(doc.to_dict())) + ","
	results = results[:-1]
	results += "]"
	
	
	#return (u'Document data: {}'.format(doc.to_dict()))
	return render_template("maps.html", results=results)
	#except:
	#	return "Nothing found"
	#return results.doc()#.hashCode()
	#return 'hello karan'
	
@app.route('/sensor',methods=['POST'])
def getSense():
	req_data = request.get_json()
	
	userID = req_data['userId']
	cycleID = req_data['deviceId']
	tempSense = req_data['temperature']
	vibrSense = req_data['vibration']
	lightSense = req_data['light']
	
	contactNum = '+13128046895'
	maxTemp=50.0
	if float(tempSense)>=maxTemp:
		system('python autoMsg.py')
	
	doc_ref = fdb.collection(u'Location').document(userID+"_"+cycleID)
	doc_ref.set({
		u'tempSense':tempSense,
		u'vibrSense':vibrSense,
		u'lightSense':lightSense
	})
    
	return 'All good'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
