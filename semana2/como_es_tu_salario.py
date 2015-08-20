print'  '
print'  '
print'  '
print '        SALARIO DESEADO MENOS LA COTIZACION DE NEGOCIO INDEPENDIENTE'
print' '
salario=raw_input ('Escriba aqui su salario deseado:')
print' '
x=raw_input('Calcular para empleado o empleador?:')
if x=='empleado':
	print' '
	print'Necesitamos saber de que nivel son sus riesgos laborales'
	print'  '
	print'  '
	y=raw_input('Sus riesgos laborales son de nivel 1,2,3,4 o 5?:')
	if y=='1':
		print'  '
		print'Usted escojio empleado independiente y riesgo nivel uno:'
		h=float(salario)*0.04
		k=float(salario)-((h)*2)
		r1=float(salario)*0.00522
		r2=float(salario)*0.01044
		print'   '
		print'-Salud 4%:',h
		print'   '
		print'-Pension 4%:',h
		print'   '
		print'-Riesgos laborales 0.522%:',r1
		print'  '
		print'   Estos porcentajes seran retirados de su salario total entonces'
		print'    '
		print'         SU SALARIO A GANAR MENOS LA COTIZACION ES DE:'
		print'  '
		print'                         ',(k-r1)
	if y=='2':
			h2=float(salario)*0.04
			k2=float(salario)-((h2)*2)
			r2=float(salario)*0.01044
			print'  '
			print'Usted escojio empleado independiente y riesgo nivel dos:'
			print'   '
			print'-Salud 4%:',h2
			print'   '
			print'-Pension 4%:',h2
			print'   '
			print'-Riesgos laborales 1.044%:',r2
			print'  '
			print'   Estos porcentajes seran retirados de su salario total entonces'
			print'    '
			print'         SU SALARIO A GANAR MENOS LA COTIZACION ES DE:'
			print'  '
			print'                         ',(k2-r2)
	if y=='3':
				h3=float(salario)*0.04
				k3=float(salario)-((h3)*2)
				r3=float(salario)*0.02436
				print'  '
				print'Usted escojio empleado independiente y riesgo nivel tres:'
				print'   '
				print'-Salud 4%:',h3
				print'   '
				print'-Pension 4%:',h3
				print'   '
				print'-Riesgos laborales 2.436%:',r3
				print'  '
				print'   Estos porcentajes seran retirados de su salario total entonces'
				print'    '
				print'         SU SALARIO A GANAR MENOS LA COTIZACION ES DE:'
				print'  '
				print'                         ',(k3-r3)
	if y=='4':
					h4=float(salario)*0.04
					k4=float(salario)-((h4)*2)
					r4=float(salario)*0.0435
					print'  '
					print'Usted escojio empleado independiente y riesgo nivel cuatro:'
					print'   '
					print'-Salud 4%:',h4
					print'   '
					print'-Pension 4%:',h4
					print'   '
					print'-Riesgos laborales 4.35%:',r4
					print'  '
					print'   Estos porcentajes seran retirados de su salario total entonces'
					print'    '
					print'         SU SALARIO A GANAR MENOS LA COTIZACION ES DE:'
					print'  '
					print'                         ',(k4-r4)
	if y=='5':
						h5=float(salario)*0.04
						k5=float(salario)-((h5)*2)
						r5=float(salario)*0.696
						print'  '
						print'Usted escojio empleado independiente y riesgo nivel cinco:'
						print'   '
						print'-Salud 4%:',h5
						print'   '
						print'-Pension 4%:',h5
						print'   '
						print'-Riesgos laborales 6.96%:',r5
						print'  '
						print'   Estos porcentajes seran retirados de su salario total entonces'
						print'    '
						print'         SU SALARIO A GANAR MENOS LA COTIZACION ES DE:'
						print'  '
						print'                         ',(k5-r5)
if x=='empleador':

	print'Usted escojio empleador independiente,se le descontara lo siguiente:'
	sal=float(salario)*0.085
	pen=float(salario)*0.12
	sen=float(salario)*0.02
	ic=float(salario)*0.03
	cc=float(salario)*0.04
	total=float(salario)-(pen+sal+sen+ic+cc)
	print' '
	print'-Aportes de salud 8.5%:',sal
	print' '
	print'-Pension 12%:',pen
	print'  '
	print'-SENA 2%:',sen
	print' '
	print'-ICBF 3%:',ic
	print' '
	print'-Caja de compensacion 4%:',cc
	print' '
	print'         SU SALARIO A GANAR MENOS LA COTIZACION ES DE:'
	print'  '
	print'                         ',(total)
