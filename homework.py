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
my_dict = {"first_one":"we can do it"}

def biggest_dict(**kwargs):
    for key, value in kwargs.items():
        if key not in my_dict:
         my_dict[key]=value

biggest_dict (name="Alex", user="Play", adress="Street")
print(my_dict)
biggest_dict (name="Alex", color= "Gray", telephon= "89996663355")
print(my_dict)