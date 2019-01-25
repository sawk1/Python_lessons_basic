# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

b = input ('введите список продуктов через пробел: ').split()
spisok = [i for i in range(0,len(b))]
for i in spisok:
    print ('{}. {:>20}'.format(spisok[i], b[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = input('введите любые значения через пробел: ').split()
spisok2 = input('введите любые значения через пробел: ').split()
i = 0
while i<=(len(spisok1)):
    n = 0
    while n<=(len(spisok2)-1):
        if not spisok1:
            break
        else:
            if spisok1[i-1] == spisok2[n]:
                p = spisok1[i-1]
                spisok1.pop(i-1)
                #print('i = ', i, 'n = ', n, spisok1, 'удаленный элемент: ', p) #видим какие эллементы удалены
                i =0
        n = n+1
    i = i + 1
print(spisok1)

#2й вариант с применением for

spisok1 = input('введите любые значения через пробел: ').split()
spisok2 = input('введите любые значения через пробел: ').split()
for i in spisok1:
    for n in spisok2:
        if not spisok1:
            break
        else:
            if i == n:
                k = spisok1.index(i)
                spisok1.pop(k)
print(spisok1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

spisok1 = input('введите произвольный список из целых чисел: ').split()
spisok2 = spisok1
i = 0
a = 0
while i<len(spisok1):
    a = int(spisok1[i])
    if a%2==0:
        spisok2[i] = a/4
    else:
        spisok2[i] = a*2
    i = i+1
print (spisok2)

#2й вариант с применением for

spisok1 = input('введите произвольный список из целых чисел: ').split()
spisok2 = []
for i in spisok1:
    i = int(i)
    if i%2==0:
        a = i/4
        spisok2.append(a)
    else:
        a = i*2
        spisok2.append(a)
print (spisok2)