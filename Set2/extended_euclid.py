# Algoritmo di euclide esteso
def EEA(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = EEA(b % a, a)
        return gcd, y - (b // a) * x, x

if __name__ == '__main__':
    print("----------------------------------")
    print("Algoritmo di Euclide esteso\nCalcolo di MCD(a,b)")
    print("----------------------------------")
    a = int(input("Inserire a : "))
    b = int(input("Inserire b : "))
    gcd, x, y = EEA(a, b)
    print("MCD: ", gcd)
    print("Valori di X,Y: ", x, y)
