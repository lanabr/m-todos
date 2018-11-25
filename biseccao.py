import numpy as np

def f(x): #f = x^4 - 2x^3 - 4x^2 + 4x + 4:
    total = pow(x, 4) - 2 * pow(x, 3) - 4 * pow(x, 2) + 4 * x + 4
    return total

def bisec(e, max, a, b):   #e = precisão
    i = 0
    x = []

    for k in range(0, max):
        x.append((a + b) / 2)
        
        if f(x[k]) < 0:
            b = x[k]
        else:
            a = x[k]

        erro = np.abs(x[k] - x[k - 1])
        print(i, x[k], erro)

        if np.abs(b - a) < e:
            break

        i = i + 1

def main():
    #e = input("Erro: ")
    #max = input("Max iterações: ")
    #a = input("Ponto a: ")
    #b = input("Ponto b: ")
    #bisec(float(e), int(max), int(a), int(b))
    bisec(0.000001, 50, 0, 3)
    
    k = (np.log10(3) - np.log10(0.000001)) / np.log10(2)
    print("Quantidade de iterações teóricas:", np.ceil(k))


if __name__ == '__main__':
    main()
