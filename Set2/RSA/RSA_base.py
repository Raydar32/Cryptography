import prime_generator as prime
import extended_euclid as eea
import exp 

phi_n = 0
def generate_coprime(bits,k):
    while True:
        n = prime.generate_number(bits-1)
        gcd,x,y=  eea.EEA(n,k)
        if(gcd==1):
            return n
        else:
            continue
        
def generate_d(bits,phi):
    q = generate_coprime(bits-1,phi)
    return q

def generate_e(d,phi):
    gcd,x,y=  eea.EEA(phi,d)
    return y

def generate_keys(bits,phi):
    while(True):
        d = generate_d(bits,phi)
        e = generate_e(d,phi)
        if(d>0 and e>0):
            return d,e

def rsa_encrypt(messaggio,e,n):
        messaggio_ascii = [ord(ele) for sub in list(messaggio) for ele in sub]        
        enc = []
        for word in messaggio_ascii:
            c = exp.exp_veloce(int(word),e,n)
            enc.append(c)
        return enc
    
def rsa_decrypt(messaggio,d,n):
        dec = []
        for word in messaggio:
            m = exp.exp_veloce(int(word),d,n)
            dec.append(m)
        return ''.join(chr(i) for i in dec)

if __name__== "__main__":
    
    bits = int(input("Inserire numero bit > "))
    p = prime.generate_prime(bits)
    q = prime.generate_prime(bits)
    n = p * q 
    phi_n = (p-1)*(q-1)    
    d,e = generate_keys(bits,phi_n)
    print("----------------------------------")
    print("p: ", p)
    print("q: ", q)
    print("n: ", n)
    print("Phi(n): ",phi_n)
    print("d: ", d)
    print("e: ", e)
    print("----------------------------------")
    print("Chiave pubblica: (",n,",",e,")")
    print("Chiave privata: (",n,",",d,")")
    print("----------------------------------")    
   
    messaggio = input("Inserire messaggio > ")
    enc = rsa_encrypt(messaggio,e,n)
    print("Enc: ", enc )
    print("Dec: ", rsa_decrypt(enc,d,n))
