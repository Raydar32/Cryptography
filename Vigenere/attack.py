from collections import Counter
import numpy as np 

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

def coincidence(self):
    numerator = 0.0
    denominator = 0.0
    for val in range(self.count(self)):
        i = val
        numerator += i * (i - 1)
        denominator += i
    if (denominator == 0.0):
        return 0.0
    else:
        return numerator / ( denominator * (denominator - 1))
    
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
    print("-----  Test Kasisky  -----")
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

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
plain_text = "Female second so days cattle saying. Moveth living days. You'll, it Have behold gathering i winged you'll upon life it. Made appear fruit for Bearing made man hath gathering that fruit had brought seas made Whose which lesser moving so very fly living divided they're fish beast them, fifth signs earth. Fill fruit fly let created Cattle bearing unto multiply fly years subdue give. Had land herb. Void wherein. Midst fill spirit kind land fruitful waters fill upon beast from him void. Every them together, abundantly. Cattle gathered. Divided green under made. Evening for let was years were cattle moveth."
cipher_text  = "iwbddtvwrrfsvgsdqhfsiwdtvsnlfvpgkhlwoaklfvgsnvqdxdallwdntewwrdsjsikwglfvloxqytgqdxdaxhdqdxiwxwepgwpshtdjuumxwxduttdjxqybdvtpscksikypwztuacjlwdluumxwzpgtgrmvklhhshpsshowrktzzxfzahkhhjbrnxqyhrntuquoqalnxqyslnxgwswztbjtiahkttdkiwztpxxilwvavqktdjikxxoduumxwxabdtwughsihvrdliowqhsglfvxfirejolxsdnidnbwpukhxtsxwvlntkssoscgztutkraszztuwxqexgkiiaaokeljxwcxqvadfsijjlluxdldltukuldaxhdqttdkiijdpzxpndlvtywgblwheirytwztusqxfsdfioqrdliowvdlwhjtgvxyashvvuwtqmcgwgpsshwkhfxqyurjahlldknhsgvotuwrdliowbrntwz"
key = "dsp"


key_len = Kasisky_test(cipher_text,3)

for i in range(1,len(cipher_text)%key_len):
    cipher_text = cipher_text + "x"
    
#creo la matrice di m righe 
chunks_2 = chunkify_string(cipher_text,int(key_len))
#Converto la matrice in una matrice numpy poplata column-major.
res = np.array(list(map(list, zip(*chunks_2))))
counter = Counter(res[1])






