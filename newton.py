import numpy as np

def f(x):  #f = x^4 - 2x^3 - 4x^2 + 4x + 4:
    total = pow(x, 4) - 2 * pow(x, 3) - 4 * pow(x, 2) + 4 * x + 4
    return total

def deri(x): #f' = 4x^3 - 6x^2 - 8x + 4
    total = 4 * pow(x, 3) - 6 * pow(x, 2) - 8 * x + 4
    return total

def newton(e, max, a, b):
    x = []
    x.append((a + b) / 2) #+ 1 para o segundo ponto
    print(0, x[0], 0.0)
    i = 1

    for k in range(1, max):
        x.append(x[k - 1] - f(x[k - 1]) / deri(x[k - 1]))

        erro = np.abs(x[k] - x[k - 1])
        print(i, x[k], erro)

        if erro < e:
            break

        i = i + 1

def main():
    #e = input("Erro: ")
    #max = input("Max iterações: ")
    #a = input("Ponto a: ")
    #b = input("Ponto b: ")
    #newton(float(e), int(max), int(a), int(b))
    newton(0.000001, 20, 0, 3)

if __name__ == '__main__':
    main()
