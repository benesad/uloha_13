import argparse
from mtrx import Matrix

def matrix_multiply(A, B):
    if A.width != B.height:
        print("Nasobeni zadanych matic neni definovane.")
        exit()

    C = Matrix(B.width, A.height)
    
    for row_A in range(A.height):
        for col_B in range(B.width):
            for row_B in range(A.height):
                C.representation[row_A][col_B] += (float(A.representation[row_A][row_B])) * (float(B.representation[row_B][col_B]))
    return C

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--A', required=False, default=None)
parser.add_argument('-b', '--B', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.A != None and args.B != None and args.output != None:
    A = Matrix()
    B = Matrix()
    A.read(args.A)
    B.read(args.B)
    matrix_multiply(A, B)
    C = matrix_multiply(A, B)
    C.save(args.output)

else:
    print("Nezadali jste povinne argumenty (-a,b pro vstupni matice, -o pro vystupni soubor.")
    exit()

                      