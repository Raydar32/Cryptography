#   '---------------------------------------------------------------------------------------
#   ' File      : hill_console.py
#   ' Author    : Alessandro Mini (mat. 7060381)
#   ' Date      : 10/03/2021
#   ' Purpose   : In questo file .py viene implementata la console di controllo del cifrario
#   '             di Hill in cui è possibile cifrare/decifrare.
#   '---------------------------------------------------------------------------------------


import hill_cypher as hc
import sys

def hasNumbers(inputString):
     return any(char.isdigit() for char in inputString)
def preprocess_word(word,BLOCK_SIZE):
    print("[PREPROC]: Conversione in lower case")
    word = word.lower()
    print("[PREPROC]: Rimozione degli spazi")
    word = word.replace(" ","")
    if(len(word)%BLOCK_SIZE)!=0:        
        print("[PREPROC]: Applicazione carattere di padding: 'X'")
        for i in range(0,len(word)%BLOCK_SIZE):
            word = word + 'x'
    print("[PREPROC]: Result : ", word)
    return word

def check_key(key):
    if " " in key or hasNumbers(key):
        return False
    else:
        return True
    
while True:   
    choice = input("Premere:\n[1] per cifrare/decifrare una parola\n[2] per uscire")     
    if(int(choice)==1):
        key = input("Inserire la chiave > ").lower()
        BLOCK_SIZE = int(input("Inserire block size > "))
        word = input("Inserire parola o frase da cifrare > ")
        
        if len(key) != pow(BLOCK_SIZE,2) or check_key(key) == False:
            print("Errore, block size e lunghezza chiave non compatibili")
            sys.exit(0)           
            
        word = preprocess_word(word,BLOCK_SIZE)        
        print("----    Avvio procedura di cifratura    ----")
        print("originale:",word)
        enc = hc.hillChipher_encrypt(word,key,BLOCK_SIZE)
        print("enc: ", enc)
        try:
            dec = hc.hillChipher_decrypt(enc,key,BLOCK_SIZE)
        except:
            print("Errore: la matrice non è invertibile")
        else:
            print("dec : ",dec)
            print("--------------------------------------------")
    if (int(choice)==2):
        sys.exit(0)
        
