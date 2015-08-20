S=0
M=0
int(S)
float(M)

M=float(raw_input("Ingrese su salario Mensual"))
S=M*4/100
print "Descuento por salud: ", int(S)

P=M*4/100
print "Descuento por pension: ", int(P)

O=M*8.3/100
print "Descuento por cesantias", int(O)


N=M-S-P-O
print "Su salario neto como empleado es: ", N

G=M*14/100
print "Descuento por pension", int(G)

U=M*8.5/100
print "Descuento por salud", int(U)

I=M-G-U
print "Su salario neto como empleador es: ", I


