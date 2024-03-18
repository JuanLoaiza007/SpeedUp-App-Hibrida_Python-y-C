import ctypes
import os

ccalc = ctypes.CDLL(os.path.abspath("./libs/libcmath.so"))

print(ccalc.multiplicacion(100, 20))
