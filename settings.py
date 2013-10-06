PARAM_NAME = "lccp_pnrno1"

BASE_URL = "http://www.indianrail.gov.in/cgi_bin/inet_pnrstat_cgi.cgi"

PNR_REGEX_STRICT = r'^[0-9]{10}$'

MAGIC_CLASS = 'table_border_both'

FIELDS_1 = (
		'train_number',
		'train_name',
		'travel_date',
	)

FIELDS_2 = (
		'from',
		'to',
		'alight',
		'board',
	)

FIELDS_3 = (
		'class',
	)

FIELDS_4 = (
		'seat_number',
		'status',
	)
FIELDS_5 = (
		'chart_prepared',
	)