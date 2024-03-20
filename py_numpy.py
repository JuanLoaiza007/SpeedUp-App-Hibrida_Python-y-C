import numpy as np


def main(arreglo, escalar):
    arreglo = np.array(arreglo)
    resultado = arreglo * escalar

    # print("Resultado: ", resultado)


if __name__ == "__main__":
    arreglo = [0.0, 1.0, 2.0, 3.0]
    escalar = 2.0
    main(arreglo, escalar)
