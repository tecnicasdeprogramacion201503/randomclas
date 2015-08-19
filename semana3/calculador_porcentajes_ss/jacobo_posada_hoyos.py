salario= input("Digite el valor de su salario:")
while salario <0:
	print ""
	print "El salario no puede ser negativo"
	salario= input("Digite el valor de su salario:")

empleado= input("Es usted 1. empleado o 2. independiente:")

while empleado != 1 and empleado != 2 :
	print""
	print "Solo puede escoger 1. o 2."
	empleado= input("Es usted 1. empleado o 2. independiente:")

if empleado == 1:
	print ""
	print "Descuentos:"
	pension=(salario*0.04)
	print "pension:" , (pension)
	salud=(salario*0.04)
	print "salud:" , (salud)

elif empleado == 2:
	print ""
	print "Descuentos:"
	pension=(salario*0.12)
	print "pension:" , (pension)
	salud=(salario*0.085) 
	print "salud:" , (salud)

print ""
print "Su salario neto despues de los descuentos es igual a:" , (salario-pension-salud)
