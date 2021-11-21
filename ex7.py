# task 1
my_list_1 = ['one', 'two', 'three', 'four', 'five', 'six']


def ret_nl(my_list_1):
    new_list_1 = []
    for index, item in enumerate(my_list_1):
        if index % 2 != 0:
            new_list_1.append(item[::-1])
        else:
            new_list_1.append(item)
    return new_list_1


print(ret_nl(my_list_1))
########################################################################
# task 2
my_list_2 = ['dell', 'apple', 'hp', 'asus', 'lenovo', 'xiaomi']


def a_bg(my_list_2):
    new_list_2 = [item for item in my_list_2 if item[0].startswith('a')]
    return new_list_2


print(a_bg(my_list_2))
########################################################################
# task 3
my_list_3 = ['dell', 'apple', 'hp', 'asus', 'lenovo', 'xiaomi']


def a_in(my_list_3):
    new_list_3 = [*filter(lambda item: 'a' in item, my_list_3)]
    return new_list_3


print(a_in(my_list_3))
########################################################################
# task 4
my_list_4 = [1, 'two', 3, 'four', 5, 'six']


def only_str(my_list_4):
    new_list_4 = [item for item in my_list_4 if isinstance(item, str)]
    return new_list_4


print(only_str(my_list_4))
########################################################################
# task 5
my_str_1 = 'exercise number seven'


def sin_sym(my_str_1):
    new_list_5 = [item for item in my_str_1 if my_str_1.count(item) == 1]
    return new_list_5


print(sin_sym(my_str_1))
########################################################################
# task 6
my_str_2 = 'exercise'
my_str_3 = 'number seven'


def sing_symb(my_str_2, my_str_3):
    new_list_6 = list(set(my_str_2).intersection(set(my_str_3)))
    return new_list_6


print(sing_symb(my_str_2, my_str_3))
########################################################################
# task 7
my_str_4 = 'exercise'
my_str_5 = 'number seven'


def sing_symb_2(my_str_4, my_str_5):
    new_list_7 = [item for item in my_str_4 if my_str_5.count(item) == 1 and my_str_4.count(item) == 1]
    return new_list_7


print(sing_symb_2(my_str_4, my_str_5))
########################################################################
# task 8
names = ["petrov", "sidorov", "ivasev", "stepanov"]
domains = ["net", "com", "ua"]


def rand_mail(names, domains):
    import random
    random_number = str(random.randint(100, 999))
    random_word = ''.join(chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(5, 7)))
    email = random.choice(names) + "." + random_number + "@" + random_word + "." + random.choice(domains)
    return email


print(rand_mail(names, domains))
