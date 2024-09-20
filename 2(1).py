#вычислить сумму s= cosx+(cos2x)/(2**2)+...+(cosnx)/(n**2)+...
#суммирование прекратить, когда очередной член суммы по модулю будет меньше e = 0.0001
import math
x= float(input())
e= 0.0001
n=1
s=0
z = (math.cos(n*x))/(n**2)
while(math.fabs(z) >= e):
    z = (math.cos(n * x)) / (n ** 2)
    s= s+z
    n += 1
    print('сумма=',s,'последний член последовательности по модулю =',math.fabs(z))
else:
    print(s)