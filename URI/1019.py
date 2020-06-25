N = int(input())

a = N % 3600
b = a % 60

A = int(N/3600)
B = int(a/60)
C = int(b)

print("%i:%i:%i" % (A,B,C))