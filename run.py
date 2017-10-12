from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_file(file_path):
	jsonfile = open(file_path,'r+')
	jsontext = jsonfile.read()
	data = json.loads(jsontext)
	return data

@app.route('/')
def hello_world():
    data = read_json_file('static/data/index.json')
    return render_template('index.html',data=data)

@app.route('/detail/<string:student_number>')
def look_details(student_number):
	data = read_json_file('static/data/index.json')
	user_data={}
	for item in data:
		if student_number == item['student_num']:
			user_data = item
			break
	return render_template('detail.html',data=user_data)

if __name__ == '__main__':
	# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
	# sock.settimeout(CHECK_TIMEOUT)  
	# sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)    
	# sock.bind(('', UDP_PORT))  
    app.run(debug=True)
