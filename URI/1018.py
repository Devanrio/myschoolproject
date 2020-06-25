N = int(input())

a = N % 100
b = a % 50
c = b % 20
d = c % 10
e = d % 5
f = e % 2
g = f % 1

A = int(N/100)
B = int(a/50)
C = int(b/20)
D = int(c/10)
E = int(d/5)
F = int(e/2)
G = int(f/1)

print(N)
print("%i nota(s) de R$ 100,00" % A)
print("%i nota(s) de R$ 50,00" % B)
print("%i nota(s) de R$ 20,00" % C)
print("%i nota(s) de R$ 10,00" % D)
print("%i nota(s) de R$ 5,00" % E)
print("%i nota(s) de R$ 2,00" % F)
print("%i nota(s) de R$ 1,00" % G)