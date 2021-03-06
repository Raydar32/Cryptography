# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:05:27 2021

@author: Alessandro
"""

import hill_cypher as hc
import numpy as np

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("----------- Modalità attacco ---------------")

plain_list = ["testtesttest",
              "plainplainpl",
            "cmykeueldlqy",
            "svesinizzhtk",
            "jgtmtinninrf",
            "mhfdvzhsktkm",
            "sjisfziymbws",
            "qkqkgnrmgjyh",
            "tjuodutysgxy",
            "uyshnwkxrfot",
            "prsfnykanzmp",
            "bhjdiuptktqt",]
cipher_list = [
            "uxqctjlaghkv",
            "qhtluiwpchze",
            "mqguewfyagpu",
            "smxbypxayobp",
            "jnvquhipdxxa",
            "lgsbbmqlychc",
            "uqjtsomkugzo",
            "oicjsdgfknzr",
            "mtbuohgfsokn",
            "msmmzpfsovlz",
            "wxbctfvaflrt",
            "bhowdckbtxrb",
                ]

alphabet_map = hc.generate_alphabet_map(letters)
plaintext_matrix = np.zeros((len(plain_list[0]),len(plain_list[0])))
ciphertext_matrix = np.zeros((len(plain_list[0]),len(plain_list[0])))

#Genero la matrice dei plaintext recuperati del tipo 
# p1 | p2 | p3 ... |pm
i = 0
for row in plain_list:
    plaintext_matrix[i] = hc.word_to_vector(row,alphabet_map)
    i = i + 1
plaintext_matrix = plaintext_matrix.T
#Genero la matrice dei ciphertext recuperati del tipo 
# c1 | c2 | c3 ... |cm
i = 0
for row in cipher_list:
    ciphertext_matrix[i] = hc.word_to_vector(row,alphabet_map)
    i = i + 1
ciphertext_matrix = ciphertext_matrix.T

