from flask import Flask

app = Flask(__name__)

@app.route('/api/<pnr>')
def hello_world(pnr):
	return 'Hello, %s! Dummy code. Go away for now.' % pnr

if __name__ == '__main__':
	app.run()