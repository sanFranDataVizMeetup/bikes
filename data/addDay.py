
# A python function adding the day, and type of day to the bike accident JSON file
# open file
import json
from pprint import pprint
open('new_crash_data.json', 'w')
with open('sanfrancisco_crashes_cp.json', 'rw') as json_data:
	json_data = json.load(json_data)
	accidents = json_data['accidents']
	#pprint(data)

def convertDate(data):
	for accident in data:
		date = accdent['date']



def addDay(data):
	import datetime
	newdata = []

	for accident in data:
		# Format and decompose the date in year, month and day
		date = accident['date']
		date = date[-8:]
		y = int(date[0:4])
		m = int(date[4:6])
		d = int(date[6:8])

		# Convert to a datetime object
		dt = datetime.date(y,m,d)

		# Create new fields in the accident object
		accident[u'date'] = date
		date = date[2:]
		date = int(date)
		accident[u'weekday'] = dt.weekday()
		accident[u'weekdayname'] = weekdayname(accident[u'weekday'])

		# Determine is the day is a work or weekend day
		# TODO: get the list of public holidays
		if accident[u'weekday'] < 5:
			accident[u'weekdaytype'] = 0
			accident[u'weekdaytypename'] = u'Workday'
		else:
			accident[u'weekdaytype'] = 1
			accident[u'weekdaytypename'] = u'Weekend day'

		newdata.append(accident)
	return newdata

def weekdayname(i):
    days = [u'Monday', u'Tuesday', u'Wednesday', u'Thursday', u'Friday', u'Saturday', u'Sunday']
    return days[i]

print addDay(accidents)
