import matplotlib.pyplot as plt
import numpy as np

def f5(x):
    return 0.1379 + 1.0093*(x + 0.5) + 2.8595*(x + 0.5)*(x + 0.25) + -16.8209*(x + 0.5)*(x + 0.25)*(x - 0) + 33.6417*(x + 0.5)*(x + 0.25)*(x - 0)*(x - 0.25)

def f11(x):
    return 0.0561 + 0.1823*(x + 0.82) + 0.574*(x + 0.82)*(x + 0.64) + 2.0475*(x + 0.82)*(x + 0.64)*(x + 0.46) + 4.0811*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28) + -42.368*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28)*(x + 0.1) + 95.9481*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28)*(x + 0.1)*(x - 0.08) + -106.146*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28)*(x + 0.1)*(x - 0.08)*(x - 0.26) + 39.0355*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28)*(x + 0.1)*(x - 0.08)*(x - 0.26)*(x - 0.44) + 74.5818*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28)*(x + 0.1)*(x - 0.08)*(x - 0.26)*(x - 0.44)*(x - 0.62) + -171.7224*(x + 0.82)*(x + 0.64)*(x + 0.46)*(x + 0.28)*(x + 0.1)*(x - 0.08)*(x - 0.26)*(x - 0.44)*(x - 0.62)*(x - 0.8)

def f15(x):
    return 0.0502 + 0.1375*(x + 0.87) + 0.3287*(x + 0.87)*(x + 0.74) + 0.8165*(x + 0.87)*(x + 0.74)*(x + 0.61) + 2.1476*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48) + 4.611*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35) + -14.9319*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22) + -128.7878*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09) + 609.2501*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04) + -1211.9976*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04)*(x - 0.17) + 1225.0252*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04)*(x - 0.17)*(x - 0.3) + -2.1984*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04)*(x - 0.17)*(x - 0.3)*(x - 0.43) + -2368.2953*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04)*(x - 0.17)*(x - 0.3)*(x - 0.43)*(x - 0.56) + 5022.9144*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04)*(x - 0.17)*(x - 0.3)*(x - 0.43)*(x - 0.56)*(x - 0.69) + -6920.1732*(x + 0.87)*(x + 0.74)*(x + 0.61)*(x + 0.48)*(x + 0.35)*(x + 0.22)*(x + 0.09)*(x - 0.04)*(x - 0.17)*(x - 0.3)*(x - 0.43)*(x - 0.56)*(x - 0.69)*(x - 0.82)

def f(x):
    return 1 / (1 + 25 * pow(x, 2))

def main():
    x1 = np.arange(-1, 1, 0.001)
    y1 = []
    for i in range(0, len(x1)):
        y1.append(f5(x1[i]))

    x2 = np.arange(-1, 1, 0.001)
    y2 = []
    for i in range(0, len(x2)):
        y2.append(f11(x2[i]))

    x3 = np.arange(-1, 1, 0.001)
    y3 = []
    for i in range(0, len(x3)):
        y3.append(f15(x3[i]))

    x4 = np.arange(-1, 1, 0.001)
    y4 = []
    for i in range(0, len(x4)):
        y4.append(f(x4[i]))

    plt.plot(x4, y4, 'k--', c='magenta', label='Função 1 / (1 + 25 * x ^ 2))')
    plt.plot(x1, y1, 'k-.', c='red', label='Polinomio com 5 pontos')
    plt.plot(x2, y2, 'k:', c='green', label='Polinomio com 11 pontos')
    plt.plot(x3, y3, 'k-', c='blue', label='Polinomio com 15 pontos')

    plt.legend(loc='upper left')

    plt.xlim(-1, 1)
    plt.ylim(0, 4.5)

    plt.title('Função ii) 1 / (1 + 25 * x ^ 2))')

    plt.show()

if __name__ == '__main__':
    main()
