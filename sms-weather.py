from twilio.rest import TwilioRestClient
import time
from datetime import datetime
from pytz import timezone
from time import gmtime, strftime
import json
import urllib2


def pretty_print(str):
    print json.dumps(str, indent=4, sort_keys=True)

def pretty(str):
    return json.dumps(str, indent=4, sort_keys=True)
    
def sendSMS(body):
  # put your own credentials here 
	ACCOUNT_SID = "AC2a7f1002XXXXXXXXXXXXXXXXXXXXXXXX" 
	AUTH_TOKEN = "77b9a6e4XXXXXXXXXXXXXXXXXXXXXXXX" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	 
	mes =  client.messages.create(to="+918287032944", from_="+14043694122", body=body)
	print mes

while True:
	data = json.load(urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Delhi,India'))
	t = float(float(data['main']['temp']) - 272.15)
	fmt = "%d-%m-%Y, %H:%M:%S %Z%z"
	now_time = datetime.now(timezone('Asia/Kolkata'))
	msg = now_time.strftime(fmt) + ': Station: ' + data['name'] + ', Weather: ' + data['weather'][0]['description'] + ', Temp: ' + str(float(t)) + 'C'
	print msg
	print 'SMS ID: ',
	sendSMS(msg)
	print '------------------------------------------------------------------------'
	time.sleep(180)
