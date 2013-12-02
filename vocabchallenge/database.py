import psycopg2
from flask import g, request, session
from vocabchallenge import app

def connect_db():
    database = psycopg2.connect('host=%s password=%s dbname=%s user=%s' % (app.config['DATABASE_HOST'], app.config['DATABASE_PASSWORD'], app.config['DATABASE_NAME'], app.config['DATABASE_USER']))
    return database

def disconnect_db():
    g.database.commit()
    g.database.close()

def set_user(mxit_id):
    try:
        c = g.database.cursor()
        c.execute('SELECT id, username FROM users WHERE mxit_id = %s LIMIT 1', (str(mxit_id), ))
        #if there are no values in query fetchone returns None, which is a type mismatch as a tuple is expected
        session['userid'], session['username'] = c.fetchone()
    except TypeError:
        return False
    finally:
        c.close()
    return True


def create_user():
    g.database.rollback()
    try:
        mxit_id = request.headers['X-Mxit-Userid-R']
        mxit_nick = request.headers['X-Mxit-Nick']
    except KeyError:
        mxit_id = -1  # development id
        mxit_nick = 'roflpop'
    haveUser = set_user(mxit_id)
    if not haveUser:
        try:
            c = g.database.cursor()
            c.execute('SELECT max(id)+1 FROM users')
            userid = c.fetchone()[0]
            if not userid:
                userid = 0
            c.execute('INSERT INTO users (id, mxit_id, username, joined) VALUES (%s, %s, %s, NOW())', (userid, mxit_id, mxit_nick))
            session['userid'] = userid
            session['username'] = mxit_nick
            g.database.commit()
        finally:
            c.close()

    g.database.commit()

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
        cur.execute('SELECT word, definition FROM english_words ORDER BY RANDOM() LIMIT 1')
    elif language=='afrikaans':
        cur.execute('SELECT word, definition FROM afrikaans_words ORDER BY RANDOM() LIMIT 1')
    elif language=='french':
        cur.execute('SELECT word, definition FROM french_words ORDER BY RANDOM() LIMIT 1')
    elif language=='german':
        cur.execute('SELECT word, definition FROM german_words ORDER BY RANDOM() LIMIT 1')
    #make it default to English so nothing strange happens
    else:
        cur.execute('SELECT word, definition FROM english_words ORDER BY RANDOM() LIMIT 1')
    
    word, definition = cur.fetchone()
    word, definition = word.decode('utf-8'), definition.decode('utf-8')
    cur.close()
    return (word, definition)

def get_padding_words(language, word, num):
    cur = g.database.cursor()
    if language=='english':
        cur.execute('SELECT word FROM english_words WHERE word!=%s ORDER BY RANDOM() LIMIT %s', [word,num])
    elif language=='afrikaans':
        cur.execute('SELECT word FROM afrikaans_words WHERE word!=%s ORDER BY RANDOM() LIMIT %s', [word,num])
    elif language=='french':
        cur.execute('SELECT word FROM french_words WHERE word!=%s ORDER BY RANDOM() LIMIT %s', [word,num])
    elif language=='german':
        cur.execute('SELECT word FROM german_words WHERE word!=%s ORDER BY RANDOM() LIMIT %s', [word,num])
    #make it default to English so nothing strange happens
    else:
        cur.execute('SELECT word FROM english_words WHERE word!=%s ORDER BY RANDOM() LIMIT %s', [word,num])

    words = [row[0].decode('utf-8') for row in cur.fetchall()]
    cur.close()
    return words

def get_userid(username):
    cur = g.database.cursor()
    cur.execute('SELECT id FROM users WHERE username=%s LIMIT 1', [username])
    userid = cur.fetchone()[0]
    cur.close()
    return userid

def get_num_games(userid):
    cur = g.database.cursor()
    cur.execute('SELECT COUNT(*) FROM scores WHERE userid=%s', [userid])
    games = cur.fetchone()[0]
    cur.close()
    return games

def get_breakdown(userid):
    cur = g.database.cursor()
    cur.execute('SELECT language, MAX(score) AS highscore, count(*) as games_played FROM scores WHERE userid=%s GROUP BY language', [userid])
    breakdown = [dict(language=row[0].capitalize(), highscore=row[1], games_played=row[2]) for row in cur.fetchall()]
    cur.close()
    return breakdown

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
    cur.execute('SELECT users.username, MAX(scores.score) AS highscore FROM scores, users WHERE users.id=scores.userid GROUP BY users.username ORDER BY highscore DESC LIMIT %s', [x])
    topx = [dict(username=row[0], score=row[1] for row in cur.fetchall()]
    cur.close()
    return topx

def get_top(x,language):
    cur = g.database.cursor()
    cur.execute('SELECT users.username, MAX(scores.score) AS highscore FROM scores, users WHERE users.id=scores.userid AND scores.language=%s GROUP BY users.username ORDER BY highscore DESC LIMIT %s', (language,x))
    topx = [dict(username=row[0], score=row[1] for row in cur.fetchall()]
    cur.close()
    return topx

# http://toolserver.org/~enwikt/definitions/ wikitionary definition dump