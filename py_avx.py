import os
import numpy as np
from ctypes import CDLL, c_double, c_int, POINTER

# Tipos de datos de C que usaremos
# c_int                                 # int
# c_double                              # double
# POINTER(c_double)                     # double *


def main(arreglo, escalar):
    # Importar libreria
    libVecScMult = CDLL(os.path.abspath("./lib/vectorScalarMultiplyAVX.so"))
    # Traducir argumentos
    libVecScMult.vectorScalarMultiply.argtypes = [
        POINTER(c_double), c_double, POINTER(c_double), c_int]

    # Variables en python
    arreglo = np.array(arreglo, dtype=np.double)
    resultado = np.zeros(len(arreglo), dtype=np.double)
    length = len(arreglo)

    # Obtener el puntero a los datos del array de NumPy
    vect_ptr = arreglo.ctypes.data_as(POINTER(c_double))
    result_ptr = resultado.ctypes.data_as(POINTER(c_double))

    # Llamar a la función con el puntero al array
    libVecScMult.vectorScalarMultiply(vect_ptr, escalar, result_ptr, length)

    print("Resultado: ", resultado)


if __name__ == "__main__":
    arreglo = [0.0, 1.0, 2.0, 3.0]
    escalar = 2.0
    main(arreglo, escalar)
