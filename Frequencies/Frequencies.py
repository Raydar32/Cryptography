import pandas
from collections import Counter
import numpy as np
import string 

def split(string, length):
   return(string[i:i+length] for i in range (0,len(string),length))

def countOccurrencies(letter):
    return Counter(letter)

def empiric_distr(text, m):
    t=list(split(text, m))
    occurrencies=countOccurrencies(t)
    result={}
    for elem in occurrencies:
        result[elem]=occurrencies[elem]/len(t)
    return result

def plot_letter_frequencies(text):
    letter_counts = Counter(bulk_text)
    letter_counts = dict(sorted(letter_counts.items()))
    for key in letter_counts:
        letter_counts[key] /= len(bulk_text)
    df = pandas.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar',color="green")
    
#dato un testo in input lo porta in minuscolo e toglie i segni di punteggiatura
def preprocess_input(text_source):
    text_source = text_source.lower()    
    text_source = text_source.replace(" ","")    
    text_source = text_source.translate(str.maketrans('', '', string.punctuation))
    return ''.join(text_source)


def entropy(text,m):    
    labels=list(split(bulk_text, int(m)))   
    prob_dict = {x:labels.count(x)/len(labels) for x in labels}
    probs = np.array(list(prob_dict.values()))
    return - probs.dot(np.log2(probs))

def coincidence_index(text, m):
    t=list(split(text, m))
    ngrams=countOccurrencies(t)
    temp=0
    for item in ngrams:
        temp = temp +(ngrams[item]*(ngrams[item]-1))/(len(t)*((len(t)-1)))   
    return temp


bulk_text = preprocess_input(open('text.txt', 'r').read())
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plot_letter_frequencies(bulk_text)

#Stampa delle distribuzioni empiriche
m = input("Inserire m > ")
data = empiric_distr(bulk_text,int(m))
data = dict(sorted(data.items(), key=lambda item: item[1]))
many = input("Inserire num. top n-grammi da visualizz. > ")
data = dict(Counter(data).most_common(int(many)))
df = pandas.DataFrame.from_dict(data, orient='index')
df.plot(kind='bar',color="green")

#Calcolo entropia
print("Calcolo entropia")
print(entropy(bulk_text,m))


#Calcolo l'ic
print(coincidence_index(bulk_text,int(m)))
