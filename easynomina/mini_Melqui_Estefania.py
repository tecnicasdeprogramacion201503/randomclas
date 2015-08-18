import sys
longi=len(sys.argv)
print "el numero de argumentos es" ,longi
i=0
I=0
p=0
s=0
c=0
v=0
pr=0
n=0


if (longi != 3):
	i=float(raw_input("Ingrese 1 si es empleado o 2 si es independiente: "))
	I=float(raw_input("Ingrese salario bruto: "))
else:
	i=int(sys.argv[1])
	I=float(sys.argv[2])

#descuentos asalariado
#pension	4
#salud	4
#cesantias	8.33
#vacaciones		4.2
#prima	4.2

#descuentos independiente
#pension  16
#salud    12.5
#cesantias          12
#vacaciones         8.33
#prima              8.33

#prima =  float(8.333)*3.44
#print float("%.2f" %prima)

print ""
print "                       LIQUIDADOR DE SALARIO NETO"
print ""
#i=raw_input("Ingrese 1 si es empleado o 2 si es independiente: ")
print ""
#I=raw_input("Ingrese salario bruto: ")
#I=float(I)
print ""
if (int(i) == 1):
          p=I*4/100
          print "Descuento por pension: ", float("%.2f" %p)
          s=I*5/100
          print "Descuento por salud: ", float("%.2f" %s)
          c=I*8.33/100
          print "Descuento por cesantias: ", float("%.2f" %c)
          v=I*4.2/100
          print "Descuento por vacaciones: ", float("%.2f" %v)
          pr=I*4.2/100
          print "Descuento por prima: ", float("%.2f" %pr)
          n=I-p-s-c-v-pr
          print "(valores dados en pesos)"
          print ""
          print "Su salario neto es: ", float("%.2f" %n)
else:
          p=I*16/100
          print "Descuento por pension: ", float("%.2f" %p)
          s=I*12.5/100
          print "Descuento por salud: ", float("%.2f" %s)
          c=I*12/100
          print "Descuento por cesantias: ", float("%.2f" %c)
          v=I*8.33/100
          print "Descuento por vacaciones: ", float("%.2f" %v)
          pr=I*8.33/100
          print "Descuento por prima: ", float("%.2f" %pr)
          n=I-p-s-c-v-pr
          print "(valores dados en pesos)"
          print ""
          print "Su salario neto es: ", float("%.2f" %n)
		  
outfile = open('salida.txt', 'w') # Indicamos el valor 'w'.
mensajesalud="salud="+str(s)
print mensajesalud
outfile.write(mensajesalud)
outfile.write(',')
mensajepension="pension="+str(p)
print mensajepension
outfile.write(mensajepension)
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('salida.txt', 'r')
print('>>> Escritura de fichero concatenando su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()
