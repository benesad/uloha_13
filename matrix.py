import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--matrix1', required=False, default=None)
parser.add_argument('-b', '--matrix2', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.matrix1 != None and args.matrix2 != None and args.output != None:
    lines = read(args.matrix1, args.matrix2)
   
else:
    print("Nezadali jste povinne argumenty (-a,b pro vstupni matice, -o pro vystupni soubor.")
    exit()