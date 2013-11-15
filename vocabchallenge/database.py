import sqlite3
from flask import g, request, session
from vocabchallenge import app

def connect_db():
	print app.config['DATABASE']
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

def feedback(username, userid, feedback):
	g.db.execute('INSERT INTO feedback values(null, datetime(\'now\'), ' + '\''+username+'\'' + ',' + userid + ',' + '\''+feedback+'\'' + ')')
	g.db.commit()