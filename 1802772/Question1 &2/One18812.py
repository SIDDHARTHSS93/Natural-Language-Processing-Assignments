import urllib
from urllib import request
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer
import nltk
from nltk import word_tokenize,re,pos_tag
#In order to take the content from the website provided, we will use import urllib
url="https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison"
#Response is the variable used to open the file
response=request.urlopen(url)
#variable rw stores the converted html format of the file
rw=response.read().decode('utf8')
#We will use BeautifulSoup to extract data from the htnk document
#we will store Beautiful soup into a variable s this variable will search for display elements in the html like h1,paragraph p and so on and give the required information into a
#variable rel.

s=BeautifulSoup(rw,'html.parser')
rel=""
for relevance in s.find_all('h1'):
    rel+=(relevance.text)
for relevance in s.find_all('p'):
    rel+=(relevance.text)
for relevance in s.find_all('h2'):
    rel+=(relevance.text)

#rel_tokens_nopunct willtraverse through rel and remove all punctuation marks and divide the text into tokens
#Using set on our rel_tokens_nopunct function we will get the unique types from the tokens
rel_tokens_nopunct = [word for word in word_tokenize(rel)
if re.search("\w", word)]
print("The length of tokens from the url before Lemmatization are:",len(rel_tokens_nopunct))
print("\n\nThe length of types from the url before Lemmatization are:",len(set(rel_tokens_nopunct)))
print("\n\nThe tokens contained in the website:"+url+" before Lemmatization are:\n\n")
print(rel_tokens_nopunct)
print("\n\nThe types contained in the website:"+url+" before Lemmatization are:\n\n")
print(set(rel_tokens_nopunct))

#We will use the Lemmatizer function to Lemmatize the words and store the lemmatized values for each of the values in l1,l2,l3
lem=WordNetLemmatizer()
l=[lem.lemmatize(i,pos='v') for i in rel_tokens_nopunct]
l2=[lem.lemmatize(i,pos='n') for i in l]
l3=[lem.lemmatize(i,pos='a') for i in l2]
print("\n\nThe length of tokens from the url After Lemmatization are:",len(l3))
print("\n\nThe length of types from the url After Lemmatization are:",len(set(l3)))
print("\n\n The types contained in the website:"+url+" after Lemmatization is:\n\n")
print(set(l3))
print("\n\n The tokens contained in the website:"+url+" after Lemmatization is:\n\n")
print(l3)
#We will use the pos_tag function to divide the tokens into pairs of sentences and its tags
print("\n\n After Parts of Speech Tagging we have text:")
print(" Text\t   POS")
post=nltk.pos_tag(l3)

for i in range(len(post)):
    if post[i]==')':
        print("\n")
    print(post[i])





