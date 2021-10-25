# 1 task
from random import randint
value = randint(1, 200)
new_value = int(value / 2) if value < 100 else -(value)
print(value, new_value)
#######################################################
# 2 task
value = randint(1, 200)
new_value = 1 if value < 100 else 0
print(value, new_value)
#######################################################
# 3 task
value = randint(1, 200)
new_value = True if value < 100 else False
print(value, new_value)
#######################################################
# 4 task
my_str = 'exercise'
print(my_str[::2])
#######################################################
# task 5
my_str = 'exercise'
print(my_str[1::2])
#######################################################
# task 6
my_str = 'qwer'
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)
#######################################################
# task 7
my_str = 'qwer'
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)
