print                                            "PROGRAMA DE SALARIO "
D=(int( input("Presione: \n 1) Empleado de una empresa  \n 2) Trabajador independiente:  \n ")))
if D == 1: 
	S=(input(" introducir salario  \n"))
##  descuento de salario 
	SA= S*0.085
	print ("descuento salud 8.5%"),SA
	PE= S*0.12
	print ("descuento pension 12%"),PE
	ICBF= S * 0.03
	print ("descuento ICBF 3%"),ICBF
	SENA= S * 0.02
	print ("descuento sena 2%"),SENA
	ST= S-(SA+PE+ICBF+SENA)
	print (" salario total :")
	print int(ST)
if D ==2: 
	S=(input(" introducir salario  \n "))
##  descuento de salario
	SA= S*0.04
	print ("descuento salud 4%"),SA
	PE= S*0.04
	print ("descuento pension 4%"),PE
	print " "
	ST= S-(SA+PE)
	print (" salario total: ")
	print int(ST)

