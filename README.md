# SpeedUp de App Híbrida en Python y C

Este repositorio contiene 3 códigos ejecutables hechos en Python los cuales muestran 3 formas distintas de realizar una multiplicación de un vector por un escalar, además una biblioteca compartida hecha en C, la cual usa instrucciones AVX para multiplicar un vector por un escalar y será usada por uno de los códigos ejecutables de Python. 

## Integrantes

- **Juan David Loaiza Santiago** - 2177570
- **Juan Sebastián Muñoz Rojas** - 2177436
- **Julián David Rendón Cardona** - 2177387

## Cómo usar la biblioteca

**1.** Abrir una terminal en el directorio **lib** y ejecutar el siguiente comando:
```bash
gcc -fPIC -shared -march=native -o vectorScalarMultiplyAVX.so vectorScalarMultiplyAVX.c
```
Esto lo que hace es compilar el código en C y se genere un **shared object** que representa la librería compartida.

**2.** Ejecutar el archivo **py_avx.py** :
```bash
python py_avx.py
```
Al ejecutar se mostrará el resultado del ejemplo usando la librería compartida hecha en C.
