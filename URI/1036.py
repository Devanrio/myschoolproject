import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
try:
	bhaskara1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
	bhaskara2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
	print("R1 = %.5f"% bhaskara1)
	print("R2 = %.5f"% bhaskara2)
except:
	print("Impossivel calcular")