#   '---------------------------------------------------------------------------------------
#   ' File      : main.cpp
#   ' Author    : Alessandro Mini (mat. 7060381)
#   ' Date      : 8/11/2020
#   ' Purpose   : Main class for both sequential and OpenMP versions of K-means.
#   '---------------------------------------------------------------------------------------

import numpy as np
from sympy import Matrix



#Si definisce l'alfabeto di riferimento, in questo caso quello inglese.
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#   '---------------------------------------------------------------------------------------
#   ' Metodo    : vector_modulus
#   ' Fine      : Calcolare il modulo di un vettore, prende in ingresso un vettore e ne esegue
#   '             v[i] = v[i] mod (|alfabeto|).
#   '---------------------------------------------------------------------------------------
def vector_modulus(vector,alphabet):
    for i in range(0,len(vector)):
        vector[i] = vector[i] % len(alphabet)   
        
#   '---------------------------------------------------------------------------------------
#   ' Metodo    : generate_alphabet_map
#   ' Fine      : Questo metodo mappa ogni lettera nel corrispettivo intero, a=0,b=1..z=26.
#   '---------------------------------------------------------------------------------------
def generate_alphabet_map(letters):       
    dizionario = {}
    for idx,letter in enumerate(letters):
        dizionario[letter] = idx
    return dizionario

#   '---------------------------------------------------------------------------------------
#   ' Metodo    : generate_inverse_alphabet_map
#   ' Fine      : Questo metodo genera la mapap inversa del metodo precedente, associa gli
#   '             interi al rispettivo carattere, 0=a, 1=b ... 26 = z.
#   '---------------------------------------------------------------------------------------
def generate_inverse_alphabet_map(letters):
    dizionario = {}
    for idx,letter in enumerate(letters):
        dizionario[letter] = idx    
    inv = {v: k for k, v in dizionario.items()}
    return inv

#   '---------------------------------------------------------------------------------------
#   ' Metodo    : word_to_vector
#   ' Fine      : Questo metodo prende in ingresso una stringa e una mappa e converte la stringa
#   '             in un array di caratteri sulla base della codifica della mappa.
#   '             Usando la mappa alfabeto->interi su "test" si ottiene [19,4,18,19].
#   '             Usando la mappa interi->alfabeto su [19,4,18,19] si ottiene "test".
#   '---------------------------------------------------------------------------------------
def word_to_vector(message,mapfunc):
    vectorized_word = []
    for word in message:
            vectorized_word.append(mapfunc[word])
    return vectorized_word

#   '---------------------------------------------------------------------------------------
#   ' Metodo    : get_inverse
#   ' Fine      : Questo metodo calcola la matrice inversa di una matrice quadrata M 
#   '             modulo |alfabeto|.
#   '---------------------------------------------------------------------------------------
def get_inverse(matrix, alphabet):
    alphabet_len = len(alphabet)    
    matrix = Matrix(matrix)
    return np.matrix(matrix.inv_mod(alphabet_len))


#   '---------------------------------------------------------------------------------------
#   ' Metodo    : encrypt_block
#   ' Fine      : Questo metodo del cifrario di Hill cifra un blocco del messaggio originale.
#   '             la grandezza del blocco è definita dalla variabile block_size, gli altri 
#   '             parametri del metodo sono il blocco stesso, l'alfabeto e la chiave di cifratura.
#   '---------------------------------------------------------------------------------------
def encrypt_block(block,block_size,letters,key):
    #Si genera la mappa dell'alfabeto e la mappa inversa
    alphabet_map = generate_alphabet_map(letters)                   
    alphabet_map_inverse = generate_inverse_alphabet_map(letters)   
    #Si vettorizza la chiave
    key = word_to_vector(key,alphabet_map)
    #Si fa il reshaping della chiave in forma di matrice per poter poi
    #eseguire il prodotto K * plaintext
    key_matrix = key_matrix = np.asarray(key).reshape(block_size,block_size)
    #Si vettorizza il messaggio originale
    message_vector = np.asarray(word_to_vector(block,alphabet_map)).T
    #Si esegue il prodotto tra la matrice della chiave ed il vettore messaggio trasposto
    #(Matrice per vettore colonna)
    i = np.dot(key_matrix,message_vector)
    #Come penultima istruzione si esegue il modulo del vettore
    vector_modulus(i,letters)
    #Si converte il vettore in stringa usando la mappa inversa
    translated = word_to_vector(i.T,alphabet_map_inverse)
    #Si restituisce il vettore tradotto
    return translated
    
#   '---------------------------------------------------------------------------------------
#   ' Metodo    : decrypt_block
#   ' Fine      : Questo metodo del cifrario di Hill decifra un blocco del messaggio cifrato.
#   '             la grandezza del blocco è definita dalla variabile block_size, gli altri 
#   '             parametri del metodo sono il blocco stesso, l'alfabeto e la chiave di cifratura.
#   '             questo metodo contiene inoltre la verifica di invertibilità della matrice.
#   '---------------------------------------------------------------------------------------
def decrypt_block(block,block_size,letters,key):
    #Si genera la mappa dell'alfabeto e la mappa inversa
    alphabet_map = generate_alphabet_map(letters)
    alphabet_map_inverse = generate_inverse_alphabet_map(letters)
    #Si vettorizza la chiave
    key = word_to_vector(key,alphabet_map)
    #Si fa il reshaping della chiave in forma di matrice per poter poi
    #eseguire il prodotto K * plaintext
    key_matrix = key_matrix = np.asarray(key).reshape(block_size,block_size)
    #Verifica della condizione di invertibilità per la matrice.
    if(np.linalg.det(key_matrix)==0):
        print("Errore")
        return    
    #Si esegue l'inversione (Se possibile)
    key_matrix_inverse=get_inverse(key_matrix,letters)
    #Si vettorizza e traspone il messaggio
    message_vector = np.asarray(word_to_vector(block,alphabet_map)).T    
    #Prodotto tra la matrice chiave invertita e chipher.
    i =np.dot(key_matrix_inverse,message_vector)
    i = np.array(i).flatten().tolist()
    #Modulo 
    vector_modulus(i,letters)
    #conversione in stringa
    translated = word_to_vector(i,alphabet_map_inverse)
    return translated
   
#   '---------------------------------------------------------------------------------------
#   ' Metodo    : hillChipher_encrypt
#   ' Fine      : Questo metodo implementa il cifrario vero e proprio, prende in ingresso 
#   '             il messaggio, la chiave e la block_size, divide il messaggio in blocchi
#   '             e richiama la procedura di cifratura dei blocchi su ogni blocco.
#   '             unisce quindi il risultato in una stringa unica.
#   '---------------------------------------------------------------------------------------
def hillChipher_encrypt(text,key,BLOCK_SIZE):           
    chunks = [text[i:i+BLOCK_SIZE] for i in range(0, len(text), BLOCK_SIZE)]
    encrypted = ""
    for chunk in chunks:
        enc_block = encrypt_block(chunk,BLOCK_SIZE,letters,key)
        for letter in enc_block:
            encrypted = encrypted + str(letter)
    return encrypted
 
#   '---------------------------------------------------------------------------------------
#   ' Metodo    : hillChipher_decrypt
#   ' Fine      : Questo metodo decifra un messaggio con cifrario di Hill, esegue l'opposto
#   '             del metodo precedente.
#   '---------------------------------------------------------------------------------------
def hillChipher_decrypt(text,key,BLOCK_SIZE):
    chunks = [text[i:i+BLOCK_SIZE] for i in range(0, len(text), BLOCK_SIZE)]
    decrypted = ""
    for chunk in chunks:
        enc_block = decrypt_block(chunk,BLOCK_SIZE,letters,key)
        for letter in enc_block:
            decrypted = decrypted + str(letter)
    return decrypted



# ---------- Main ----------

MESSAGE = "bhjdiuptktqt"
KEY = "gybnqkurp"    
BLOCK_SIZE = 3

print("originale:",MESSAGE)
enc = hillChipher_encrypt(MESSAGE,KEY,BLOCK_SIZE)
print("enc: ", enc)
dec = hillChipher_decrypt(enc,KEY,BLOCK_SIZE)
print("dec : ",dec)






#attacco, costruisco un insieme di coppie plain,cypher 
#mi servono m coppie con M lunghezza del blocco




    