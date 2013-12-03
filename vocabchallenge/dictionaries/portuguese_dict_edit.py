
f = open('portuguese_dictionary.tsv','r')
outpt = open('portuguese_dictionary_v1.tsv','w')

def remove_formatting(text):
    temp = ''
    for c in text:
        if not c =='[' and not c==']' and not c =='#':
            temp = temp + c
    return temp

# as it stands now this seperates all words with a direct translation
for line in f:
    dictitem = line.split('\t')
    if 65 <= ord(dictitem[1][0]) <= 90 or 97 <= ord(dictitem[1][0]) <= 122:
        if dictitem[2]!='Suffix' and dictitem[2]!='Prefix' and dictitem[2]!='Proper noun' and dictitem[2]!='Symbol' and dictitem[2]!='Proverb' and dictitem[2]!='Abbreviation'  and dictitem[2]!='Initialism':
            if not 'initialism' in dictitem[-1] and not 'Arabic spelling' in dictitem[-1] and 'initialism' not in line and 'abbreviation' not in line and 'acronym' not in line and 'shit' not in line and 'fuck' not in line and 'cunt' not in line:
                if '[[' in dictitem[-1] and not '{{' in dictitem[-1] and not '[[#English' in dictitem[-1]:
                    if len(dictitem[-1].split(' ')) == 2:
                        if not '|' in dictitem[-1].split(' ')[1]:
                            outpt.write(dictitem[1]+'\t'+remove_formatting(dictitem[-1]))
                    else:
                        outpt.write(dictitem[1]+'\t'+remove_formatting(dictitem[-1]))
f.close()