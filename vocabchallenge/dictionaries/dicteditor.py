
f = open('afrikaans_dictionary.tsv','r')
outpt = open('afrikaans_dictionary_v1.tsv','w')


# as it stands now this seperates all words with a direct translation
for line in f:
    dictitem = line.split('\t')
    if dictitem[2]!='Suffix' and dictitem[2]!='Prefix' and dictitem[2]!='Proper noun':
        if not 'initialism' in dictitem[-1] and not 'Arabic spelling' in dictitem[-1]:
            if '# [[' in dictitem[-1]:
                outpt.write(dictitem[1]+'\t'+dictitem[-1])
f.close()