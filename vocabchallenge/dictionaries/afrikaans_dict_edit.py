
f = open('afrikaans_dictionary.tsv','r')
outpt = open('afrikaans_dictionary_v1.tsv','w')

def remove_formatting(text):
    temp = ''
    for c in text:
        if not c =='[' and not c==']' and not c =='#':
            temp = temp + c
    return temp

# as it stands now this seperates all words with a direct translation
for line in f:
    dictitem = line.split('\t')
    if dictitem[2]!='Suffix' and dictitem[2]!='Prefix' and dictitem[2]!='Proper noun':
        if not 'initialism' in dictitem[-1] and not 'Arabic spelling' in dictitem[-1]:
            if '[[' in dictitem[-1] and not '{{' in dictitem[-1]:
                if len(dictitem[-1].split(' ')) == 2:
                    if not '|' in dictitem[-1].split(' ')[1]:
                        outpt.write(dictitem[1]+'\t'+remove_formatting(dictitem[-1]))
                else:
                    if not '|' in dictitem[-1]:
                        outpt.write(dictitem[1]+'\t'+remove_formatting(dictitem[-1]))
f.close()