import psycopg2
from vocabchallenge import config

db = psycopg2.connect('dbname=%s user=%s' % (config.DATABASE_NAME, config.DATABASE_USER))

c = db.cursor()

print 'dropping tables'

c.execute('drop table if exists users')
c.execute('drop table if exists scores')
c.execute('drop table if exists feedback')
c.execute('drop table if exists german_words')
c.execute('drop table if exists french_words')
c.execute('drop table if exists english_words')
c.execute('drop table if exists afrikaans_words')

c.close()
db.commit()
print 'Completed'
