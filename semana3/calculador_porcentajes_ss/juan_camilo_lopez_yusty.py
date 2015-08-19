while True:
	try:
		salario = int(raw_input('Ingrese el salario que desea tener, use el punto para separar decimales: '))
		break
	except ValueError:
		print("\nIngreso mal el salario.\nPor favor ingrese un valor numerico sin comas o letras.\n")

while True:
	print "\nUsted es: \n	1)Trabajador independiente \n	2)Empleado en una empresa"
	empre_ind = raw_input("Ingrese 1 o 2 segun corresponda su categoria: \n	")
	if empre_ind == "1":
		salud = salario*0.125
		pension = salario*0.16
		prestad = salud + pension
		libreEmpleado = salario - prestad
		print "\nA usted le queda libre para gastar, un total de: $", str(libreEmpleado),"\n\nDebe paraga en prestaciones un total de: $",str(prestad)
		print "Las prestaciones descontadas son:\n	Salud: $",str(salud),"\n	Pension: $",str(pension)
		break
	elif empre_ind== "2":
		salud = salario * 0.04
		pension = salario*0.04
		icbf = salario*0.03
		sena = salario*0.02
		prestad = salud + pension + icbf + sena
		libreEmpleado = salario - prestad
		print "\nA usted le queda libre para gastar, un total de: $", str(libreEmpleado), "\n\nDebe pagar en prestaciones, deducciones y paraficasles, un total de: $",str(prestad)
		print "Las prestaciones, deducciones y parafiscales son:\n	Salud: $",str(salud),"\n	Pension: $",str(pension),"\n	ICBF: $",str(icbf),"\n	Sena: $",str(sena)
		break
	else:
		print "\nEl valor ingresado fue incorrecto. \nIngrese 1 o 2, segun corresponda su categoria."
