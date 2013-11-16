
f = open('TEMP-E20131101.tsv','r')
for line in f:
    dictitem = line.split('\t')[3]
    if (65 <= ord(line[8:-1][0]) <= 90) or (97 <= ord(line[8:-1][0]) <= 122):
        print dictitem
f.close()