#programa para el gasto de salario de una persona independiente o empleada mensual
print""
nombre= raw_input("ingrese su nombre: ")
print""
print(nombre + ',con este programa podra calcular el total de su salario mensual legal\n    ')
z = input('ingrese su salario    ')
print ''
t = int(input('empleado (pulse 1) o independiente (pulse 2)  \n  ' ))
print""
#para empleado
if t ==1:
#deducciones
 salud =int (z*0.04)
 pension=int (z*0.04)
 #prestaciones sociales
 prima = int (z*0.083)
 cesantias = int (z*0.083)
 interesescesantias = int (cesantias*0.12)
 vacaciones = int (z*0.041)
 print('su salario ' + nombre + ' corresponde al de un empleado.')
 print("sus deducciones correspondes a las siguientes:")
 print""
 print("salud 4%")
 print salud
 print""
 print 'pension 4%'
 print pension
 print""
 print("sus prestaciones corresponden a las siguientes:")
 print""
 print("prima ")
 print prima
 print""
 print"cesantias"
 print cesantias
 print ""
 print"intereses cesantias"
 print interesescesantias
 print ""
 print "vacaciones"
 print vacaciones
 print""
 print(nombre + ' por lo tanto el dinero que le queda libre mensual es')
 salario = z - salud - pension + prima + cesantias + interesescesantias + vacaciones
 print salario
#para independiente
else:
 #deducciones
 salud =int (z*0.125)
 pension = (z*0.16)
 ica = int (z*0.01)
 honorarios = (z*0.1)
 #prestaciones (no posee)
 print("sus deducciones correspondes a las siguientes:")
 print""
 print"salud 12.5%"
 print salud
 print""
 print("pension 16%")
 print pension
 print""
 print('ICA 1%')
 print ica
 print""
 print('honorarios 10%')
 print honorarios
 print""
 print (nombre + " usd por ser independiente no cuenta con prestaciones.")
 print""
 print("por lo tanto el dinero que le queda libre mensual es")
 salario = z - salud - pension - ica - honorarios
 print salario
 print""
print('                EL PROGRAMA A FINALIZADO')