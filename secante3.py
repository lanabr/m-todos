import numpy as np
import math

def f(w):  #x(t) = -(g / 2w^2) * ((e^(wt) - e^(-wt)) / 2 - sin(wt))
           #1.7 = -(32.17 / 2w^2) * ((e^(w) - e^(-w)) / 2 - sin(w))
    total = -(32.17 / 2 * pow(w, 2)) * ((pow(math.e, w) - pow(math.e, -w)) / 2 - math.sin(w)) - 1.7
    return total

def secante(e, max, a, b):
    x = []

    x.append((a + b) / 2 - 0.5)
    print("0", x[0], "0.0")
    x.append(((a + b) / 2) + 0.5)
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
    secante(0.00001, 20, -1, 0) 
    #tem que dar -0.317059

if __name__ == '__main__':
    main()
