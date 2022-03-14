from flask import Flask
from flask import render_template,jsonify
from flask import request,redirect,session,send_file,send_from_directory

import MySQLdb 
import pymysql
from pymysql.converters import escape_string
import hashlib


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
	if "loggedin" in session:
		if session['loggedin'] == True:
			return render_template('home.html')
		else:
			session['loggedin'] = False
			session['Username'] = ""
			session['IDUser'] = ""
			return redirect("/login")
	else:
		session['loggedin'] = False
		return redirect("/login")




@app.route('/game', methods=['GET', 'POST'])
def game():
	if "loggedin" in session:
		if session['loggedin'] == True:
			return render_template('game.html')
		else:
			session['loggedin'] = False
			session['Username'] = ""
			session['IDUser'] = ""
			return redirect("/login")
	else:
		session['loggedin'] = False
		session['Username'] = ""
		session['IDUser'] = ""
		return redirect("/login")

@app.route('/getInfo', methods=['GET', 'POST'])
def getInfo():
	if "loggedin" in session:
		if session['loggedin'] == True:
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
		else:
			session['loggedin'] = False
			session['Username'] = ""
			session['IDUser'] = ""
			return redirect("/login")
	else:
		session['loggedin'] = False
		session['Username'] = ""
		session['IDUser'] = ""
		return redirect("/login")



@app.route('/Challenges/<path:filename>', methods=['GET', 'POST'])
def download(filename):  
	if "loggedin" in session:
		if session['loggedin'] == True:
			return send_from_directory(directory='Challenges', path=filename)
		else:
			session['loggedin'] = False
			session['Username'] = ""
			session['IDUser'] = ""
			return redirect("/login")
	else:
		session['loggedin'] = False
		session['Username'] = ""
		session['IDUser'] = ""
		return redirect("/login")




@app.route('/login', methods=['GET', 'POST'])
def login():
	if "loggedin" in session:
		if session['loggedin'] == True:
			return redirect("/")
	if request.method == 'POST':
		Data = request.form
		Username = Data['Username']
		Username = escape_string(Username)
		Password = escape_string(hashlib.sha256(Data['Password'].encode()).hexdigest())
		db=MySQLdb.connect(host="localhost",user="root",passwd="FlagFlag123.",db="platformgame" )
		cursor = db.cursor()
		sql = ("SELECT ID, Username, Password FROM users WHERE Username = %s and Password = %s")
		cursor.execute(sql, (Username, Password))
		users = list(cursor.fetchall())
		if len(users) == 1:
			session['loggedin'] = True
			session['Username'] = Username
			session['IDUser'] = str(users[0][0])
		return redirect("/")


	return render_template('login.html')
	


@app.route('/register', methods=['GET', 'POST'])
def register():
	if "loggedin" in session:
		if session['loggedin'] == True:
			return redirect("/")
	if request.method == 'POST':
		Data = request.form
		Username = Data['Username']
		Username = escape_string(Username)
		db=MySQLdb.connect(host="localhost",user="root",passwd="FlagFlag123.",db="platformgame" )
		cursor = db.cursor()
		sql = ("SELECT Username FROM users WHERE Username = %s")
		cursor.execute(sql, ([Username]))
		users = list(cursor.fetchall())
		if len(users) == 0:
			if len(Username) > 5:
				Password = escape_string(hashlib.sha256(Data['Password'].encode()).hexdigest())
				Email = escape_string(Data['Email'])
				sql = "INSERT INTO users (Username,Password,Email,Points) VALUES (%s, %s, %s, %s)"
				cursor.execute(sql, (Username, Password, Email, 0))
				db.commit()
				db.close()
				return redirect("/")
		return render_template('login.html')
	else:
		return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
	if "loggedin" in session:
		if session['loggedin'] == True:
			session['loggedin'] = False
			session['Username'] = ""
			session['IDUser'] = ""
	
	return render_template('login.html')



@app.route('/sendFlag', methods=['GET', 'POST'])
def sendFlag():
	if "loggedin" in session:
		if session['loggedin'] == True:
			if request.method == 'POST':
				Data = request.form
				print (Data)
				Flag = Data['Flag']
				Flag = escape_string(Flag)
				print (Flag)
				Nume = Data['Name']
				Nume = escape_string(Nume)
				print (Nume)
				db=MySQLdb.connect(host="localhost",user="root",passwd="FlagFlag123.",db="platformgame" )
				cursor = db.cursor()
				sql = ("SELECT Puncte FROM challenges WHERE Nume = %s and Flag = %s")
				cursor.execute(sql, (Nume, Flag))
				flag = list(cursor.fetchall())
				if len(flag) > 0:

					Points = flag[0][0]
					sql = ("SELECT * FROM solves WHERE Challenge = %s and ID_User = %s")
					cursor.execute(sql, (Nume, session['IDUser']))
					solved = list(cursor.fetchall())
					print (len(solved))

					if len(solved) == 0:

						sql = "INSERT INTO solves (ID_User,Challenge) VALUES (%s, %s)"
						cursor.execute(sql, (session['IDUser'], Nume))
						db.commit()

						sql = ("SELECT Points FROM users WHERE Username = %s ")
						cursor.execute(sql, ([session['Username']]))
						userPoints = list(cursor.fetchall())
						totalPoints = Points + int(userPoints[0][0])

						sql = ("UPDATE users SET Points = %s WHERE Username = %s")
						cursor.execute(sql, (str(totalPoints),session['Username']))
						db.commit()
						db.close()
				return "DA"
	return redirect("/")





@app.route('/account', methods=['GET', 'POST'])
def account():
	if "loggedin" in session:
		if session['loggedin'] == True:
			db=MySQLdb.connect(host="localhost",user="root",passwd="FlagFlag123.",db="platformgame" )
			cursor = db.cursor()
			sql = ("SELECT Points FROM users WHERE Username = %s ")
			cursor.execute(sql, ([session['Username']]))
			userPoints = list(cursor.fetchall())[0][0]
			db.close()
			return render_template('account.html',username=session['Username'],points=userPoints)
		else:
			session['loggedin'] = False
			session['Username'] = ""
			session['IDUser'] = ""
			return redirect("/login")
	else:
		session['loggedin'] = False
		session['Username'] = ""
		session['IDUser'] = ""
		return redirect("/login")




if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0')
