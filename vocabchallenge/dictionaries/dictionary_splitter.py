
f = open('TEMP-S20131002.tsv','r')
outpt = open('shona_dictionary.tsv','w')

for line in f:
    dictitem = line.split('\t')
    if dictitem[0]=='Shona':
        outpt.write(line)
    
f.close()