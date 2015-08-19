tipo = input ("Ingrese 1 si es independiente o 2 si es empleado: ")
while tipo != 1 and tipo != 2:
	print "Ingrese solo 1 o 2"
	tipo = input ("Ingrese 1 si es independiente o 2 si es empleado: ")
sal = float(input("Ingrese el salario: "))
while sal < 0:
	print "Ingrese un valor positivo"
	sal = float(input("Ingrese el salario: "))
if tipo == 1:
	print "Salud: ", 0.125*sal
	print "Pension: ", 0.16*sal
	print "Salario neto: ", sal-(0.125*sal)-(0.16*sal)
else:
	print "Salud: ", 0.04*sal
	print "Pension: ", 0.04*sal
	print "Salario neto: ", sal-(0.04*sal)-(0.04*sal)
