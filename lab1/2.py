import argparse
import operator

func = {"add": operator.add,
        'mull': operator.mul,
        'sub': operator.sub,
        'div': operator.truediv
        }
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", type=str)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    print(args)

    print(func[args.action](args.a, args.b))
except ZeroDivisionError:
    print("Error. Division by zero")
except:
    print("Error. Incorrectly entered data")
