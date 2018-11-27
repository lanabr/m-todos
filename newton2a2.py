import numpy as np

def f1(x):  #função i)
    total = pow(np.e, x)
    return total

def f2(x):  #função ii)
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
            poli = poli + "(x "
            if x[j] < 0:
                poli = poli + "+ " + str(np.abs(x[j])) + ")"
            else:
                poli = poli + "- " + str(x[j]) + ")"

        if i < n - 1:
            poli = poli + " + "

    return poli

def ys(x, n):  #função para calcular os ys dependendo da função
    y = []

    for i in range(0, len(x)):
        if n == 1:
            y.append(f1(x[i]))
        else:
            y.append(f2(x[i]))

    return y

def main():
    #Função i) e^x com 3 pontos
    x = [-0.5, 0, 0.5]
    y = ys(x, 1)   #1 para a primeira função, 2 para a segunda
    n = len(x)   #grau do polinomio

    poli = newton(n, x, y)

    print("Função i) e^x com 3 pontos:\n", poli)

    # Função i) e^x com 7 pontos
    x = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]
    y = ys(x, 1)
    n = len(x)

    poli = newton(n, x, y)

    print("Função i) e^x com 7 pontos:\n", poli)

    #Função ii) 1 / (1 + 25 * x ^2) com 5 pontos
    x = [-0.5, -0.25, 0, 0.25, 0.5]
    y = ys(x, 2)
    n = len(x)

    poli = newton(n, x, y)

    print("Função ii) e^x com 5 pontos:\n", poli)

    # Função ii) 1 / (1 + 25 * x ^2) com 11 pontos
    x = [-0.82, -0.64, -0.46, -0.28, -0.1, 0.08, 0.26, 0.44, 0.62, 0.8, 0.98]
    y = ys(x, 2)
    n = len(x)

    poli = newton(n, x, y)

    print("Função ii) e^x com 11 pontos:\n", poli)

    # Função ii) 1 / (1 + 25 * x ^2) com 15 pontos
    x = [-0.87, -0.74, -0.61, -0.48, -0.35, -0.22, -0.09, 0.04, 0.17, 0.3, 0.43, 0.56, 0.69, 0.82, 0.95]
    y = ys(x, 2)
    n = len(x)

    poli = newton(n, x, y)

    print("Função ii) e^x com 15 pontos:\n", poli)

if __name__ == '__main__':
    main()
