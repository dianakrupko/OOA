import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action", type=str)
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)
args = parser.parse_args()
print(args)


def add(a, b):
    print(a + b)


def mul(a, b):
    print(a - b)


def sub(a, b):
    print(a * b)


def div(a, b):
    if b != 0:
        print(a / b)
    else:
        print("Error")


if args.action == "add":
    add(args.a, args.b)
elif args.action == "mul":
    mul(args.a, args.b)
elif args.action == "sub":
    sub(args.a, args.b)
elif args.action == "div":
    div(args.a, args.b)
