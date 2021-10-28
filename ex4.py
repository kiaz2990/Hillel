# task 1
my_list = [50, 110, 80, 140, 90, 170]
for value in my_list:
    if value > 100:
        print(value)

###################################################
# task 2
my_list = [50, 110, 80, 140, 90, 170]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

###################################################
# task 3
my_list = [80, 140, 60]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

###################################################
# task 4
my_string = '0123456789'
my_list = []
for val_1 in my_string:
    for val_2 in my_string:
        my_list.append(int(val_1 + val_2))
print(my_list)
