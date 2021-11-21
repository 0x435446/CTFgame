from flask import Flask
from flask import render_template,jsonify
from flask import request,redirect,session,send_file

app = Flask(__name__)

app.secret_key = 'PapanasiCuBranza123456'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'FlagFlag123.'
app.config['MYSQL_DB'] = 'BlockIT'

app.config['UPLOAD_FOLDER']='/tmp/upload'
app.config['UPLOAD_EXTENSIONS'] = ['.txt']



@app.route('/', methods=['GET', 'POST'])
def index():
		return render_template('index.html')

@app.route('/getInfo', methods=['GET', 'POST'])
def getInfo():
	if request.method == 'POST':
		Data = request.form
		return Data['Challenge']



if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0')
