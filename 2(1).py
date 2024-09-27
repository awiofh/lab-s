#определить средний рост девочек и мальчиков одного класса. В классе учится n учеников
list1 = []
list2 = []
averageboy = 0
averagegirl = 0
print('введите кол-во учеников')
n = int(input())
boy = 0
girl = 0
for x in range(0,n):
    y = (input('мальчик или девочка?'))
    if (y == "мальчик"):
        boy += 1
        print('рост')
        x = float(input())
        list1.append(x)
    else:
        girl +=1
        print('рост')
        z = float(input())
        list2.append(z)
averageboy = sum(list1)/len(list1)
averagegirl = sum(list2)/len(list2)
print("средний рост мальчиков=",round(averageboy,2))
print("средний рост девочек=",round(averagegirl,2))
print('кол-во девочек=',girl)
print('кол-во мальчиков=',boy)
