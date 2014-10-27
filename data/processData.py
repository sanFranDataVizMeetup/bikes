# A python script to process raw bike accident data and add useful fields.

import sys
import json

from addDay import addDay
from addWeather import addWeather

def main():
	# Read the bike accidents JSON file
	jsonstr = open(sys.argv[1]).read()
	data = json.loads(jsonstr)

	# Add the type of day
	data['accidents'] = addDay(data['accidents'])
	data['accidents'] = addWeather(data['accidents'])

	from pprint import pprint
	pprint(data['accidents'])

	jsonexport = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

	f = open(sys.argv[1] + ".export.json", 'w')
	f.write(jsonexport)
	f.close()

if __name__ == '__main__':
	main()