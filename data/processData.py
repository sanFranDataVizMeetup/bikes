# A python script to process raw bike accident data and add useful fields.

import sys
import json

from addDay import addDay

def main():
	# Read the bike accidents JSON file
	jsonstr = open(sys.argv[1]).read()
	data = json.loads(jsonstr)

	accidents = data['accidents']

	# Add the type of day
	data['accidents'] = addDay(accidents)

	jsonexport = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

	f = open(sys.argv[1] + ".export.json", 'w')
	f.write(jsonexport)
	f.close()

if __name__ == '__main__':
	main()