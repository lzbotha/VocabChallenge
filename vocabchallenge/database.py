import psycopg2
from flask import g, request, session
from vocabchallenge import app

def connect_db():
    database = psycopg2.connect('dbname=%s user=%s' % (app.config['DATABASE_NAME'], app.config['DATABASE_USER']))
    return database

def disconnect_db():
    g.database.commit()
    g.database.close()

@app.before_request
def before_request():
    g.database = connect_db()

@app.teardown_request
def teardown_request(exception):
    disconnect_db()

def feedback(username, userid, feedback):
    cur = g.database.cursor()
    cur.execute('INSERT INTO feedback (datetime,username,userid,feedback) VALUES(\'now\',%s,%s,%s)',(username,userid,feedback))
    cur.close()

# http://toolserver.org/~enwikt/definitions/ wikitionary definition dump