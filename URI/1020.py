x = int(input())

a = x % 365
b = a % 30

A = int(x/365)
B = int(a/30)
C = int(b)

print("%i ano(s)" % A)
print("%i mes(es)" % B)
print("%i dia(s)" % C)