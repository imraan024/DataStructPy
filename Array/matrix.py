from numpy import *

matrix1 = matrix('3, 24, 5; 24, 6, 2 ; 4, 5, 76')
matrix2 = matrix('4, 3, 4 ; 24, 5, 1; 6, 67, 2')

matrix3 = matrix1 + matrix2
matrix4 = matrix1 * matrix2 #for multiplication it should be 1st matrix row = 2nd matrix column.

print("Sum of the matrices: ", matrix3)
print("Multiplication of the matrices: ", matrix4)
