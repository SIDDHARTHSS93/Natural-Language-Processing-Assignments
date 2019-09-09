import nltk
from nltk.corpus import wordnet as wn

def hypernyms(lines,file):
    file.write('word1\tword2\tSimilarity1\thyp1\thyp2\tSimilarity2\n')
    for line in lines:
        words = line.split()
        #Calculating synsets of word1 word2
        synsets_word1 = wn.synsets(words[0])
        synsets_word2 = wn.synsets(words[1])
        file.write(words[0])
        file.write('\t')
        file.write(words[1])
        file.write('\t')
        file.write(words[2])
        file.write('\t')
        maximum=0
        if (len(synsets_word1) != 0) and (len(synsets_word2) != 0):
            p = ''
            q = ''
            similarity = 0
            for x in range(len(synsets_word1)):
                for y in range(len(synsets_word2)):
                    
                    #Calculating hypernyms for word1 and word2
                    hypernyms1 = synsets_word1[x].hypernyms()
                    hypernyms2 = synsets_word2[y].hypernyms()
                    if ((len(hypernyms1) != 0) and (len(hypernyms2) != 0)):
                        for l in range(len(hypernyms1)):
                            for m in range(len(hypernyms2)):
                                
                                #Calculating similarity between each hypernym and selecting highest similarity pair hypernym
                                similarity = hypernyms1[l].path_similarity(hypernyms2[m])
                                if(str(similarity) != 'None'):
                                    if(similarity > maximum):
                                        maximum = similarity
                                        p = str(hypernyms1[l])
                                        q = str(hypernyms2[m])

            #Writing into file 
            if(p != '' and q != ''):
                word1 = (str(p)[8:])[:-7]
                word2 = (str(q)[8:])[:-7]
                file.write(word1)
                file.write('\t')
                file.write(word2)
                file.write('\t')
                if(similarity != 0):
                    file.write(str(similarity))
                else:
                    file.write('None')
            elif(p == '' and q == ''):
                file.write('No hypernyms for word1 and word2')
            elif(p == ''):
                file.write('No hypernym for word 1')
            else:
                file.write('No hypernym for word 2')
                
            
            file.write('\n')
        elif(len(synsets_word1) == 0 and len(synsets_word2) == 0):
            file.write('No synsets for word1 and word2')
            file.write('\n')
        elif(len(synsets_word1) == 0):
            file.write('No synonyms for first word')
            file.write('\n')
        else:
            file.write('No synonyms for secound word')
            file.write('\n')
            
        
#Reading file data
with open('original-pairs.txt') as f:
    lines = f.readlines()
file = open('original-pair-hypernyms.txt','w')
hypernyms(lines,file)

file.close()
f.close()


