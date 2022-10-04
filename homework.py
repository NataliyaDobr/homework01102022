# 1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

# def to_dict(lst):
#     some_dict = {}
#     some_lst = lst
#     for i in range(len(some_lst)):
#         some_dict[some_lst[i]]=some_lst[i]
#     print(some_dict)

# lst = ['surname','name','telephone','adress']
# to_dict(lst)

# 2. Иван решил создать самый большой словарь в мире. 
# Для этого он придумал функцию biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ: значение» 
# и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
# my_dict = {"first_one":"we can do it"}

# def biggest_dict(**kwargs):
#     for key, value in kwargs.items():
#         if key not in my_dict:
#          my_dict[key]=value

# biggest_dict (name="Alex", user="Play", adress="Street")
# print(my_dict)
# biggest_dict (name="Alex", color= "Gray", telephon= "89996663355")
# print(my_dict)

# 3. Дана строка в виде случайной последовательности чисел от 0 до 9. 
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), 
# а в качестве значений – количество этих чисел в имеющейся последовательности. 
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. 
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел. 
import random
import operator
from collections import OrderedDict

def new_str():
    some_str = ''
    for i in range(10):
        some_str = some_str+str(random.randint(1, 10))
    return(some_str) 

def count_it(sequence):
    some_dict = {}
    for i in range(len(sequence)):
        if i not in some_dict:
            some_dict[sequence[i]] = [sequence.count(sequence[i])]

    sorted_tuples = sorted(some_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = OrderedDict()
    for k, v in sorted_tuples:
      sorted_dict[k] = v
      if len(sorted_dict)==3:
        break
    return(sorted_dict)

strr = new_str()
print(strr)
print(count_it(strr))

# 4.Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, 
# в которых фамилия начинается с соответствующей буквы. 
# Например: >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева") 
# { "А": { "П": ["Петр Алексеев"] }, 
#   "И": { "И": ["Илья Иванов"] }, 
#   "С": { "И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"] } }

def thesaurus(*args):
    some_dict = {}
    #some_more_dict = {}
    for i in args:
       surname_letter = i.split()[1][0]
       name_letter = i[0]
       if surname_letter in some_dict:
        if name_letter in some_more_dict:
            some_more_dict[name_letter].append(i)
        else:
            some_more_dict[name_letter] = [i]
       else:
        some_more_dict = {name_letter: [i]}
        some_dict[surname_letter] = some_more_dict
    print(some_dict)

thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
