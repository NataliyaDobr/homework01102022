# 1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dict(lst):
    some_dict = {}
    some_lst = lst
    for i in range(len(some_lst)):
        some_dict[some_lst[i]]=some_lst[i]
    print(some_dict)

lst = ['surname','name','telephone','adress']
to_dict(lst)
