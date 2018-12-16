import matplotlib.pyplot as plt
import numpy as np

def f3(x):
    return 0.6065 + 0.7869 * (x + 0.5) + 0.5105 * (x + 0.5)*(x - 0)

def f7(x):
    return 0.4724 + 0.5367 * (x + 0.75) + 0.3048*(x + 0.75)*(x + 0.5) + 0.1154*(x + 0.75)*(x + 0.5)*(x + 0.25) + 0.0328*(x + 0.75)*(x + 0.5)*(x + 0.25)*(x - 0) + 0.0075*(x + 0.75)*(x + 0.5)*(x + 0.25)*(x - 0)*(x - 0.25) + 0.0014*(x + 0.75)*(x + 0.5)*(x + 0.25)*(x - 0)*(x - 0.25)*(x - 0.5)

def f(x):
    return pow(np.e, x)

def main():
    x1 = np.arange(-1, 1, 0.001)
    y1 = []
    for i in range(0, len(x1)):
        y1.append(f3(x1[i]))

    x2 = np.arange(-1, 1, 0.001)
    y2 = []
    for i in range(0, len(x2)):
        y2.append(f7(x2[i]))

    x3 = np.arange(-1, 1, 0.001)
    y3 = []
    for i in range(0, len(x3)):
        y3.append(f(x3[i]))

    plt.plot(x3, y3, 'k-.', c='orange', label='Função e^x')
    plt.plot(x1, y1, 'k--', c='red', label='Polinomio com 3 pontos')
    plt.plot(x2, y2, 'k:', c='green', label='Polinomio com 7 pontos')

    plt.legend(loc='upper left')

    plt.xlim(-1, 1)
    plt.ylim(0, 3)

    plt.title('FunÃ§Ã£o i) e^x')

    plt.show()

if __name__ == '__main__':
    main()
