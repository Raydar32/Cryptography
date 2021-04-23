import miller_rabin as miller
import random



def generate_number(bits):    
    bit_sequence = []
    for i in range(0,bits):
        bit_sequence.append(random.randint(0,1))
    n = int("".join(str(i) for i in bit_sequence),2)
    return n

def generate_prime(bits):  
    while(True):
        n = generate_number(bits)
        if miller.miller_rabin(n,10) == False:
            return n
        else:
            continue
        

    
if __name__ == "__main__":
    bits = int(input("Inserire num. bit numero da generare > "))
    print("n : ", generate_prime(bits))