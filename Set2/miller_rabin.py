# -*- coding: utf-8 -*-
import random

def find_r_d(n):
    #Funzione per determinare i parametri r,d
    #t.c n-1 = (2^r)*d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d//2
    return r,d

def miller_rabin(n,k):
    #Calcolo la fattorizzazione di n per determinare r,d
    r,d = find_r_d(n)
    print("Parametri: n =",n," k =",k," r =", r , "d =",d)
    #Assumendo p(test_singolo) = 0.25 (al più)
    print("Prob errore (max):",((pow(0.25,k))))
    #k = accuratezza
    for i in range(1,k):
        #Calcolo a^d mod n con a scelto casualmente
        a = random.randint(2,n-2)
        x = pow(a,d)%n
        if x==1 or x==n-1:
            continue
        for q in range(1,r-1):
            x = (x*x)%n
            if x==1:
                return True
            if x==n-1:
                continue
        return True
    return False

    
n = 15
k = 10
print("Esito: ", miller_rabin(49,2))

#k = 2 errore in 2 tentativi
#k = 3 errore in 68 tentativi
#k = 4 errore in 292
#k = 5 errore in 14537 tentativi
#k = 6 errore in 361712 tentativi


    
