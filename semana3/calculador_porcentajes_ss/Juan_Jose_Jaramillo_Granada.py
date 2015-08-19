# Programa para calcular prestaciones de servicios en Colombia 2015

print ""
print "CALCULADORA DE PRESTACIONES DE SERVICIOS"
print ""

salario = int(raw_input('Ingrese un salario para calcular su descuento de prestaciones: '))
condicion = str(raw_input('Desea trabajar como independiente(I) o como empleado(E)?: '))
print "\n"

if condicion=='E':
	print 'Su aporte a salud y pension es de 4% respectivamente ya que su empresa aporta un 8,5% de salud y un 12% de pension'
	print 'Su aporte a cesantias es de un 8.6% cuyos intereses sobre el sueldo total son de 0.089% y de un 8.6% para la prima de junio'
	descuento = int(salario*(0.08+0.086+0.0089+0.086))
else:
	print 'Su aporte a salud es de 12,5% y pension es de un 16%'
	descuento = int(salario*0.125)

salario = salario-descuento

print "\n"
print 'Le quedan libres para gastar', '$'+str(salario)
print 'En prestaciones se le van', '$'+str(descuento)