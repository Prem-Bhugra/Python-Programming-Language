"""Program to build a command line utility for faulty calculation of numbers"""
import argparse
import sys
def faucalc(args):
    if args.o == "add" and args.x == 56 and args.y == 9:
        return 77
    elif args.o == "mul" and args.x == 45 and args.y == 3:
        return 55
    elif args.o == "div" and args.x == 56 and args.y == 6:
        return 4
    else:
        if args.o == "add":
            return args.x + args.y
        elif args.o == "sub":
            return args.x - args.y
        elif args.o == "mul":
            return args.x * args.y
        elif args.o == "div":
            return args.x / args.y
        else:
            return "Something went wrong"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type = float, default = 1.0, help = "Please contact Prem")    
    parser.add_argument("--y", type = float, default = 3.0, help = "Please contact Prem")    
    parser.add_argument("--o", type = str, default = "add", help = "Please contact Prem")
    args = parser.parse_args()
    sys.stdout.write(str(faucalc(args)))