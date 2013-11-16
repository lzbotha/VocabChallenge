
f = open('TEMP-E20131101.tsv','r')
for line in f:
    if (65 <= ord(line[8:-1][0]) <= 90) or (97 <= ord(line[8:-1][0]) <= 122):
        print line[8:-1]
f.close()