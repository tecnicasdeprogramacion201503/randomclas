x=input('salario quedesea ganar:')
print '1: independiente'
print '2: Empleado-empresa'
y=input('ingrese el tipo de epleado:')

while y > 2:
			print ('Valor intreducido es erroneo')
			print '1: independiente'
			print '2: Empleado-empresa'
			y=input('ingrese el tipo de epleado:')
if y == 1:
	print 'Empleado independiente'
	pension= (x*0.16)
	salud= (x*0.125)
else:
	print 'Empleado dependiente'
	pension=(x*0.04)
	salud= x*0.04


print ''
print 'su salario quedaria en:'
print 'descuento en salud:' , salud
print 'descuento en pension:' , pension
print 'salario neto:' , x-salud-pension

