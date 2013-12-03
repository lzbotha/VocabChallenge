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
f5 = open('vocabchallenge/dictionaries/spanish_dictionary_v1.tsv','r')
f6 = open('vocabchallenge/dictionaries/italian_dictionary_v1.tsv','r')
f7 = open('vocabchallenge/dictionaries/portuguese_dictionary_v1.tsv','r')
cur = database.cursor()

print 'inserting words into english_words'
for line in f1:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO english_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f1.close()

print 'inserting words into afrikaans_words'
for line in f2:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO afrikaans_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f2.close()

print 'inserting words into german_words'
for line in f3:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO german_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f3.close()

print 'inserting words into french_words'
for line in f4:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO french_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f4.close()

print 'inserting words into spanish_words'
for line in f5:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO spanish_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f5.close()

print 'inserting words into italian_words'
for line in f6:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO italian_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f6.close()

print 'inserting words into portuguese_words'
for line in f7:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO portuguese_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
f7.close()

cur.close()

database.commit()
database.close()