# task 1
from collections import defaultdict

persons = [{"name": "John", "age": 15}, {"name": "Sam", "age": 30}, {"name": "Jack", "age": 45}]
youngest_man = defaultdict(list)
longest_name = defaultdict(list)
average_age = []

for i in persons:
    name = i['name']
    age = i['age']
    youngest_man[age].append(name)
    longest_name[len(name)].append(name)
    average_age.append(age)

print(*youngest_man[min(youngest_man)])
########################################
print(*longest_name[max(longest_name)])
########################################
print(sum(average_age) // len(average_age))

###################################################
# task 2
my_dict_1 = {"name": "John", "age": 15}
my_dict_2 = {"name": "Sam", "job": "programmer"}

common_keys = my_dict_1.keys() & my_dict_2
result = my_dict_1.copy()
result.update(my_dict_2)
result.update({key: [my_dict_1[key], my_dict_2[key]] for key in common_keys})
print(list(common_keys))
##############################################################################
my_list = {key: my_dict_1[key] for key in set(my_dict_1) - set(my_dict_2)}
print(list(my_list))
##############################################################################
new_dict = {key: my_dict_1[key] for key in my_dict_1.keys() - my_dict_2}
print(new_dict)
##############################################################################
my_dict_3 = {}

for i in my_dict_1.keys() | my_dict_2.keys():
    if i in my_dict_1:
        if i in my_dict_2:
            my_dict_3[i] = [my_dict_1[i], my_dict_2[i]]
        else:
            my_dict_3[i] = my_dict_1[i]
    else:
        my_dict_3[i] = my_dict_2[i]
print(my_dict_3)










