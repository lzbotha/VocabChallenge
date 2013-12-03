import psycopg2

from vocabchallenge import config

db = psycopg2.connect('user=%s dbname=%s' % (config.DATABASE_USER, config.DATABASE_NAME))

c = db.cursor()

try:
    c.execute('create table users('
                'id SERIAL PRIMARY KEY,'
                'mxit_id VARCHAR(100) NOT NULL,'
                'username VARCHAR NOT NULL,'
                'joined DATE NOT NULL'
                ')')

    c.execute('create table scores('
                'id SERIAL PRIMARY KEY,'
                'userid INT NOT NULL,'
                'language VARCHAR NOT NULL,'
                'score INT NOT NULL'
                ')')

    c.execute('create table feedback('
                'id SERIAL PRIMARY KEY,'
                'datetime TIMESTAMP NOT NULL,'
                'userid INT NOT NULL,'
                'feedback TEXT'
                ');')

    c.execute('create table afrikaans_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    c.execute('create table english_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    c.execute('create table french_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    c.execute('create table german_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    c.execute('create table italian_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    c.execute('create table spanish_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    c.execute('create table portuguese_words('
                'id SERIAL PRIMARY KEY,'
                'word VARCHAR NOT NULL,'
                'definition TEXT NOT NULL'
                ')')

    db.commit()

except psycopg2.ProgrammingError, e:
    print 'You have already created databases. To update schema first clear databsae. We dont upgrade '
    print e
finally:
    c.close()
    db.close()
