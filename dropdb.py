import psycopg2
import sys

print 'Are you sure this is what you want to do? Say YES to confirm'
if raw_input() != 'YES':
    sys.exit()
db = psycopg2.connect('user=%s' % config.database_user)

c = db.cursor()

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
