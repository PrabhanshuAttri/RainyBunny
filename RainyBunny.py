from twilio.rest import TwilioRestClient
import time
from datetime import datetime
from pytz import timezone
from time import gmtime, strftime
import json
import urllib2

# put your own credentials here 
def sendSMS(body):
	ACCOUNT_SID = "AC2a7f100XXXXXXXXXXXXXXXXXXXXXXXXX" 
	AUTH_TOKEN = "77b9a6e4XXXXXXXXXXXXXXXXXXXXXXXX" 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	mes =  client.messages.create(to="+91XXXXXXXXXX", from_="+14XXXXXXXXX", body=body)
	print mes

while True:
	data = json.load(urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Delhi,India'))
	forec = json.load(urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=Delhi,India'))
	t = float(float(data['main']['temp']) - 272.15)
	fmt = "%d-%m-%Y, %H:%M:%S"
	now_time = datetime.now(timezone('Asia/Kolkata'))
	msg = 'Station: ' + data['name'] + ' ' + now_time.strftime(fmt) + ': Weather: ' + data['weather'][0]['description'] + ', Temp: ' + str(float(t)) + 'C'
	fmt = "%d"
	forec_date = '2015-07-' + str(int(now_time.strftime(fmt)) + 1) +' 12:00:00'
	for x in forec['list']:
		if(str(forec_date) in str(x['dt_txt'])):
			t = float(float(x['main']['temp']) - 272.15)
			msg += ' and ' + x['dt_txt'] + ' Weather:' + x['weather'][0]['description'] + ', Temp: ' + str(float(t)) + 'C'

	print msg
	print 'SMS ID: ',
	sendSMS(msg)
	print '------------------------------------------------------------------------'
	time.sleep(180)
