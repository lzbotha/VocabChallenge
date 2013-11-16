import psycopg2



database = psycopg2.connect('dbname=vocabchallenge user=bzl')
f = open('dictionary.tsv','r')
cur = database.cursor()
for line in f:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO words (word,definition) VALUES(%s,%s)',(dictitem[1],dictitem[3]))
cur.close()

database.commit()
database.close()