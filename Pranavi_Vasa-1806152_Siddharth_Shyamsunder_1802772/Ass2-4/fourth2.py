import nltk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re

def word_similarity(words):
    file.write('word1\tword2\tSimilarity\n')
    for word in words:
        #Calculating synsets for word1
        synsets_word1 = wn.synsets(word)
        for word2 in words:
            if(word != word2):
                #Calculating synsets for word2
                synsets_word2 = wn.synsets(word2)
                file.write(word)
                file.write('\t')
                file.write(word2)
                file.write('\t')
                maximum=0
                if (len(synsets_word1) != 0) and (len(synsets_word2) != 0):
                    
                    for x in range(len(synsets_word1)):
                        for y in range(len(synsets_word2)):
                            #Calculating similarity between each hypernym and selecting highest similarity pair hypernym
                            similarity = synsets_word1[x].path_similarity(synsets_word2[y])
                            
                            if(str(similarity) != 'None'):
                                if(similarity > maximum):
                                    maximum = similarity
                if(maximum == 0):
                    file.write('None')
                else:
                    file.write(str(maximum))
                file.write('\n')
                
file1 = open('text1.txt', encoding = 'utf8')
sampledata = file1.read()
sampledata = sampledata.lower()

#Removing any alpha numeric words
def good_word(word):
    import string
    for c in word:
        if not c in string.ascii_letters:
            return False
    return True

def clean_string(input_str):
    return ' '.join([w for w in input_str.split() if good_word(w)])

cleaned = clean_string(sampledata)

#Tokenizing 
tokens = word_tokenize(cleaned)

#Removing punchuations
tokens_nopun = [word for word in tokens if re.search("\w",word)]

#Removing stop words
filtered_words = [word for word in tokens_nopun if word not in stopwords.words('english')]

#Lemmatization
lemmatiser = WordNetLemmatizer()
tokens_lemma = []
for word in filtered_words:
    tokens_lemma.append(lemmatiser.lemmatize(word))

#Removing duplicates
tokens_set = set(tokens_lemma)
file1.close()

#Writing in original-pairs file
file = open('original-pairs.txt','w')
word_similarity(tokens_set)
file.close()
