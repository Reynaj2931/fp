Algoritmo examendelaunidad5
	Definir opciones Como Real
	Escribir "menu"
	Escribir "eligen la opcion 1"
	Escribir "elige la opcion 2"
	Escribir "elige la opcion 3"
	Escribir " salir"
	leer opciones 
	Segun opciones Hacer
		1 :
			Escribir "introduce tu nombre:"
			leer nombre
		2:
	        Escribir "calcula los dias de vidas que tengas segun tus años:"
			leer años
	     3:
			 Escribir "cual es tu calificacion del semestre"
			 leer calificacion 
			 Si  calificacion < 7 Entonces
				 Escribir "esta reprovado"
				 

					SiNo
					 Escribir "estas aprovado"
					fin si
				
			
					 De Otro Modo:
						 Escribir"no se encuentra esa opcion"
						
				 Fin Segun
FinAlgoritmo
