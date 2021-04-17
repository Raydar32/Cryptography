from timeit import default_timer as timer



print("Algoritmo di esponenz. veloce")
print("Esegue a^m mod n")
a = int(input("inserire a : "))
m = int(input("inserire m : "))
n = int(input("inserire n : "))
m_orig = m
m = [int(x) for x in list('{0:0b}'.format(m))]

d = 1
i = 0

print("###    Algoritmo di esponenz. veloce    ###")
start = timer() # Benchmark temporale
for bit in reversed(m):
    d = (d*d)%n
    if m[i]==1:
        d = (d*a)%n
    i = i + 1
end = timer()
print("Risultato : ", d, " Ottenuto in : ",end-start,"s")



print("###   Algoritmo di esponenz. 'classico'    ###")
start = timer() # Benchmark temporale
temp = 1
for i in range(0,m_orig):
    temp = temp *a 

end = timer()
print("Risultato: ",temp%n,"Ottenuto in : ",end-start,"s")