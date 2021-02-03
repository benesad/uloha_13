import argparse
from mtrx import Matrix

def matrix_multiply(matrix1, matrix2):
    if matrix1.width != matrix2.height:
        print("Nasobeni zadanych matic neni definovane.")
        exit()

    result = Matrix(matrix1.width, matrix2.height)
    
    for row_m1 in range(matrix1.height):
        for row_m2 in range(matrix2.width):
            for column_m2 in range(matrix2.height):

                result.representation[row_m1][row_m2] += (int(matrix1.representation[row_m1][column_m2])) * (int(matrix2.representation[column_m2][row_m2]))
    return result

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--matrix1', required=False, default=None)
parser.add_argument('-b', '--matrix2', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.matrix1 != None and args.matrix2 != None and args.output != None:
    matrix1 = Matrix()
    matrix2 = Matrix()
    matrix1.read(args.matrix1)
    matrix2.read(args.matrix2)
    matrix_multiply(matrix1, matrix2)

else:
    print("Nezadali jste povinne argumenty (-a,b pro vstupni matice, -o pro vystupni soubor.")
    exit()

                      