import timeit
import random
import os

with open('myFileNum.txt', "w") as myNumber:
    while os.path.getsize("myFileNum.txt") <=50*1048576:
        line = str(random.randint(1, 10)) + "\n"
        myNumber.write(line)
        n = line.strip()


s = """
sumNums = 0
with open ("myFileNum.txt","r") as nums:
    data=nums.readlines()
    for line in data:
        if line.strip().isdigit():
            sumNums+=int(line.strip())
"""
print(timeit.timeit(s, number=10))


s = """
sumNums = 0
with open ("myFileNum.txt","r") as nums:
 for line in nums:
    if line.strip().isdigit():
        sumNums+=int(line.strip())
"""
print(timeit.timeit(s, number=10))

s = """
sumNums = 0
with open ("myFileNum.txt","r") as nums:
  sumNums = sum(int(line.strip()) for line in nums if line.strip().isdigit())
"""
print(timeit.timeit(s, number=10))
