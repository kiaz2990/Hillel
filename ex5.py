# task 1
my_int = 10500
my_res = str(my_int)
print(my_res.count('0'))
###################################################
# task 2
my_int = 10500
my_str = str(my_int)
my_res = len(my_str) - len(str(int(my_str[::-1])))
print(my_res)
###################################################
# task 3
my_list_1 = ['ho', 1, 'me', 3]
my_list_2 = [0, 'wo', 2, 'rk']
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)
###################################################
# task 4
my_list = ['rk', 'ho', 'me', 'wo']
new_list = my_list[1:] + my_list[0:1]
print(new_list)
###################################################
# task 5
my_list = ['rk', 'ho', 'me', 'wo']
print(id(my_list))
my_list.append(my_list.pop(0))
print(id(my_list), my_list)
###################################################
# task 6
my_str = "25 35 45 55"
my_sum = sum(int(value) for value in my_str.split(' ') if value.isdigit())
print(my_sum)
###################################################
# task 7
my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
i1 = my_str.find(l_limit)
i2 = my_str.rfind(r_limit)
sub_str = my_str[i1 + 1: i2]
print(sub_str)
###################################################
# task 8
my_str = "qwertyu"
result = []
for index, value in enumerate(my_str):
    if index % 2 == 0:
        couple = my_str[index:index + 2]
        if len(couple) > 1:
            result.append(couple)
        else:
            result.append(value + "_")
print(result)
###################################################
# task 9
my_list = [3, 5, 2, 6, 4, 10, 1, 8]
my_res = sum([my_list[i-1] < my_list[i] > my_list[i+1] for i in range(1, len(my_list)-1)])
print(my_res)
