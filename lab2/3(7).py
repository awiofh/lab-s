#В компьютер вводятся координаты и точек, лежащих на плоско-сти.
# После ввода координат каждой точки выводить номер квадранта, в котором она находится.
# Определить количество точек, лежащих по отдельности в 1-м и 3-м квадрантах.
quadrant1 = 0
quadrant3 = 0
print("Введите координаты точек, 'exit' для завершения")
while True:
    z = input("Введите координаты (x, y): ")
    if z.lower()== 'exit':
        break
    try:
        x, y = map(float, z.split(','))
    except ValueError:
        print("введите координаты в формате 'x, y'")
        continue
    if x > 0 and y > 0:
        print("точка находится в 1 квадранте.")
        quadrant1 += 1
    elif x < 0 and y < 0:
        print("точка находится в 3 квадранте.")
        quadrant3 += 1
    elif x < 0 and y > 0:
        print("точка находится в 2 квадранте.")
    elif x > 0 and y < 0:
        print("точка находится в 4 квадранте.")
    else:
        print("точка не принадлежит в 1 или 3 квадранту")
print("количество точек в 1 квадранте",quadrant1)
print("количество точек в 3 квадранте",quadrant3)
