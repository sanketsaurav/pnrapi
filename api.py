from flask import Flask, jsonify
import requests

from settings import *
from utils import *

app = Flask(__name__)

@app.route('/pnr/<pnr>')
def pnr_api(pnr):
	"""
	Returns the PNR data in JSON after fetching from Indian Railways website.
	"""
	if is_pnr_valid(pnr):
		response = requests.post(BASE_URL, data={PARAM_NAME : pnr})
		if response.status_code is 200:
			pnr_data = parse_html(response.content)

			if not pnr_data:
				return jsonify({'status' : 'PNR FLUSHED / SERVICE UNAVAILABLE',
				'data' : {}
					})

			return jsonify({'status' : 'OK', 
				'data' : build_response_dict(pnr_data)
				})
		else:
			return jsonify({'status' : 'ERROR',
				'data' : {}
				})
	else:
		return jsonify({'status' : 'INVALID PNR',
				'data' : {}
			})

@app.route('/')
def homepage():
	pass
if __name__ == '__main__':
	app.run()