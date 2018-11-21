import numpy as np
import math

def f(h):  #f = V = L((pir^2) / 2 - r^2 arcsen(h / r) - h(r^2 - h^2)^(1/2))
           #12.4 = 10(pi / 2 - arcsen(h) - h(1 - h^2)^(1/2))
    total = 10 * (math.pi / 2 - math.asin(h) - h * math.sqrt(1 - pow(h, 2))) - 12.4
    return total

def secante(e, max, a, b):
    x = []

    x.append((a + b) / 2)
    print("0", x[0], "0.0")
    x.append(((a + b) / 2) - 0.5)
    print("1", x[1], np.abs(x[1] - x[0]))
    i = 2
    for k in range(2, max):

        x.append((x[k - 2] * f(x[k - 1]) - x[k - 1] * f(x[k - 2])) / (f(x[k - 1]) - f(x[k - 2])))

        erro = np.abs(x[k] - x[k - 1])
        print(i, x[k], erro)

        if erro < e:
            break
        i = i + 1
    print("Profundidade: ", 1 - x[k])

def main():
    #e = input("Erro: ")
    #max = input("Max iterações: ")
    #a = input("Ponto a: ")
    #b = input("Ponto b: ")
    #secante(float(e), int(max), int(a), int(b))
    secante(0.01, 20, 0, 1)   #[0, 1] pois f(0) > 0 e f(1) < 0

if __name__ == '__main__':
    main()
