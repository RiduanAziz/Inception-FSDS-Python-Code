import argparse
import sys

def calculator(args):
    a = args.a
    b = args.b 
    if args.o == 'add':
        return args.a + args.b
    elif args.o == 'subtract':
        return args.a - args.b
    elif args.o == 'multiply':
        return args.a * args.b
    elif args.o == 'divide':
        if args.b != 0:
            return args.a / args.b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"
    

perser = argparse.ArgumentParser()
perser.add_argument("--a", type=float, default=1.0)
perser.add_argument("--b", type=float, default=1.0)
perser.add_argument("--o", type=str, default="add")

args = perser.parse_args()
sys.stdout.write(str(calculator(args)))

