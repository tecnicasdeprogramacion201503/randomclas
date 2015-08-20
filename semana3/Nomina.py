#Melqui Camacho Espitia
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

print ""
print "                       LIQUIDADOR DE SALARIO NETO"
print ""
i=raw_input("Ingrese 1 si es empleado o 2 si es independiente: ")
print ""
I=raw_input("Ingrese salario bruto: ")
print ""
if (int(i) == 1):
          p=float(I)*4/100
          print "Descuento por pension: ", float("%.2f" %p)
          s=float(I)*4/100
          print "Descuento por salud: ", float("%.2f" %s)
          c=float(I)*8.33/100
          print "Descuento por cesantias: ", float("%.2f" %c)
          v=float(I)*4.2/100
          print "Descuento por vacaciones: ", float("%.2f" %v)
          pr=float(I)*4.2/100
          print "Descuento por prima: ", float("%.2f" %pr)
          n=float(I)-p-s-c-v-pr
          print "(valores dados en pesos)"
          print ""
          print "Su salario neto es: ", float("%.2f" %n)
else:
          pi=float(I)*16/100
          print "Descuento por pension: ", float("%.2f" %pi)
          si=float(I)*12.5/100
          print "Descuento por salud: ", float("%.2f" %si)
          ci=float(I)*12/100
          print "Descuento por cesantias: ", float("%.2f" %ci)
          vi=float(I)*8.33/100
          print "Descuento por vacaciones: ", float("%.2f" %vi)
          pri=float(I)*8.33/100
          print "Descuento por prima: ", float("%.2f" %pri)
          ni=float(I)-pi-si-ci-vi-pri
          print "(valores dados en pesos)"
          print ""
          print "Su salario neto es: ", float("%.2f" %ni)