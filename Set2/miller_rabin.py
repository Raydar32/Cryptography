import random

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

def find_r_d(n):
    # Funzione per determinare i parametri r,d
    # t.c n-1 = (2^r)*d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r = 1
        d = d // 2
    return r, d


def miller_rabin(n, k):
    # Calcolo la fattorizzazione di n per determinare r,d
    r, d = find_r_d(n)
    #print("Parametri: n =", n, " k =", k, " r =", r, "d =", d)
    # Assumendo p(test_singolo) = 0.25 (al più)
    #print("Prob errore (max):", ((pow(0.25, k))))
    # k = accuratezza
    for i in range(1, k):
        # Calcolo a^d mod n con a scelto casualmente
        a = random.randint(2, n - 2)
        # Si richiama il metodo di exp veloce
        x = exp_veloce(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for q in range(1, r - 1):
            x = (x * x) % n
            if x == 1:
                return True
            if x == n - 1:
                continue
        return True
    return False


if __name__ == "__main__":
    n = 15
    k = 10
    print("----------------------------------")
    print("Test di primalità Miller-Rabin")
    print("----------------------------------")
    n = int(input("Inserire n da testare -> "))
    k = int(input("Inserire num esecuzioni -> "))
    print("Esito: ", miller_rabin(n, k))
    
