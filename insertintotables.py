import psycopg2
from vocabchallenge import config

print 'Connecting to database'
database = psycopg2.connect('dbname=%s user=%s'%(config.DATABASE_NAME, config.DATABASE_USER))
print 'Connected to database'
print 'Opening dictionary files'
f1 = open('vocabchallenge/dictionaries/english_dictionary_v1.tsv','r')
f2 = open('vocabchallenge/dictionaries/afrikaans_dictionary_v1.tsv','r')
f3 = open('vocabchallenge/dictionaries/german_dictionary_v1.tsv','r')
f4 = open('vocabchallenge/dictionaries/french_dictionary_v1.tsv','r')
cur = database.cursor()

print 'inserting words into english_words'
for line in f1:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO english_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

print 'inserting words into afrikaans_words'
for line in f2:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO afrikaans_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

print 'inserting words into german_words'
for line in f3:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO german_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

print 'inserting words into french_words'
for line in f4:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO french_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

cur.close()

database.commit()
database.close()