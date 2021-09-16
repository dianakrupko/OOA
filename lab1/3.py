Sign = {'+', '-'}
Number = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


def check(index):
    if (
            (expression[index - 1] in Sign and expression[index] == '0' and expression[index + 1] in Number) or
            (expression[index - 1] in Sign and expression[index] in Sign) or
            (expression[index] not in Number and expression[index] not in Sign)):
        return False, None
    if index == len(expression) - 1:
        return True, eval(expression)
    return check(index + 1)


expression = str(input())
lenght = len(expression)
if (expression == "") or (expression[0] in Sign) or (expression[lenght - 1] in Sign):
    print((False, None))
    exit(1)
print(check(0))
