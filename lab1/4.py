capacity = int(input("Maximum capacity of the backpack: "))  # integer describing the capacity of a knapsack
weights = input("Weight of gold bars: ").split()  # list of weights of each gold bar
stuffdict = {}


def getValues():
    val = [int(item) for item in weights]
    return val


def createTable(stuffdict, capacity):
    value = getValues()
    length = len(value)
    table = [[0 for a in range(capacity + 1)] for i in range(length + 1)]
    for row in range(length + 1):
        for col in range(capacity + 1):
            if row == 0 or col == 0:
                table[row][col] = 0
            elif value[row - 1] <= col:
                table[row][col] = max(value[row - 1] + table[row - 1][col - value[row - 1]],
                                      table[row - 1][col])
            else:
                table[row][col] = table[row - 1][col]
    return table, value


def getResult(stuffdict, func, capacity):
    matrix, area = func(stuffdict, capacity)
    length = len(area)
    res = matrix[length][capacity]
    return res


result = getResult(stuffdict, createTable, capacity)
print('Maximum weight of gold that fits into a knapsack with capacity of', capacity, '-', result)
