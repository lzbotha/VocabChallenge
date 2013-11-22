import psycopg2



database = psycopg2.connect('dbname=vocabchallenge user=bzl')
f1 = open('english_dictionary_v1.tsv','r')
f2 = open('afrikaans_dictionary_v1.tsv','r')
f3 = open('german_dictionary_v1.tsv','r')
f4 = open('french_dictionary_v1.tsv','r')
cur = database.cursor()
for line in f1:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO english_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

for line in f2:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO afrikaans_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

for line in f3:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO german_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

for line in f4:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO french_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))

cur.close()

database.commit()
database.close()