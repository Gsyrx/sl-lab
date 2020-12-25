from functools import reduce
list = [5, 8, 10] 
sum = reduce(lambda x, y: x + y, list)
print (sum)
