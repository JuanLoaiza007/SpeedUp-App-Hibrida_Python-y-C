import py_avx as avx
import py_numpy as numpy
import py_ingenuo as ingenuo
import cProfile
import pstats

arreglo = [i for i in range(1000000)]
escalar = 2.0

print("Ingenua:")
prof = cProfile.Profile()
prof.enable()
ingenuo.main(arreglo, escalar)
prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)

print("Numpy:")
prof = cProfile.Profile()
prof.enable()
numpy.main(arreglo, escalar)
prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)

print("AVX:")
prof = cProfile.Profile()
prof.enable()
avx.main(arreglo, escalar)
prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)