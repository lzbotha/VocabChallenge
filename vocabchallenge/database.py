import psycopg2
from flask import g, request, session
from vocabchallenge import app

def connect_db():
    database = psycopg2.connect('dbname=%s user=%s' % (app.config['DATABASE_NAME'], app.config['DATABASE_USER']))
    return database

def disconnect_db():
    g.database.commit()
    g.database.close()

def create_user():
    g.database.rollback()
    #other stuff
    session['username'] = 'roflpop'
    session['userid'] = 0

@app.before_request
def before_request():
    g.database = connect_db()
    #create a new user here if necessary
    create_user()

@app.teardown_request
def teardown_request(exception):
    disconnect_db()

def feedback(userid, feedback):
    cur = g.database.cursor()
    cur.execute('INSERT INTO feedback (datetime,userid,feedback) VALUES(\'now\',%s,%s)',(userid,feedback))
    cur.close()

def get_entry(language):
    cur = g.database.cursor()
    if language=='english':
        cur.execute('SELECT * FROM english_words ORDER BY RANDOM() LIMIT 1')
    elif language=='afrikaans':
        cur.execute('SELECT * FROM afrikaans_words ORDER BY RANDOM() LIMIT 1')
    elif language=='french':
        cur.execute('SELECT * FROM french_words ORDER BY RANDOM() LIMIT 1')
    elif language=='german':
        cur.execute('SELECT * FROM german_words ORDER BY RANDOM() LIMIT 1')
    #make it default to English so nothing strange happens
    else:
        cur.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')
    
    word, definition = cur.fetchone()
    cur.close()
    return (word, definition)

def insert_score(userid, language, score):
    cur = g.database.cursor()
    cur.execute('INSERT INTO scores (userid, language, score) VALUES(%s,%s,%s)',(userid,language,score))
    cur.close()

def get_highscore(userid):
    cur = g.database.cursor()
    cur.execute('SELECT MAX(score) FROM scores WHERE userid = %s', [userid])
    highscore = cur.fetchone()
    cur.close()
    return highscore[0]

def get_top(x):
    cur = g.database.cursor()
    cur.execute('SELECT users.username, SUM(scores.score) FROM scores, users GROUP BY users.username LIMIT %s', [x])
    topx = [dict(username=row[0], score=row[1]) for row in cur.fetchall()]
    cur.close()
    return topx

# http://toolserver.org/~enwikt/definitions/ wikitionary definition dump