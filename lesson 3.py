#1
from linecache import cache

print(int(-1.6), int(2.99))

#2

print("www.my_site.com#about".replace("#", "/") )

#3

print("stroka".__add__("ing"))

#or

print("stroka"+"ing")

#4

a=1
b=2

a,b=b,a
print(a,b)

print("Ivanou Ivan".split(" "))
a="Ivanou Ivan".split(" ")
a.reverse()
print(a)
print(a[0] + " " + a[1])

#5

def probely(stroka):
    stroka.replace(" ","")

    if stroka.startswith(" "):
        return stroka[1:]
    else:
        return stroka

#print(probely(" some generated text "))
print(" some generated text ".strip())

#6 создайте словарь связав с переменной school и наполните данными с количеством уч в 10 разн классах

a = [['1b',15],['2b',14],['3a',18],['4a',33],['5a',13],['6b',23],['7a',22], ['8c',26],['9b',19],['10a',33]]
school =dict(a)
print(school)

#7 созд список и извлеките 2 эл

shoppinglist = ['cola','sugar','banana']
print(shoppinglist[1])

#8

stroka1='develop'
stroka2='development'
print(stroka1 in stroka2)

#9
x='My name is Agent Smith'
print(x[1]) #y
print(x[3:16:3]) #nesgt

#10

mylist=[1,5,2,9,2,9,1]
#mylist2=[1,5,2,9,2,9,1,5,4]

def unique(mylist):
    cache= set()

    for elem in mylist:
        #print(elem)
        if not elem in cache:
            cache.add(elem)
        else:
            cache.discard(elem)

    return cache.pop()


print(unique(mylist))
