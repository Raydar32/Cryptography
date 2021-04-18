import time


def exp_veloce(a, m, n):
    m = [int(x) for x in list("{0:0b}".format(m))]
    d = 1
    i = 0
    for bit in reversed(m):
        d = (d * d) % n
        if m[i] == 1:
            d = (d * a) % n
        i = i + 1
    return d


def exp_norm(a, m, n):
    temp = 1
    for i in range(0, m):
        temp = temp * a
    return temp % n


print("----------------------------------")
print("Esponenziale Veloce")
print("Esegue a^n mod n")
print("----------------------------------")
a = int(input("Inserire a -> "))
m = int(input("Inserire m -> "))
n = int(input("Inserire n -> "))
print("----------------------------------")
start = time.perf_counter()
start_time = time.time()
end = time.perf_counter()
print("[EXP.Veloce] Risultato: ", exp_veloce(a, m, n), " tempo: ", end - start, "s")


start = time.perf_counter()
start_time = time.time()
end = time.perf_counter()
print("[EXP.Norm]   Risultato: ", exp_norm(a, m, n), " tempo: ", end - start, "s")
