





import numpy as np
from sympy import Matrix
import math

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def vector_modulus(vector,alphabet):
    for i in range(0,len(vector)):
        vector[i] = vector[i] % len(alphabet)        
def generate_alphabet_map(letters):       
    dizionario = {}
    for idx,letter in enumerate(letters):
        dizionario[letter] = idx
    return dizionario
def generate_inverse_alphabet_map(letters):
    dizionario = {}
    for idx,letter in enumerate(letters):
        dizionario[letter] = idx    
    inv = {v: k for k, v in dizionario.items()}
    return inv
def word_to_vector(message,mapfunc):
    vectorized_word = []
    for word in message:
            vectorized_word.append(mapfunc[word])
    return vectorized_word

def encrypt_block(block,block_size,letters,key):
    alphabet_map = generate_alphabet_map(letters)
    alphabet_map_inverse = generate_inverse_alphabet_map(letters)   
    key = word_to_vector(key,alphabet_map)
    key_matrix = key_matrix = np.asarray(key).reshape(block_size,block_size)
    message_vector = np.asarray(word_to_vector(block,alphabet_map)).T
    i = np.dot(key_matrix,message_vector)
    vector_modulus(i,letters)
    translated = word_to_vector(i.T,alphabet_map_inverse)
    return translated
    

def get_inverse(matrix, alphabet):
    alphabet_len = len(alphabet)    
    matrix = Matrix(matrix)
    return np.matrix(matrix.inv_mod(alphabet_len))

    
    
def decrypt_block(block,block_size,letters,key):
    alphabet_map = generate_alphabet_map(letters)
    alphabet_map_inverse = generate_inverse_alphabet_map(letters)   
    key = word_to_vector(key,alphabet_map)
    key_matrix = key_matrix = np.asarray(key).reshape(block_size,block_size)
    
    if(np.linalg.det(key_matrix)==0):
        print("Errore")
        return    
    key_matrix_inverse=get_inverse(key_matrix,letters)
    message_vector = np.asarray(word_to_vector(block,alphabet_map)).T

def hillChipher_encrypt(text,key,BLOCK_SIZE):           
    chunks = [text[i:i+BLOCK_SIZE] for i in range(0, len(text), BLOCK_SIZE)]
    encrypted = ""
    for chunk in chunks:
        enc_block = encrypt_block(chunk,BLOCK_SIZE,letters,key)
        for letter in enc_block:
            encrypted = encrypted + str(letter)
    return encrypted


#BLOCK_SIZE = 4
#phrase = "heilhitlerweattacktomorr"
#KEY = "abcdfhjkshcnsjch"   
#enc = hillChipher_encrypt(phrase,KEY,BLOCK_SIZE)
    
MESSAGE = "act"
KEY = "gybnqkurp"    
BLOCK_SIZE = 3
result = decrypt_block(MESSAGE,BLOCK_SIZE,letters,KEY)



    