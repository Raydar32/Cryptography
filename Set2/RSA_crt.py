# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:16:56 2021

@author: Alessandro
"""

import exp
import extended_euclid as eea

def decryptCRT(c,dp,dq,p,q,qinv):
  m1 =  exp.exp_veloce(c, dp, p) 
  m2 =  exp.exp_veloce(c, dq, q) 
  h = (qinv * (m1 - m2)) % p 
  m = m2 + h * q
  return m

def keyGeneratorCRT(d,p,q):
    dq = exp.exp_veloce(d,1,q-1)
    dp = exp.exp_veloce(d,1,p-1)
    gcd,x,y = eea.EEA(p,q)
    return dp,dq,y

def rsa_decrypt(messaggio,d,p,q,dp,dq,qinv):    
    dec = []
    for word in messaggio:
        m = decryptCRT(word,dp,dq,p,q,qinv)
        dec.append(m)
    return ''.join(chr(i) for i in dec)


