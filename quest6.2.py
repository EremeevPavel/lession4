from itertools import cycle

x = 0
for push in cycle(['При', 'вет!']):
    if x > 11:
        break
    print(push)
    x += 1