#   '---------------------------------------------------------------------------------------
#   ' File      : hill_cypher_attack.py
#   ' Author    : Alessandro Mini (mat. 7060381)
#   ' Date      : 07/03/2021
#   ' Purpose   : In questo file si implementa uno script di attacco al cifrario di hill.
#   '---------------------------------------------------------------------------------------


import hill_cypher as hc
import numpy as np
from sympy import Matrix



letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def get_inverse(matrix, alphabet):
    alphabet_len = len(alphabet)    
    matrix = Matrix(matrix)
    return np.matrix(matrix.inv_mod(alphabet_len))

print("----------- Modalità attacco ---------------")



alphabet_map = hc.generate_alphabet_map(letters)
alphabet_map_inverse = hc.generate_inverse_alphabet_map(letters) 

plain = "plainplainpl"
cipher = "qhtluiwpchze"
BLOCK_SIZE = 3

print ("Divisione del messaggio in blocchi di dim. ",BLOCK_SIZE)
print("Plain text:", plain)
print("Cipher text:", cipher)
plain = hc.word_to_vector(plain,alphabet_map)
cipher =  hc.word_to_vector(cipher,alphabet_map)


plain_chunks = [plain[i:i+BLOCK_SIZE] for i in range(0, len(plain), BLOCK_SIZE)]
cipher_chunks = [cipher[i:i+BLOCK_SIZE] for i in range(0, len(cipher), BLOCK_SIZE)]
plain_chunks = plain_chunks[:BLOCK_SIZE]
cipher_chunks = cipher_chunks[:BLOCK_SIZE]
print("Plain text:", plain_chunks)
print("Cipher text:", cipher_chunks)

plain_matrix = np.zeros((BLOCK_SIZE,BLOCK_SIZE))
for i in range(0,BLOCK_SIZE):
    plain_matrix[i] = plain_chunks[i]

cipher_matrix = np.zeros((BLOCK_SIZE,BLOCK_SIZE))
for i in range(0,BLOCK_SIZE):
    cipher_matrix[i] = cipher_chunks[i]

plain_matrix = np.array(plain_matrix).astype(np.integer)
plain_matrix = plain_matrix.T
cipher_matrix = cipher_matrix.T
print("--------------------------")
print("Decrittazione...")

A = Matrix(plain_matrix) 
A = hc.get_inverse(plain_matrix,letters) 
key = np.dot(cipher_matrix,A).astype(int)
key = key.reshape(1,len(key)*len(key))[0]
decoded_key = []
for i in range(0,key.shape[1]):
    decoded_key.append(key.item(i)%len(letters))
    
print("Chiave decifrata", key)
print("Chiave decifrata", hc.word_to_vector(decoded_key,alphabet_map_inverse))

