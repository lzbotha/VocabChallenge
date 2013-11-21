import psycopg2



database = psycopg2.connect('dbname=vocabchallenge user=bzl')
f = open('english_dictionary_v1.tsv','r')
cur = database.cursor()
for line in f:
    dictitem = line.split('\t')
    cur.execute('INSERT INTO english_words (word,definition) VALUES(%s,%s)',(dictitem[0],dictitem[1]))
cur.close()

database.commit()
database.close()