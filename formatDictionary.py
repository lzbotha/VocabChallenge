
def normalchars(s):
    for c in s:
        if not 97 <= ord(c) <= 122 and c!=' ':
            return False
    return True

f = open('TEMP-E20131101.tsv','r')
outpt = open('dictionary.tsv','w')
wordcount = 0
prevword = ''
for line in f:
    dictitem = line.split('\t')
    #if the entry starts with a letter
    if (97 <= ord(dictitem[1][0]) <= 122):
        # eliminate all weird things like prefixes, suffixes, acronyms etc
        if dictitem[2][0:2]!='{{' and dictitem[2]!='Prefix' and dictitem[2]!='Letter' and dictitem[2]!='Proper noun' and dictitem[2]!='Symbol' and dictitem[2]!='Abbreviation' and dictitem[2]!='Initialism' and dictitem[2]!='Preposition':
            # filter out vulgar words and other things
            if not 'vulgar' in dictitem[3] and not 'initialism' in dictitem[3] and not 'idiomatic' in dictitem[3] and not 'abbreviation' in dictitem[3]:
                # remove duplicates... this is maybe not a good call
                if prevword != dictitem[1]:
                    # check that words only contain characters a-z
                    if normalchars(dictitem[1]):
                        outpt.write(line)
                        prevword = dictitem[1]
                        wordcount+=1
f.close()
print wordcount