print""
print"                        CALCULO DEL SALARIO REAL OBTENIDO"
print""
I=input("Salario ofertado: ")
print ""
print "Seleccione:  \n 1.Trabajador independiente \n 2.Empleado de una empresa \n "
n=input ("Ingrese la opcion de acuerdo a su caso: ")
print""
R=0.10*I
Rn=0.11*I
S= 0.02*I
Ic=0.03*I
Cc=0.04*I
C=0.0833*I
P=0.0833*I
V=0.0417*I
In=0.01*I
Se=0.04*I
Sem=0.085*I
Pe= 0.064*I
Pem=0.12*I
if n == 1:
	print "Seleccione  \n 1.Es declarante \n 2.No es declarante \n"
	k=input("Ingrese la opcion de acuerdo a su caso: ")
	print""
	if n == 1:
		print "  Retencion por honorarios", 0.10*I
	elif n == 2:
		print"  Retencion por honorarios", 0.11*I
	print "  Salud: " ,0.04*I
	print "  Pension: ", 0.064*I
	print""
	print "Usted recibira por salario : ", I-R-Rn-Se-Pe,"pesos."
elif n == 2:
	print "  Aportes  parafiscales"
	print "    Sena: " , 0.02*I
	print "    ICBF: ", 0.03*I
	print "    Cajas de Compensacion Familiar: " , 0.04*I
	print "  Cargas prestacionales"
	print"    Cesantias: ", 0.0833*I
	print"    Prima de servicios: ", 0.0833*I
	print"    Vacaciones: ", 0.0417*I
	print"    Intereses sobre las Cesantias: ", 0.01*I , "mensual"
	print "  Seguridad social"
	print"    Salud: ", 0.085*I
	print"    Pension:  ",0.12*I
	print""
	print "Usted le cuesta a la empresa : ", I+S+Ic+C+P+V+In, "pesos"
	print""
	print "Usted recibira por salario : ", I-Sem-Pem-In-Cc, "pesos" 
else:
	print "Solo puede ingresar las opciones 1 y 2."