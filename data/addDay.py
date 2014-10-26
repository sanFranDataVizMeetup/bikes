# A python function adding the day, and type of day to the bike accident JSON file

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