# Задание 5го урока:
# - цель: продемонстрировать понимание, что такое функция, как ее создавать и использовать/запускать
# - необходимо для 3го или 4го ДЗ обернуть задачи в функции
# - достаточно будет написать 3-4 функции. Обратите внимание, что функции должны что-то возвращать,
# то есть в конце иметь return <РЕЗУЛЬТАТ>. Иначе от функции будет мало смысла, она должна выполнить работу и вернуть значения

#from lesson 3
#2

#print("www.my_site.com#about".replace("#", "/") )

def replace(string):
    string = string.replace("#", "/")
    return string

print(replace("www.my_site.com#about"))



#print("stroka"+"ing")

def add_ing(string):
    string = string + "ing"
    return string

print(add_ing("cry"))


#8
# stroka1='develop'
# stroka2='development'
# print(stroka1 in stroka2)

def check_string_in_string(string1, string2):

    return string1 in string2

print(check_string_in_string("develop","development" ))


#from lesson 4
#3
# myname = "Olga"
# a=f"my name is {myname}"
# print(a)

def generate_string(name):
    name = f"my name is {name}"
    return name

print(generate_string("Alexey"))