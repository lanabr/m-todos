import numpy as np

def f(x):  #f = x^4 - 2x^3 - 4x^2 + 4x + 4, f' = 4x^3 - 6x^2 - 8x + 4
    total = 4 * pow(x, 3) - 6 * pow(x, 2) - 8 * x + 4
    return total

def secante(e, max, a, b):
    x = []

    x.append((a + b) / 2) 
    print("0", x[0], "0.0")
    x.append(((a + b) / 2) - 0.1) 
    print("1", x[1], np.abs(x[1] - x[0]))
    i = 2
    for k in range(2, max):
        x.append((x[k - 2] * f(x[k - 1]) - x[k - 1] * f(x[k - 2])) / (f(x[k - 1]) - f(x[k - 2])))

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
    #secante(float(e), int(max), int(a), int(b))
    secante(0.000001, 20, 0, 3)

if __name__ == '__main__':
    main()
