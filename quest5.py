from functools import reduce

element = [n for n in range(100, 1001) if n % 2 == 0]
sum_all = reduce(lambda x, y: x + y, element)


print(sum_all)