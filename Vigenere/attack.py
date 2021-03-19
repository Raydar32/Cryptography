from collections import Counter
import numpy as np 
import collections
import string


def find_all_indexes(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1

def countOccurrencies(letter):
    return Counter(letter)

def preprocess_word(word):    
    word = word.lower()    
    word = word.replace(" ","")    
    word = word.translate(str.maketrans('', '', string.punctuation))
    return ''.join(word)

    
def list_GCD(my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result 
    
def chunkify_string(string,blocksize):
    chunks = [string[i:i+blocksize] for i in range(0, len(string), blocksize)]
    return chunks

def Kasisky_test(cipher_text,ngram_size): 
    print("--------  Test Kasisky  --------")
    chunks = chunkify_string(cipher_text,ngram_size)
    top_recurrent = countOccurrencies(chunks).most_common(1)[0][0]
    indexes = find_all_indexes(cipher_text,top_recurrent)
    indexes[:] = [n - indexes[0] for n in indexes][1:]
    indexes_gcd = list_GCD(indexes)
    print("Distanze delle occorrenze del ",ngram_size,"-grammo: ",top_recurrent," : " , indexes)
    print("Lunghezza chiave ipotizzata: ", indexes_gcd)
    return indexes_gcd

def string_to_matrix(str_in):
    nums = str_in.split()
    n = int(len(nums) ** 0.5)
    return list(map(list, zip(*[map(int, nums)] * n)))


def generate_cipher_matrix(cipher_text,estimated_key_len):
    #padding della stringa
    for i in range(0,estimated_key_len-(len(cipher_text)%key_len)):
        cipher_text = cipher_text + "x"    
    #creo la matrice di m righe 
    chunks = chunkify_string(cipher_text,int(key_len))   
    #Converto la matrice in una matrice numpy poplata column-major.
    res = list(map(list, zip(*chunks))) 
    return res


def coincidence_index(text):
    t=text
    ngrams=countOccurrencies(t)
    temp=0
    for item in ngrams:
        temp = temp +(ngrams[item]*(ngrams[item]-1))/(len(t)*((len(t)-1)))   
    return temp


def decrypt_k_row(matrix,row):
    riga = res[row]
    #Si calcolano le frequenze dei caratteri di ogni riga 
    frequencies = [0]*26
    for idx,letter in enumerate(letters):
        if letter in riga:
            frequencies[idx] = Counter(riga)[letter]
    frequencies = np.array(frequencies)/len(riga)
    all_shifts = []
    #genero tutti gli shift
    for i in range(0,25):
        v = np.roll(frequencies,(-1)*i) #shifto di -1 a destra per shift a sx
        all_shifts.append(v)
    english_frequencies = np.array(list(englishLetterFreq.values()))
    #cerco lo shift che meglio approssima le frequenze inglesi+
    products = []
    for item in all_shifts:
        dot = np.dot(item,english_frequencies)
        products.append(dot)       
    max_value = max(products)
    max_index = products.index(max_value)    
    return letters[max_index]
        
                
    
englishLetterFreq = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07}
englishLetterFreq = collections.OrderedDict(sorted(englishLetterFreq.items()))
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


cipher_text =  "EIVDMAOHSVVUPXYSAYMNAAOMWOGKHKTECDYTDRIBRPLECHWJQLBELWTCGWIJTECXBTPIGTBTBACXVFIHIRBDOGGZXYHSEEFBNDMRGQOXRWIINSMHXNOVPBXQIXYDYTDHNAROWKWLLPWYXPMPSZUXKCPHFGNBNMQARYPREDSEBLXTXVRVPOMFPXKTYKELWBRTMTJEIIEIGEGLIEKVZRWVFGAAAETHUQAXYGFZFLTRRKVNPOXQNSLDYFEFJSEAWNPHICRSHUUMZVGDXWDYIQIGEIMFFQVPFNGRXFBTTXFRVMGQTMKENAEMZIGJJNRXHFZNUEEQSIGQMYCCDALXETKVCGZLMCMTDYTTXQGFVIFNTHNUNATAMWYNCLGDRFRMMIETPRKVZRWMJUGTGBVOEABAGCKTMFEEWUSOWBMFPXJZIKETTDNTBHDILVULBDXVHVVGBRHEUUMMRTKHVQVTQDYIOYHFVWBSWABMCXYQLXSGWFRCAHLISBQYIOGLCVPOBRDVKAGTKXBVRUMLCEEIMNXPXWDYGNHJASNQUVHHBVRTQGRXQVXYMTAMANNTEGKIKAAXTAMFZGMMCPGYANAEKSSRRGHSRSDBUGYDIHRIZBNEIUTCFBRBVRUPHSAHVDMTNWTCBMMWFXQZZNAEXGSLQCVYCXSQWHMXBVRUWEGEWZENGAMQCAVPTRHRFZMXNLMWGUZACISIUWYRHUOAQTWNAEPMFEIMECHNLFCPRZEXRIGOHUGXXMEPVFBXSHNHJCZXAGIRFYLWAMBLQCKCVSEQQHNMJSLQCBLPRPIURTAMMYNJXFPTGKQHNMBVRANKMBXZYYMOMQARHWKRWIZDIPNLBFNPOXPTEJAHLYXAPHVBAYIWRXFBAFVCJVPTRHECXNAAMLSSKVXQBIJAQAEGBVRAZXFPTGKNAERTZOGUX"
cipher_text = preprocess_word(cipher_text)
key = "dsp"


#Si trova la lunghezza della chiave usando Kasisky
key_len = Kasisky_test(cipher_text,2)

print("--- Decifratura della chiave ---")
#Si genera la matrice del cipher_text 
print("Generazione matrice del cipher_text")
res = generate_cipher_matrix(cipher_text,key_len)
#Si decifra la chiave:
key = []
for idx,row in enumerate(res):
    k = decrypt_k_row(res, idx)
    print("Riga ", idx, " k decifrato : ", k)
    key.append(k)
print("Chiave: ",''.join([str(elem) for elem in key]) )


    
#frequencies = np.asarray([*count.values()])/len(riga)

    

    

    
    



