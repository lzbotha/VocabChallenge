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

def get_entry(difficulty):
    cur = g.database.cursor()
    cur.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')
    word, definition = cur.fetchone()
    cur.close()
    return (word, definition)

def insert_game(username, userid, score, hints):
    cur = g.database.cursor()
    cur.execute('INSERT INTO games (userid, username, score, hints) VALUES(%s,%s,%s,%s)',(userid,username,score,hints))
    cur.close()

def get_highscore(userid):
    cur = g.database.cursor()
    cur.execute('SELECT MAX(score) FROM games WHERE userid = %s', [userid])
    highscore = cur.fetchone()
    cur.close()
    return highscore[0]

def get_top(x):
    cur = g.database.cursor()
    cur.execute('SELECT username, SUM(score) FROM games GROUP BY username LIMIT %s', [x])
    topx = [dict(username=row[0], score=row[1]) for row in cur.fetchall()]
    cur.close()
    return topx

# http://toolserver.org/~enwikt/definitions/ wikitionary definition dump