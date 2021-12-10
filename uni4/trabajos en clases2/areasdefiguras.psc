Algoritmo areasdefiguras
	definir opc Como Entero
	Definir triangulo,cuadradro,circulo,rectangulo Como Real
	Escribir "poner la opcion de la figura"
	Escribir "0:calcular area del cuadradro"
	Escribir"1:calcular area del triangulo"
	Escribir "2:calcular area del circulo"
	Escribir "3:calcular area del rectangulo"
	leer opc
	Segun opc Hacer
		0:
			Escribir "area del cuadrado"
			Escribir"pon el lado"
			leer l
			cuad <- l * l
			Escribir "el area es: ",cuad 
			
	     1:
			 Escribir "area del triangulo"
			 Escribir "pon la base"
			 leer b
			 Escribir "pon la altura"
			 leer h
			 triangulo <-(b * h) / 2
			 Escribir "area es:", triangulo
	     2:
			 Escribir "area del circulo"
			 Escribir "pon el radio"
			 leer r
			 circulo<-pi*r^2
			 Escribir "el area es :", circulo
			
		 3:
			 Escribir "area del rectangulo"
			 Escribir "pon la base"
			 leer b
			 Escribir "pon la altura"
			 leer h
			 rectangulo<-(b * h)
		     Escribir "area es :", rectangulo
				 De Otro Modo:
					 Escribir "opcion invalida"
			
	Fin Segun
FinAlgoritmo
