# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:11:24 2021

@author: Alessandro
"""

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
    choice = input("Premere 1 per cifrare/decifrare una parola\n")     
    if(int(choice)==1):
        key = input("Inserire la chiave > ").lower()
        BLOCK_SIZE = int(input("Inserire block size > "))
        word = input("Inserire parola o frase da cifrare > ")
        
        if len(key) != pow(BLOCK_SIZE,2) or check_key(key) == False:
            print("Errore")
            sys.exit(0)
            
            
        word = preprocess_word(word,BLOCK_SIZE)        
        print("----    Avvio procedura di cifratura    ----")
        print("originale:",word)
        enc = hc.hillChipher_encrypt(word,key,BLOCK_SIZE)
        print("enc: ", enc)
        dec = hc.hillChipher_decrypt(enc,key,BLOCK_SIZE)
        print("dec : ",dec)
        print("--------------------------------------------")
        
