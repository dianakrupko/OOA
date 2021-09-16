import sys

print(sys.argv)
arguments = sys.argv[1:]
a = int(arguments[0])
b = str(arguments[1])
c = int(arguments[2])
print('Result: ', eval(str(a) + b + str(c)))
