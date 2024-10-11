#Дан одномерный массив с размером 10 и два числа P и Q (P<Q)
#Определить, сколько элементов массива заключено между P и Q.
n= 10
l = 0
list1= []
count = 0
p = float(input('введите число P'))
q = float(input('введите число Q'))
print('введите 10 чисел массива')
while(l<n):
    try:
        y = float(input())
    except ValueError:
        l+=1
        n+=1
        continue
    list1.append(y)
    l+=1
for i in range(0,len(list1)):
    if p < list1[i] < q:
        count +=1
    else:
        continue
print(count)
