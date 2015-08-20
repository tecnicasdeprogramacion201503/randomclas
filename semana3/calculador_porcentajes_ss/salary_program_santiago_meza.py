# coding=utf-8 
#programa para el calculo del salario neto mensual de un empleado o independiente

print ""
print'          BIENVENIDO AL SISTEMA DE PAGO DE RANDOMCLAS.'
print ""
nombre = raw_input('Hola, Cual es su nombre? ')
print 'hola', nombre + '!'
print ""
t = int(input('Pulse 1 si usted es empleado o pulse 2 si es independiente: '))
print ""
s = float(raw_input('Ingrese su salario bruto mensual: '))
print ""
if t == 1:
	salud =s*0.04
	pension=s*0.04
	prima = s*0.083
	cesantias = s*0.083
	interesescesantias = cesantias*0.12
	vacaciones = s*0.041
	print 'Su salario neto sera igual a su salario bruto' , float("%.f" %s)
	print 'Menos el 4% de salud y el 4% de pension'
	z= s - salud - pension
	print ""
	print 'Su salario neto sera igual a: '
	print z
	print ""
	print 'Ademas cuenta con un promedio acumulado mensual de: '
	print 'Prima, cesantias e intereses sobre estas y vacaciones'
	print 'que podran cancelarse al momento de ser liquidadas'
	print ""
	print 'Prima: '
	print prima
	print 'Cesantias: '
	print cesantias
	print 'Intereses sobre cesantias: '
	print interesescesantias
	print 'Vacaciones: '
	print vacaciones
	x = prima + cesantias + interesescesantias + vacaciones
	print ""
	print 'Que es equivalente a: '
	print x

else:
	salud =s*0.125
	pension =s*0.16
	print 'Su salario neto sera igual a su salario bruto' , float("%.f" %s)
	print 'Menos el 12.5% de salud y el 16% de pension'
	z= s - salud - pension
	print ""
	print 'Salud: '
	print salud
	print 'Pension: '
	print pension
	print ""
	print 'Su salario neto sera igual a: '
	print z
	print ""
print ""
print'           GRACIAS POR PREFERIRNOS.'
print'            QUE TENGA UN BUEN DIA.'
print""
print'                ************'
print'          EL PROGRAMA HA FINALIZADO.'
print'                ************'
raw_input()
