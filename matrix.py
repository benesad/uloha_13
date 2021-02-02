import argparse
from mtrx import Matrix

def matrix_multiply(matrix1, matrix2):
    result = Matrix()
    
    for row_m1 in range(len(matrix1.representation)):
        for row_m2 in range(len(matrix2.representation)):
            coo1 = matrix1.representation[row_m1][row_m2]
            coo2 = matrix2.representation[row_m2][row_m1]
            co_res =  int(coo1)*int(coo2)
            result.representation[row_m2][row_m1] = co_res
    print("hovno")

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

                      