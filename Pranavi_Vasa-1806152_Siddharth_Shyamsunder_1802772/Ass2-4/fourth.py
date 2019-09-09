import nltk
from nltk.corpus import wordnet as wn

def word_similarity(lines):
    for line in lines:
        words = line.split()
        #Calculating synsets of word1 and word2
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
            
            for x in range(len(synsets_word1)):
                for y in range(len(synsets_word2)):
                    #Checking similarity between each of synsets of word1 and word2 and calculating maximum similarity pair
                    similarity = synsets_word1[x].path_similarity(synsets_word2[y])
                    
                    if(str(similarity) != 'None'):
                        if(similarity > maximum):
                            maximum = similarity
            if(maximum == 0):
                file.write('None')
            else:
                file.write(str(maximum))
            
        else:
            file.write('WordNetSimilarity')
        file.write('\n')

#Writing into a file 
file = open('BioSim-100-predicted.txt','w') 
with open('SimLex999-100.txt') as f:
    lines = f.readlines()
word_similarity(lines)
file.close()
f.close()



