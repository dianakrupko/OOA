import sys

print(sys.argv)
arguments = sys.argv[1:]
try:
    a = int(arguments[0])
    b = str(arguments[1])
    c = int(arguments[2])
    print('Result: ', eval(str(a) + b + str(c)))
except ZeroDivisionError:
    print("Error. Division by zero")
except:
    print("Error. Incorrectly entered data")
