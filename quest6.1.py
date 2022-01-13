from itertools import count

for num in count(3, 0.5):
    if num > 10:
        break
    else:
        print(num)
