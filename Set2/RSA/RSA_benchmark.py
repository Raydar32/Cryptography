import string    
import random
import time
import prime_generator as prime
import RSA_base as rsa
import RSA_crt as rsa_crt
from tqdm import tqdm


def random_string(len_):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = len_))    
    
def string_to_ascii(string):
    return [ord(ele) for sub in list(string) for ele in sub]   

def ascii_to_string(ascii_):
    return ''.join(chr(i) for i in ascii_)

def generate_test(num,str_len):
    start_time = time.time()
    res = []
    for i in range(0,num):
        res.append(random_string(str_len))        
    print("Generazione stringhe conclusa in",(time.time() - start_time),"")
    return res
    
    
    
res = generate_test(100,100)

bits = int(input("Inserire numero bit > "))
p = prime.generate_prime(bits)
q = prime.generate_prime(bits)
n = p * q 
phi_n = (p-1)*(q-1)    
d,e = rsa.generate_keys(bits,phi_n)

print("----------------------------------")
print("Esecuzione Cifratura RSA")
for i in tqdm(range(len(res))):
    res[i] = rsa.rsa_encrypt(res[i],e,n)
print("Cifratura RSA conclusa")

print("Esecuzione decifratura NON ottimizzata")
start_time = time.time()
for item in tqdm(res):
    rsa.rsa_decrypt(item,d,n)
print("Decifratura NON ottimizzata conclusa in",(time.time() - start_time),"\n")

print("Esecuzione decifratura  ottimizzata")
dp,dq,qinv = rsa_crt.keyGeneratorCRT(d,p,q)
start_time = time.time()
for item in tqdm(res):                
    rsa_crt.rsa_decrypt(item,d,p,q,dp,dq,qinv)
print("Decifratura  ottimizzata conclusa in",(time.time() - start_time),"\n")

 
 


