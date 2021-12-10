Algoritmo calculadora 
	Definir opci Como Entero
	Definir suma ,resta,multiplicacion,division Como Real
	Escribir "poner la opcion de la operacion"
    Escribir"1:para hacer una suma"
	Escribir"2:para hacer una resta"
	Escribir"3:para hacer una multiplicacion"
	Escribir"4:para una division"
	leer opci
	Segun opci Hacer
	     1:
			 Escribir"ingresa el primer numero"
			 leer pn1
			 Escribir"ingrese el segundo numero"
			 leer sn2
			 s<-pn1+sn2
			 Escribir "la suma es:",s
			
		2:
			Escribir "ingresa el primer numero"
			leer pn1
			Escribir"ingresa el segundo numero"
			leer sn2
			r<-pn1-sn2
			Escribir "la resta es:",r
		3:
			Escribir"ingresa el primer numero"
			leer pn1
			Escribir"ingresa el segundo numero"
			leer sn2
			m<-pn1*sn2
			Escribir "la multiplicacion es:",m
			
			4:
				Escribir"ingresa el primer numero"
				leer pn1
				Escribir"ingresa el segundo numero"
				leer sn2
				d<-pn1/sn2
				Escribir "la division es :",d
				De Otro Modo:
					Escribir "opcion invalida"
			Fin Segun
		
		
	
FinAlgoritmo
