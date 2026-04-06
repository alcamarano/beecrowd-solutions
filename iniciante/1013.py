a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
MaiorAB = (a+b+abs(a-b))/2
if (MaiorAB > c):
    print("{:.0f} eh o maior".format(MaiorAB))
else:
    print("{:.0f} eh o maior".format(c))