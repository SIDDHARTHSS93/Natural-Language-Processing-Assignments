import nltk
import operator
def max_10(lines_display,file_dis):
    file_dis.write('First 10 most similar pairs\nword1\tword2\tsimilarity\n') 
    l = []
    
    #Splitting lines into words and adding it to a list
    for line in lines_display:
        words = line.split ()
        if(str(words[2]) != 'None'):
            
            l.append(words)
    
    
    l.remove(l[0])

    similarity_list = []
    for ls in range(len(l)):
        similarity_list.append(l[ls][2])

    #Calculating maximum 10 pairs from original-pairs
    for m in range(10):

        #Calculating index 
        index = similarity_list.index(max(similarity_list))
        file_dis.write(l[index][0])
        file_dis.write('\t')
        file_dis.write(l[index][1])
        file_dis.write('\t')
        file_dis.write(l[index][2])
        file_dis.write('\n')
        l.remove(l[index])
        similarity_list.remove(similarity_list[index])
    
#Calculating top 10 pairs
file_dis = open('top.txt','w')
with open('original-pairs.txt') as f1:
    lines_read = f1.readlines()
max_10(lines_read,file_dis)
file_dis.close()
f1.close()
