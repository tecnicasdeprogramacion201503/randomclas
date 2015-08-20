print""
print"                        CALCULO DEL COSTO REAL SALARIO"
print""

EL=int(input("Ingrese 1 si uste es empleado, ingrese 2 si usted es independiente"))
S=float(input("ngrese su salario:"))

if EL == 1:
 DSA= S*0.085
 DP= S*0.12
 AUX= float(75000)
 DICBF= S*0.03
 DSENA= S*0.02
 print("Descuento por salarioalud:"),float(DSA)
 print("Descuento por pension:"),float(DP)
 print("Auxilio de transporte:"),AUX
 print("Descuento por ICBF:"),float(DICBF)
 print("Descuento por SENA"),float(DSENA)
 ST = S-(DSA+DP+AUX+DICBF+DSENA)
 print ("Su salario real es:"),float(ST)
 
else El == 2:
 DSA=float(input("Cuanto paga de seguro medico:"))
 DP=float(input("Cuanto cotiza de pension:"))
 ST=S+DSA+DP
 print("su salario real es:"),float(ST)


 