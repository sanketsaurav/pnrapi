import re
import lxml.html as parser
import cjson

from settings import *

with open('station_codes.json') as codes:
	station_codes = cjson.decode(codes.read())

def is_pnr_valid(pnr):
	"""
	Checks if the PNR is valid.
	"""
	r = re.compile(PNR_REGEX_STRICT)
	return bool(r.match(pnr))

def despace(string):
	"""
	Removes extraneous spaces.
	"""
	return re.sub(r'\s+', ' ', string)

def groupify_passengers(passenger_list):
	"""
	Groups passenger data.
	"""
	count = len(passenger_list)/3
	groups = []
	for i in range(count):
		del passenger_list[0]
		groups.append((passenger_list.pop(0), passenger_list.pop(0)))

	return groups

def parse_html(html):
	"""
	Takes the HTML and spits out the list of fields
	relevant to the status.

	And please forgive the ugly code. Parsing such awful HTML is indeed ugly.
	"""
	tree = parser.fromstring(html)
	elements = tree.find_class(MAGIC_CLASS)

	fields = []

	for element in elements[:-1]:
		fields.append(despace(element.text or element.getchildren()[0].text).strip())

	return (fields[:3], fields[3:7], fields[7:8], fields[8:-1], fields[-1])

def build_response_dict(data):
	"""
	Takes in the field parameters and builds JSON for spitting out.
	This is kinda ugly, but HTML parsing, you see.
	"""
	global station_codes

	response = {}

	for i in range(len(FIELDS_1)):
		response[FIELDS_1[i]] = data[0][i]

	for j in range(len(FIELDS_2)):
		response[FIELDS_2[j]] = {'code' : data[1][j], 'name' : station_codes[data[1][j]]}

	for k in range(len(FIELDS_3)):
		response[FIELDS_3[k]] = data[2][k]

	response['passenger'] = []
	groups = groupify_passengers(data[3])
	for passenger in groups:
		response['passenger'].append({FIELDS_4[0] : passenger[0], FIELDS_4[1] : passenger[1]})

	response[FIELDS_5[0]] = data[4]

	return response






