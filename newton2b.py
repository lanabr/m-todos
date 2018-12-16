import numpy as np

def f(x):  #funçao ii)
    total = 1 / (1 + 25 * pow(x, 2))
    return total

def difdiv(i, f, y, x):  #i = inicio da difdiv, f = fim da difdiv
    if i == f:
        return y[i]
    else:
        fx = (difdiv(i + 1, f, y, x) - difdiv(i, f - 1, y, x)) / (x[f] - x[i])
        return fx

def newton(n, x, y):
    poli = ""

    for i in range(0, n):
        fx = difdiv(0, i, y, x)
        poli = poli + str(round(fx, 4))
        for j in range(0, i):
            poli = poli + "*(x "
            if x[j] < 0:
                poli = poli + "+ " + str(np.abs(x[j])) + ")"
            else:
                poli = poli + "- " + str(x[j]) + ")"

        if i < n - 1:
            poli = poli + " + "

    return poli

def nos(n, k):
    total = np.cos((2 * k + 1) / (2 * (n + 1)) * np.pi)
    return total

def xs(n):
    x = []

    for i in range(0, n):
        x.append(round(nos(n, i), 4))

    return x

def ys(x):
    y = []

    for i in range(0, len(x)):
        y.append(f(x[i]))

    return y

def main():
    #Função b com 5 pontos
    x = xs(5)
    y = ys(x)
    n = len(x)

    poli = newton(n, x, y)

    print("Função b com 5 pontos:\n", poli)

    # Função b com 11 pontos
    x = xs(11)
    y = ys(x)
    n = len(x)

    poli = newton(n, x, y)

    print("Função b com 11 pontos:\n", poli)

    # Função b com 15 pontos
    x = xs(15)
    y = ys(x)
    n = len(x)

    poli = newton(n, x, y)

    print("Função b com 15 pontos:\n", poli)

if __name__ == '__main__':
    main()
