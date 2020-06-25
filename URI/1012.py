A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
n = 3.14159
TRIANGULO = (A*C)/2
CIRCULO = n*(C**2)
TRAPEZIO = ((A+B)*C)/2
QUADRADO = B*B
RETANGULO = A*B
print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)