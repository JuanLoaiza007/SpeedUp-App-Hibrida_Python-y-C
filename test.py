import py_avx as avx
import py_numpy as numpy
import py_ingenuo as ingenuo
import cProfile
import pstats
import timeit

n = 1000000
arreglo = [i for i in range(n)]
escalar = 2.0

print(f"Prueba con vector de {n} números \n")

# Medir el tiempo de ejecución con timeit
print("Con timeit")
ingenuo_time = timeit.timeit(lambda: ingenuo.main(arreglo, escalar), number=10)
numpy_time = timeit.timeit(lambda: numpy.main(arreglo, escalar), number=10)
avx_time = timeit.timeit(lambda: avx.main(arreglo, escalar), number=10)

print("Tiempo de ejecución (ingenuo):", ingenuo_time/10)
print("Tiempo de ejecución (numpy):", numpy_time/10)
print("Tiempo de ejecución (avx):", avx_time/10)

print("Speedups:")

speedup_numpy = ingenuo_time / numpy_time
speedup_avx = ingenuo_time / avx_time

print("Speedup (numpy):", speedup_numpy)
print("Speedup (avx):", speedup_avx)


# Profiling con cProfile
print("")
print("Con cProfile")
print("Ingenua:")
prof = cProfile.Profile()
prof.enable()
ingenuo.main(arreglo, escalar)
prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)
ingenuo_time_p = stats.total_tt

print("")
print("Numpy:")
prof = cProfile.Profile()
prof.enable()
numpy.main(arreglo, escalar)
prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)
numpy_time_p = stats.total_tt

print("")
print("AVX:")
prof = cProfile.Profile()
prof.enable()
avx.main(arreglo, escalar)
prof.disable()
stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)
avx_time_p = stats.total_tt

print("Tiempo de ejecución (ingenuo):", ingenuo_time_p)
print("Tiempo de ejecución (numpy):", numpy_time_p)
print("Tiempo de ejecución (avx):", avx_time_p)

# Calcular el speedup
speedup_numpy_p = ingenuo_time_p / numpy_time_p
speedup_avx_p = ingenuo_time_p / avx_time_p

print("Speedup (numpy):", speedup_numpy_p)
print("Speedup (avx):", speedup_avx_p)