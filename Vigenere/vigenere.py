# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:24:50 2021

@author: Alessandro
"""

import string
import sys

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def preprocess_word(word):    
    word = word.lower()    
    word = word.replace(" ","")    
    word = word.translate(str.maketrans('', '', string.punctuation))
    return ''.join(word)

def repeat_string(a_string, target_length):
    if(len(a_string)<=target_length):
        number_of_repeats = target_length // len(a_string) + 1
        a_string_repeated = a_string * number_of_repeats
        a_string_repeated_to_target = a_string_repeated[:target_length]
        return a_string_repeated_to_target
    else:
        return a_string[:target_length]

def shift_sum(l1,l2,letters):
    new_char = (letters.index(l1) + letters.index(l2))%26
    return letters[new_char]
    
def shift_subtract(l1,l2,letters):
    new_char = (letters.index(l1) - letters.index(l2))%26
    return letters[new_char]

def vigenere_enc(text,key):
    key = repeat_string(key,len(text))
    cipher = ""
    for i in range(0,len(text)):     
        cipher = cipher + shift_sum(text[i],key[i],letters)
    return cipher
        
def vigenere_dec(text,key):
    key = repeat_string(key,len(text))
    cipher = ""
    for i in range(0,len(text)):     
        cipher = cipher + shift_subtract(text[i],key[i],letters)
    return cipher
        
while(True):
    ch = int(input("Premere:\n[1]Per cifrare un testo\n[2]Per uscire"))
    if(ch==1):
        text = input("Inserire testo da cifrare > ")
        text = preprocess_word(text)
        key = input("Inserire chiave (verra ripetuta) > ")
        key = repeat_string(key,len(text))
        enc = vigenere_enc(text,key)
        print("Cifrato :", enc)
        print("Originale: ", vigenere_dec(enc,key))
        print("Chiave : ",key)
    if(ch==2):
        sys.exit(0)


#'PLGTSETUU'#
