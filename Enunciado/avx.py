# -*- coding: utf-8 -*-
"""AVX.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EK_lEqUoUkpMOnHcCF_ZS-xn-4y9e0Za

# Operaciones AVX (Advanced Vector eXtensions)

Se presentarán a continuación algunos códigos de ejemplo relacionados con la multiplicación de vector de números de punto flotante con escalar y la operación punto (vector x vector = escalar) en sus versiones Python y en C. En sus versiones en C se presentarán versiones usando la forma regular de operar sobre vectores, se presentarán versiones con AVX y se presentarán una versión con OpenMP.

## Multiplicación vector por entero o multiplicación escalar

Se presentará a continuación la implementación en Python y en C de la multiplicación de vector por escalar:

$ \vec{v} \times x = \begin{pmatrix} v_0 \times x, v_1 \times x, \ldots, v_{n - 1} \times x \end{pmatrix} $

### Versión en Python
"""

import numpy as np

n = 10000000
lst = range(0,n)
x = 2
v = np.array(lst)

for i in lst:
  v[i] = v[i] * x

#print(v)

"""### Versión en C"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile multescalar.c
# #include <immintrin.h>
# #include <stdio.h>
# #include <assert.h>
# 
# #define VECTORSIZE 4
# 
# // Function to perform vector-scalar multiplication
# void vectorScalarMultiply(const double* vector, double scalar, double* result, int length) {
# 
#     for (int i = 0; i < length; i++) {
#       result[i] = vector[i] * scalar;
#     }
# }
# 
# int main(int argc, char* argv[]) {
#     // Example data
#     int vectorSize;
#     double *vector;
#     double scalar = 2.0;
#     double *result;
# 
#     if (argc == 1) {
#         vectorSize = VECTORSIZE;
#     } else {
#         vectorSize = atoi(argv[1]);
#     }
#     vector = (double*)malloc(sizeof(double)*vectorSize);
#     assert(vector != NULL);
#     result = (double*)malloc(sizeof(double)*vectorSize);
#     assert(result != NULL);
# 
#     // Initialize the vector with some values
#     for (int i = 0; i < vectorSize; ++i) {
#         vector[i] = i + 1;
#     }
# 
#     // Perform vector-scalar multiplication
#     vectorScalarMultiply(vector, scalar, result, vectorSize);
# 
#     // Print the result
# #ifdef DEBUG
#     printf("Original Vector:\n");
#     for (int i = 0; i < vectorSize; ++i) {
#         printf("%lf ", vector[i]);
#     }
# 
#     //printf("\nScalar: %lf\n", scalar);
# 
#     printf("Result:\n");
#     for (int i = 0; i < vectorSize; ++i) {
#         printf("%lf ", result[i]);
#     }
# #endif
# 
#     free(vector);
#     free(result);
# 
#     return 0;
# }

!gcc -o multescalar multescalar.c
!time ./multescalar 10000000

"""### Versión en C (AVX)"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile multescalar-avx.c
# /**
# Este código fue desarrollado en colaboración con ChatGPT
# 
# Fecha: 05/03/2024
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# */
# #include <immintrin.h>
# #include <stdio.h>
# #include <assert.h>
# 
# #define VECTORSIZE 4
# 
# // Function to perform vector-scalar multiplication
# void vectorScalarMultiply(const double* vector, double scalar, double* result, int length) {
#     // Ensure the length is a multiple of 4 for proper alignment
#     int alignedLength = (length + 3) & ~3;
# 
#     // Loop through the vector in 4-element chunks
#     for (int i = 0; i < alignedLength; i += 4) {
#         // Load the vector chunk into AVX register
#         __m256d vec = _mm256_loadu_pd(vector + i);
# 
#         // Broadcast the scalar value to all elements of another AVX register
#         __m256d scalarVec = _mm256_broadcast_sd(&scalar);
# 
#         // Perform element-wise multiplication
#         __m256d resultVec = _mm256_mul_pd(vec, scalarVec);
# 
#         // Store the result back to memory
#         _mm256_storeu_pd(result + i, resultVec);
#     }
# }
# 
# int main(int argc, char* argv[]) {
#     // Example data
#     int vectorSize;
#     double *vector;
#     double scalar = 2.0;
#     double *result;
# 
#     if (argc == 1) {
#         vectorSize = VECTORSIZE;
#     } else {
#         vectorSize = atoi(argv[1]);
#     }
#     vector = (double*)malloc(sizeof(double)*vectorSize);
#     assert(vector != NULL);
#     result = (double*)malloc(sizeof(double)*vectorSize);
#     assert(result != NULL);
# 
#     // Initialize the vector with some values
#     for (int i = 0; i < vectorSize; ++i) {
#         vector[i] = i + 1;
#     }
# 
#     // Perform vector-scalar multiplication
#     vectorScalarMultiply(vector, scalar, result, vectorSize);
# 
# #ifdef DEBUG
#     // Print the result
#     printf("Original Vector:\n");
#     for (int i = 0; i < vectorSize; ++i) {
#         printf("%lf ", vector[i]);
#     }
# 
#     printf("\nScalar: %lf\n", scalar);
# 
#     printf("Result:\n");
#     for (int i = 0; i < vectorSize; ++i) {
#         printf("%lf ", result[i]);
#     }
# #endif
# 
#     free(vector);
#     free(result);
# 
#     return 0;
# }
#

!gcc -march=native -o multescalar-avx multescalar-avx.c
!time ./multescalar-avx 10000000

"""## Producto punto

$ \vec{v_1} \times \vec{v_2} = (v_{1,0} \times v_{2,0}) + (v_{1,1} \times v_{2,1}) +  \ldots + (v_{1, n - 1} \times v_{2, n - 1}) $

### Versión en Python
"""

import numpy as np

n = 10000000
lst = range(0,n)
x = 2
v1 = np.array(lst)
v2 = np.array(lst)
for i in lst:
  v2[i] = 1
sum = 0
for i in lst:
  sum = sum + (v1[i] + 1) * v2[i]

"""### Versión en C

### Versión en C (AVX)
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile dotProduct-avx.c
# #include <immintrin.h>
# #include <stdio.h>
# #include <assert.h>
# 
# #define VECTORSIZE 4
# 
# // Function to calculate the dot product of two vectors
# double dotProduct(const double* vec1, const double* vec2, int length) {
#     // Ensure the length is a multiple of 4 for proper alignment
#     int alignedLength = (length + 3) & ~3;
# 
#     // Initialize accumulators
#     __m256d sumVec = _mm256_setzero_pd();
# 
#     // Loop through the vectors in 4-element chunks
#     for (int i = 0; i < alignedLength; i += 4) {
#         // Load 4 elements from each vector into AVX registers
#         __m256d vec1Chunk = _mm256_loadu_pd(vec1 + i);
#         __m256d vec2Chunk = _mm256_loadu_pd(vec2 + i);
# 
#         // Multiply corresponding elements
#         __m256d product = _mm256_mul_pd(vec1Chunk, vec2Chunk);
# 
#         // Accumulate the product
#         sumVec = _mm256_add_pd(sumVec, product);
#     }
# 
#     // Sum the elements in the accumulator
#     double result[4];
#     _mm256_storeu_pd(result, sumVec);
#     return result[0] + result[1] + result[2] + result[3];
# }
# 
# int main(int argc, char* argv[]) {
#     // Example vectors
#     int vectorSize;
#     int i;
#     double *vector1;
#     double *vector2;
# 
#     if (argc == 1)
#         vectorSize = VECTORSIZE;
#     else
#         vectorSize = atoi(argv[1]);
# 
#     vector1 = (double*)malloc(sizeof(double) * vectorSize);
#     assert(vector1 != NULL);
#     vector2 = (double*)malloc(sizeof(double) * vectorSize);
#     assert(vector2 != NULL);
# 
#     for (i = 0; i < vectorSize; i++) {
#         vector1[i] = 1;
#         vector2[i] = i + 1;
#     }
# 
#     // Calculate the dot product
#     double result = dotProduct(vector1, vector2, vectorSize);
# 
#     // Print the result
#     printf("Dot Product: %lf\n", result);
# 
#     return 0;
# }

!gcc -o dotProduct-avx -march=native dotProduct-avx.c
!time ./dotProduct-avx 10000000