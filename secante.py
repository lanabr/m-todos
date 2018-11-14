import numpy as np

def f(x):  #f = x^4 - 2x^3 - 4x^2 + 4x + 4:
    total = pow(x, 4) - 2 * pow(x, 3) - 4 * pow(x, 2) + 4 * x + 4
    return total

def secante(e, max, a, b):
    xf = 0
    x = []

    x.append((a + b) / 2)
    print("0", x[0], "0.0")
    x.append(((a + b) / 2) - 0.1)
    i = 1
    for k in range(2, max):

        x.append((x[k - 2] * f(x[k - 1]) - x[k - 1] * f(x[k - 2])) / (f(x[k - 1]) - f(x[k - 2])))

        erro = np.abs(x[k] - x[k - 1])
        print(i, x[k], erro)

        if erro < e:
            xf = x[k]
            break
        i = i + 1

def main():
    #e = input("Erro: ")
    #max = input("Max iterações: ")
    #a = input("Ponto a: ")
    #b = input("Ponto b: ")
    #secante(float(e), int(max), int(a), int(b))
    secante(0.0000001, 20, 0, 3)

if __name__ == '__main__':
    main()
