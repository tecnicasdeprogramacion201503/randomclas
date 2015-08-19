print 'Software para el calculo de la nomina salarial, by HAROLD ESTEBAN BOLANOS'
print '   '
salario=raw_input ('Escriba su salario (Puede ser el deseado) : ')

print 'Su salario ingresado fue : ',salario,'C.O.P.'
print '   '

x=raw_input('Calcular para empleado o independiente? :')
if x=='empleado' or x=='EMPLEADO':
	print 'Su salario seleccionado fue EMPLEADO'
	print ' '
	print 'Los descuentos legales para los contratos de vinculacion laboral son los siguientes :'
	esalud=float(salario)*0.04
	esaludempresa=float(salario)*0.085
	print '  '
	print 'SEGURIDAD SOCIAL'
	print '  '
	print 'SALUD: Corresponde a un aporte mensual del 4% de su salario.  Total : ',int(esalud),' C.O.P'
	print 'La empresa correspondiente proporciona el 8.5% restante ',int(esaludempresa),' C.O.P. para un total del 12.5%'
	epension=float(salario)*0.04
	epensionempresa=float(salario)*0.12
	print 'PENSION: Corresponde a otro aporte mensual del 4% de su salario. Total : ',int(epension),' C.O.P'
	print 'La empresa correspondiente proporciona el 12% restante ',int(epensionempresa),' C.O.P. para un total del 16%'
	print '  '
	print 'CARGOS PRESTACIONALES'
	print '  '
	ecesantias=float(salario)*0.0833
	print 'CESANTIAS: Corresponde a un aporte mensual del 8.33% de su salario. Total : ',int(ecesantias),' C.O.P.'
	eprima=float(salario)*0.0833
	print 'PRIMA DE SERVICIOS: Corresponde a un aporte mensual del 8.33% de su salario. Total : ',int(eprima),' C.O.P.'
	evaca=float(salario)*0.0417
	print 'VACACIONES: Correspondea un aporte mensual del 4.17% de su salario. Total : ',int(evaca),' C.O.P.'
	print '  '
	print '  '
	print '													GASTOS TOTALES '
	total=int(esalud+epension+ecesantias+evaca)
	restante=int(float(salario)-total)
	print '										GASTOS POR NOMINA: ',total,' C.O.P.'
	print '										SALARIO LIBRE DE NOMINA: ',restante,' C.O.P.'
	
	
else:
	print 'Su salario seleccionado fue INDEPENDIENTE'
	print ' '
	print 'Los descuentos legales para los contratos de vinculacion laboral son los siguientes :'
	isalud=float(salario)*0.12
	print '  '
	print 'SEGURIDAD SOCIAL'
	print '  '
	print 'SALUD: Corresponde a un aporte mensual del 12% de su salario.  Total : ',int(isalud),' C.O.P'
	ipension=float(salario)*0.16
	print 'PENSION: Corresponde a otro aporte mensual del 16% de su salario. Total : ',int(ipension),' C.O.P'
	print '  '
	print 'CARGOS PRESTACIONALES'
	print '  '
	icesantias=float(salario)*0.0833
	print 'CESANTIAS: Corresponde a un aporte mensual del 8.33% de su salario. Total : ',int(icesantias),' C.O.P.'
	iprima=float(salario)*0.0833
	print 'PRIMA DE SERVICIOS: Corresponde a un aporte mensual del 8.33% de su salario. Total : ',int(iprima),' C.O.P.'
	ivaca=float(salario)*0.0417
	print 'VACACIONES: Correspondea un aporte mensual del 4.17% de su salario. Total : ',int(ivaca),' C.O.P.'
	print '  '
	print '  '
	print '													GASTOS TOTALES '
	total2=int(isalud+ipension+icesantias+ivaca)
	restante2=int(float(salario)-total2)
	print '										GASTOS POR NOMINA: ',total2,' C.O.P.'
	print '										SALARIO LIBRE DE NOMINA: ',restante2,' C.O.P.'
