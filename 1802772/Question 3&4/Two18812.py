import urllib
from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize,re,pos_tag
import nltk
from nltk import re

#We ask User to input whether he wants to input text or URL.
choose=input("Please let us know, if you want to search phone numbers from text or URL?")
if choose=='text':
    #If choice =text we input text from user, and store the Regular Expression pattern in reg

    text=input("Please Enter a text:")
    reg='(((^)|(\s))((\+\d{2}\s\d{2}\s{0,1}\d{8})|([1-9]\d{3}\s\d{6})|((0)((0\d{2}\s\d{2}\s{0,1}\d{8})|([1-9]\d{3}\s{0,1}\d{6})|(\d{2}\s\d{2}\s{0,1}\d{8})))))'
    
    phone=re.findall(reg,text)
    print(text)
    instate='q0'
    if not phone:
            print("Sorry No MatchesFound")
    else:
        for i in range(len(phone)):
            print("Match Found:",phone[i][0],"at:",i)
    
   
#Getting PhoneNumbers from URL:
#If user wishes to enter URL, we ask user to enter URL  

elif choose=="URL":
    url=input("Please Enter the URL in full standard format:")
    #We use urlopen to open that URL, and we decode and store the URL value in rw in html format
    response=request.urlopen(url)
    rw=response.read().decode('utf8')
    #We import Beautiful Soup to extract Meaningful Data from the pattern.
    s=BeautifulSoup(rw,'html.parser')
    rel=""
    for relevance in s.find_all('h1'):
        rel+=(relevance.text)
    for relevance in s.find_all('p'):
        rel+=(relevance.text)
    for relevance in s.find_all('h2'):
        rel+=(relevance.text)
    reg='(((^)|(\s))((\+\d{2}\s((\d{2}\s\d{8})|(\d{10})))|([1-9]\d{3}\s\d{6})|((0)((0\d{2}\s((\d{2}\s\d{8})|(\d{10})))|(\d{10})|(\d{4}\s\d{6})|(\d{2}\s((\d{2}\s\d{8})|(\d{10)))))))'
    #phone traverses the text and finds if a pattern matching reg is found, if so, it displays the text following the pattern
    phone=re.findall(reg,rel)
    if not phone:
        print("Sorry No MatchesFound")
    else:
        for i in range(len(phone)):
            print("Match Found:",phone[i][0],"at:",i)



