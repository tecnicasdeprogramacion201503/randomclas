x=raw_input('Cual es su nombre?')
print 'hola' +' '+ x +'!'
y=raw_input('usted es empleado o independiente?') 
#print x +' '+'es' + ' ' + y
z=raw_input('gana mas de dos salarios mensuales? si o no')
#print x + ' '+ z + 'gana mas de dos salarios`mensuales'
q=raw_input('Cuanto es su salario?')
print x + ' ' + 'gana' + ' ' + q

if (y=='empleado'):
    salud=float(q)*0.4
    pension=float(q)
    salario=float(q) - pension
    
    print x + ' ' + 'como ganas menos de dos salarios mensuales tienes derecho a un subsidio de transporte'
else:
    print x + ' '+ 'se jodio'
        
