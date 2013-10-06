import re
import lxml.html as parser
import json

from settings import *

def is_pnr_valid(pnr):
	"""
	Checks if the PNR is valid.
	"""
	r = re.compile(PNR_REGEX_STRICT)
	return bool(r.match(pnr))

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
		fields.append(re.sub(r'\s+', ' ', element.text or element.getchildren()[0].text))

	return fields[:3], fields[3:7], fields[7:8], fields[8:-1], fields[-1]