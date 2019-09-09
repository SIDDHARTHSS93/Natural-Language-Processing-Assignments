"""
Three18812.py
Some simple arithmetic
created by sands 5/10/10
modified by ss18812 18/10/18
"""

import nltk
import numpy
import re
import warnings
warnings.filterwarnings("ignore",category=RuntimeWarning)
i=0
word=""
unigram=[]

#Get the contents of the sentence from the training data file and store in variable contents
myfile = open("sampletest.txt","r")
cont=myfile.read()
word=""
contents=cont.split()
while i<len(contents):
    #For the Unigram file, we need to have the <s> and </s> removed hence store the sentence without <s> and </s> in a variable Unigram
    if contents[i]!="<s>" and contents[i]!="</s>":
        unigram.append(contents[i])
    i+=1
count=0
#The variable unigramlength will store the count of words in the 3 sentences excluding <s> and< /s>, used in computing ungram
unigramlength=len(unigram)
print(unigramlength)
#We will store the values of our vocabulary file in a variable vocabcontents
myfile_vocab = open("sampledata.vocab.txt","r")
vocab=myfile_vocab.read()
vocabcontents=vocab.split()
vocabcontents.append("UNK")
for i in range (len(unigram)):
    word=unigram[i]
    #We use an if condition to check if our unigram sentence has words outside vocabcontents, if so we will replace those words with 'UNK'
    if word not in vocabcontents:
        unigram[i]="UNK"
        #Also temporarily store the value of UNK to our vocabcontents
        if "UNK" not in vocabcontents:
            vocabcontents.append("UNK")
#We will use 3 arrays, a word countarray that sees number of occurences words(taken from vocab list) in our training data. 
wordcountarray=numpy.zeros(len(vocabcontents))
#upu stands for unsmoothened probability for unigrams
#spu stands for smoothened probability for unigrams
upu=numpy.zeros(len(wordcountarray))
spu=numpy.zeros(len(wordcountarray))
for i in range(len(unigram)):
    for j in range(len(vocabcontents)):
        if(unigram[i]==vocabcontents[j]):
            wordcountarray[j]+=1
print(wordcountarray)
#BeforeSmoothening we have upu as the number of occurences of words(wordcountarray)/total length of words without <s> and </s>(unigramlength)
#After Smoothening we have spu as the (number of occurences of words(wordcountarray)+1)/(total length of words without <s> and </s>(unigramlength)+length of vocabulary

for i in range(len(wordcountarray)):
    upu[i]=wordcountarray[i]/unigramlength
    spu[i]=(wordcountarray[i]+1)/(unigramlength+len(vocabcontents))
print(len(vocabcontents))
print("Before Smooothening we have list:")
print("X\tP(X)")
for i in range(len(upu)):
    print(vocabcontents[i],"\t",round(upu[i],3))

print("After Smoothening, we have list:")
print("X\tP(X)")
for i in range(len(spu)):
    print(vocabcontents[i],"\t",round(spu[i],3))
bicontents=vocab.split()
#For the Bigram Model

for i in range(len(contents)):
    word=contents[i]
    #Adding UNK to vocabulary, and replacing words not found in vocab as 'UNK'
    if (word!='<s>' and word!="</s>") and word not in bicontents:
        contents[i]="UNK"
        if "UNK" not in bicontents:
            bicontents.append("UNK")
    #for Bigrams we will include<s> and</s> into our vocabulary, hence vocab count will be added by 2as well as we consider these 2 parameters as part of sentence
    if (word=='<s>' or word=="</s>"):
    
            if word =="<s>" and word not in bicontents:
                bicontents.insert(0,word)
            if word =="</s>" and word not in bicontents:
                bicontents.append(word)
#Use python nltk.bigrams to obtain a list of Bigrams from our sentences and store in variable bigramslist
bigramslist=list(nltk.bigrams(contents))
print(bigramslist)
#Bigrammatrix holds value of counts of words such that previous word isknown 
bigrammatrix=numpy.zeros(shape=(len(bicontents),len(bicontents)))
for i in range(len(bicontents)):
    for j in range(len(bicontents)):
       for k in range(len(bigramslist)):
            if bigramslist[k][0]==bicontents[i] and bigramslist[k][1]==bicontents[j]:
                bigrammatrix[i][j]+=1

#Variable probpo holds probability of previously occuring word
probpo=numpy.zeros(len(bicontents))
for i in range(len(contents)):
    for j in range(len(bicontents)):
        if contents[i]==bicontents[j]:
            probpo[j]+=1
print(probpo)
print("\n\n\nBefore Smoothing, we have list:")
# Bigram Probability before smoothening(upb) is the number of occurences of a future word such that previous word in known dvided by number of previous word known
#Here we have Rows holding previous word and columns holding future words
upb=numpy.zeros(shape=(len(bicontents),len(bicontents)))
for i in range(len(bicontents)):
    print("   ",bicontents[i],"| ",end="  ")
print("\n_______________________________________________________________________________________________")
for i in range(len(bicontents)):
    for j in range(len(bicontents)):
        upb[i][j]=(bigrammatrix[i][j])/probpo[i]
        if(j==0):
            print("\n",bicontents[i],"|",end=" ")

        print(round(upb[i][j],3),"|  ",end="  ")
# Bigram Probability after smoothening(spb) is (the number of occurences of a future word such that previous word in known +1) dvided by (number of previous word known+ square of vocabularycount)
#Here we have Rows holding previous word and columns holding future words

spb=numpy.zeros(shape=(len(bicontents),len(bicontents)))
print("\n\n\nAfter Smoothing we have list:")
for i in range(len(bicontents)):

    print("   ",bicontents[i],"  ",end="  ")
print("\n_______________________________________________________________________________________________ ")
for i in range(len(bicontents)):
    for j in range(len(bicontents)):
        spb[i][j]=(bigrammatrix[i][j]+1)/(probpo[i]+(len(bicontents)**2))
        if j==0:
            print("\n",bicontents[i],"|  ",end=" ")
        print(round(spb[i][j],3),"  ",end="  ")
myfile.close()
prob=1
word2=''
#Sentence probability is a form where we are going to read each sentence and find the probsbility of words or in case of bigrams, one word and its previous word
myfile = open("sampletest.txt","r")
count=0
for line in myfile:
    count+=1
#Unigram probability will be the product of probability of all values in the given sentence. In each of these probabilities, the total count of words will be compared with that of all words in the content
sentuni=numpy.zeros(count)
sentbi=numpy.zeros(count)
print('\n\n')
myfile = open("sampletest.txt","r")
count=0
for line in myfile:
    content=line.split()

    for i in range(len(content)):
        word2=content[i]
        if word2 not in vocabcontents:
          content[i]='UNK'

    for i in range(len(content)):
        for j in range(len(vocabcontents)):
            if content[i]==vocabcontents[j]:
                prob=prob*spu[j]
    sentuni[count]=round(prob,5)
    prob=1
    count+=1
myfile.close()
myfile = open("sampletest.txt","r")
prob2=1
count=0
for line in myfile:
    content=line.split()
    #bigram probability will be the product of probability of all pairs of previous and new words in the given sentence. In each of these probabilities, the total count of pairs will be compared with that of all words in the content

    for i in range(len(content)):
        word2=content[i]
        if word2 not in bicontents:
          content[i]='UNK'
    bigram=list(nltk.bigrams(content))
    for i in range(len(bicontents)):
        for j in range(len(bicontents)):
           for k in range(len(bigram)):
            if bigram[k][0]==bicontents[i] and bigram[k][1]==bicontents[j]:
                prob2=prob*spb[i][j]
    sentbi[count]=round(prob2,5)
    prob2=1
    count+=1
myfile.close()
print("\n\nSentence Probability of Unigram and Bigram are ")
myfile = open("sampletest.txt","r")
count=0
print("Sentences\tUnigram\tBigram")
for line in myfile:
        print(line,"\t",sentuni[count],"\t",sentbi[count])
        count+=1
    
myfile.close()
myfile_vocab.close()

