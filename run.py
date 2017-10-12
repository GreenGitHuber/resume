from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    #data = read_json_file('static/data/index.json')
    return render_template('index.html')

if __name__ == '__main__':
	# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
	# sock.settimeout(CHECK_TIMEOUT)  
	# sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)    
	# sock.bind(('', UDP_PORT))  
    app.run(debug=True)