##examen de programacion
##desarrolar un programa que guarde todos los integrantes del grupo como objetos co los siguientes atributos:edad,calificacion de las diferentes materias ,promedios ,calificacionde la preparatoria.
##reyna yamile calzada campos

class alumno():
    def __init__(self,Edad,cald,fprog,fundi,talle,ingles,calpr,lugarr,distancia):
        
        self.Edad=Edad
        self.cald=cald
        self.fprog=fprog
        self.fundi=fundi
        self.talle=talle
        self.ingles=ingles
        self.calpr=calpr
        self.lugarr=lugarr   
        self.distancia=distancia


johana=alumno(18,8,9,10,9,10,8,"jesus maria",28)
fernando=alumno(17,9,9,8,10,7,10,"pabellon de arteaga",8)
britzi=alumno(18,8,9,7,9,10,9,"rincon de romos", 14)
melani=alumno(18,9,10,8,9,9,10,"pabellon de arteaga",8)
sharlene=alumno(18,9,8,9,8,9,10,"cosio",30)
alejandro=alumno(19,9,8,9,9,10,9,"rincon de romos",14)
paola=alumno(18,9,9,8,9,10,9,"carboneras tepezala",16)
alexis=alumno(19,9,8,9,10,8,7,"rincon de romos",14)
arely=alumno(18,8,8,9,7,9,10,"rincon de romos",14)
diego=alumno(19,8,8,9,8,10,9,"rincon de romos",15)
isaac=alumno(19,9,9,10,9,9,10,"rincon de romos",14)
donaldo=alumno(18,9,8,10,9,8,9,"pabellon de arteaga",8)
austin=alumno(19,8,9,10,8,9,10,"pabellon de arteaga",8)
alain=alumno(19,8,9,8,7,10,9,"pabellon hidalgo",18)
reyna=alumno(17,8,9,10,9,10,8,"emiliano zapata ",6)




print ("ingenierias tics primer semestre")
opcion = 0
while True:
    print("""
    ¿Qué deseas mirar?
    
    a) Los 5 alumnos con mayor edad  
    b) Promedio de todos en la preparatoria 
    c) Alumnos que viven mas lejos y mas cerca
    d) Materia con mejor rendimiento
    e) Salir
    """)

    opcion = int(input("decide una opción: ") )     
    if opcion == 1:
    	print(" ")
    	print("fernando con ",fernando.Edad,"Años de edad")
    	print("alexis con ",alexis.Edad,"Años de edad")
    	print("diego con ",diego.Edad,"Años de edad")
    	print("areli con ",arely.Edad,"Años de edad")
    	print("isaac con ",isaac.Edad,"Años de edad")

    elif opcion == 2:
        print(" ")
        print("Calificaciones de los alumnos de la preparatoria: ")
        print(isaac.calpr, paola.calpr, alejandro.calpr, diego.calpr,britzi.calpr, austin.calpr,donaldo.calpr,reyna.calpr,alain.calpr)
        print(alexis.calpr, melani.calpr, fernando.calpr, johana.calpr,sharlene.calpr)
        print ("El promedio es de: 8.9")
    
    elif opcion == 3:
        print(" ")
        print("El alumno mas que vive mas lejos es sharlene en",sharlene.lugarr,"Distancia: ",sharlene.distancia)
        print ("El alumno mas cercano son fernando en",fernando.lugarr,"y melani",melani.lugarr,"Con:",fernando.distancia)
    elif opcion == 4:
         print(" ")
         print("La materia con mayor promedio en taller de etica es: ")
         print(melani.talle, britzi.talle, johana.talle, alexis.talle, isaac.talle, reyna.talle, austin.talle, donaldo.talle)
         print("promedio sumatorio es: 9.6")
    elif opcion == 5:
        break
    else:
        print("Opción error")