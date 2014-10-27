# A python function adding the historical weather conditions to the bike accident JSON file

def addWeather(data):
	import datetime
	import json
	import urllib2

	print len(data)

	for accident in data:
		# Format and decompose the date in year, month and day
		date = accident['date']
		date = date[-8:]
		y = date[0:4]
		m = date[4:6]
		d = date[6:8]

		apiKey = str(json.loads(open('apikey.secret.config').read())['apikey'])

		url = "http://api.wunderground.com/api/" + apiKey + "/history_" + y + m + d + "/q/CA/San_Francisco.json"

		res = json.loads(urllib2.urlopen(url).read())

		from pprint import pprint
		pprint(res)