

from sys import argv
script_name, first_zp, second_zp = argv
x = float(first_zp)
y = float(second_zp) * 0.05
z = x + y


print("Имя скрипта: ", script_name)
print("Оклад: ", x)
print("Оборот: ", y)
print("Итого: ", str(z))