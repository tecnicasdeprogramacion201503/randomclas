print                                            "PROGRAMA CALCULADORA DE SUELDO"
T=(int( input("Presione 1 si empleador o 2 si es empleado: ")))
if T == 1: 
	SN=(input(" introducir sueldo neto"))
## calculos de descuentos de salario neto
	DPS= SN*0.085
	print ("descuento por salud 8.5%"),DPS
	DPP= SN*0.12
	print ("descuento por pension 12%"),DPP
	DICBF= SN * 0.03
	print ("descuento por ICBF 3%"),DICBF
	DSENA= SN * 0.02
	print ("descuento por sena 2%"),DSENA
	SG= SN-(DPS+DPP+DICBF+DSENA)
	print ("su sueldo general es:")
	print int(SG)
if T ==2: 
	SN=(input(" introducir sueldo neto"))
## calculos de descuentos de salario neto
	DPS= SN*0.04
	print ("descuento por salud 4%"),DPS
	DPP= SN*0.04
	print ("descuento por pension 4%"),DPP
	print " "
	SG= SN-(DPS+DPP)
	print ("su sueldo general es: ")
	print int(SG)