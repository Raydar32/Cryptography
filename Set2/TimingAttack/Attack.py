import TimingAttackModule as t
import random
from tqdm import tqdm
import numpy as np 

ta = t.TimingAttack()


def generate_base_key():
    a = [1,]
    for i in range(1,64):
        a.append(0)
    a[len(a)-1] = 1
    return a

       
def get_attacker_times(lista,key):
    times = []
    for item in lista:
        times.append(ta.attackerdevice(item,key))
    return times

def get_victim_times(lista):
    times = []
    for item in lista:
        times.append(ta.victimdevice(item))
    return times

def generate_random_array(leng):
    a = []        
    for i in range(0,leng):
        a.append(random.randint(1000,100000))
    return a

def calculateDifference(client_times,attacker_times,index):
    diff = float(client_times[index])-float(attacker_times[index])  
    return diff


#10000 tests sono sufficenti a recuperare la chiave
tests = int(input("Inserire num. caratteri da inviare alla vittima > "))
#Inizializzo una chiave vuota
rsa_base_key = generate_base_key()
#Genero un array di caratteri casuali
random_chars = generate_random_array(tests)
#Calcolo i tempi della vittima
client_times = np.array(get_victim_times(random_chars),dtype=np.float32)
#Calcolo i tempi dell'attacker
attacker_times = get_attacker_times(random_chars,rsa_base_key)

#Per ogni bit della chiave
for i in tqdm(range(1,len(rsa_base_key))):
    #testo bit 0
    rsa_base_key[i] = 0
    #calcolo tempi_vittima_originali - tempi_attacker con chiave rsa_base_key
    times_0 = client_times - np.array(get_attacker_times(random_chars,rsa_base_key),dtype=np.float32) 
    #ripeto con bit = 1
    rsa_base_key[i] = 1
    times_1 = client_times - np.array(get_attacker_times(random_chars,rsa_base_key),dtype=np.float32) 
    #scelgo il bit sulla base della scelta che minimizza la varianza
    if np.var(times_0) < np.var(times_1):
        rsa_base_key[i] = 0
    else:
        rsa_base_key[i] = 1
    
key_1 = rsa_base_key

print("\n----------------------")
print(ta.test(key_1))
print("\n----------------------")
     
    
#10000 test recupera.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    