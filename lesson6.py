# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
#
# Вывести первый, второй, предпоследний и последний элементы данного файла.
# Если чисел меньше 3 выводить ошибку


file = open("zadanie1.txt")
array = file.read().split(",")

def print_elem(array):
    if len(array)<3:
        print("error!!!")
        return None
    else:
        print(array[0],array[1],array[-2],array[-1])

print_elem(array)

#
# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
#
# содержит четные числа из исходного файла, а второй — нечетные (в том же порядке). Если четные или нечетные числа в исходном файле
#
# отсутствуют, то соответствующий результирующий файл оставить пустым.

file0 = open("zadanie2.txt","r")
file1 = open("zadanie2_1.txt","w")
file2 = open("zadanie2_2.txt","w")

array0 = file0.read().split(",")
#array_4etnyje = file1.write(",".join(array0))
array_4etnyje = [] #массив объявляется пустым

#array_nie4etnyje = file2.write(",".join(array0))
array_nie4etnyje =[]


for i in array0:
    if int(i) % 2 == 0:
        array_4etnyje.append(i)
    else:
        array_nie4etnyje.append(i)

file1.write(",".join(array_4etnyje))
file2.write(",".join(array_nie4etnyje))

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

file3 = open("zadanie3.txt","r")
array3 = file3.read().split(",")
array_kvadratov = []

for i in array3:
    array_kvadratov.append(str(float(i)**2))

file3 = open("zadanie3.txt","w")
file3.write(",".join(array_kvadratov))


# 4 Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа

file4 = open("zadan4.txt","wb")
file4.write(b"proizwolnyj fail")

file5 = open("zadan5.txt","wb")
file5.write(b"proizwolnyj fail 2 ")


file4 = open("zadan4.txt","rb")
a1 = file4.read()

file5 = open("zadan5.txt","rb")
a2 = file5.read()

file4 = open("zadan4.txt","wb")
file5 = open("zadan5.txt","wb")

file4 = file4.write(a2)
file5 = file5.write(a1)
