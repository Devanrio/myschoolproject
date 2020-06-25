a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior = (a+b+abs(a-b))/2
maior2 = (maior+c+abs(maior-c))/2
print("%i eh o maior" % maior2)