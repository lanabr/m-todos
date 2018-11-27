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

def ys(x, n):  #função para calcular os ys dependendo da função
    y = []

    for i in range(0, len(x)):
        if n == 1:
            y.append(f1(x[i]))
        else:
            y.append(f2(x[i]))

    return y

def main():
    fx = []
    x = [-0.5, 0, 0.5]
    y = ys(x, 1)  #1 para a primeira função, 2 para a segunda
    n = len(x)   # grau do polinomio
    xi = 1

    for i in range(0, n):
        fx.append(difdiv(0, i, y, x))
        for j in range(0, i):
            fx[i] = fx[i] * (xi - x[j])

    f = sum(fx)
    print(f)

if __name__ == '__main__':
    main()
