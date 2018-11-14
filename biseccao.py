import numpy as np

def g(x): #f = x^4 - 2x^3 - 4x^2 + 4x + 4:
    total = pow(x, 4) - 2 * pow(x, 3) - 4 * pow(x, 2) + 4 * x + 4
    return total

def bisec(e, max, a, b):   #e = precisão
    i = 0

    for k in range(0, max):
        x = (a + b)/2

        if (g(a) * g(b)) < 0:
            b = x
        else:
            a = x

        erro = np.abs(b - a)
        print(i, x, erro)

        if erro < e:
            x = (b - a)/2
            break

        i = i + 1
    return x

def main():
    e = input("Erro: ")
    max = input("Max iterações: ")
    a = input("Ponto a: ")
    b = input("Ponto b: ")
    bisec(float(e), int(max), int(a), int(b))

if __name__ == '__main__':
    main()
