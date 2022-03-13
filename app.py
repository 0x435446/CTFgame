from flask import Flask
from flask import render_template,jsonify
from flask import request,redirect,session,send_file,send_from_directory

import MySQLdb 
import pymysql
from pymysql.converters import escape_string



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

		return render_template('home.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
		return render_template('index.html')

@app.route('/getInfo', methods=['GET', 'POST'])
def getInfo():
	if request.method == 'POST':
		db=MySQLdb.connect(host="localhost",user="root",passwd="FlagFlag123.",db="platformgame" )
		Data = request.form
		ID = int(Data['Challenge']) + 1
		cursor= db.cursor()
		print (ID)
		cursor.execute("SELECT * FROM challenges WHERE ID='"+ escape_string(str(ID))+"'")
		data = (cursor.fetchall())
		Name = data[0][1]
		Descriere = data[0][3]
		Location = data[0][6]
		Category = data[0][7]
		return Name + "|" + Descriere + "|" + Location + "|" + Category



@app.route('/Challenges/<path:filename>', methods=['GET', 'POST'])
def download(filename):  
	return send_from_directory(directory='Challenges', path=filename)




@app.route('/login', methods=['GET', 'POST'])
def login():
		return render_template('login.html')



if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0')
