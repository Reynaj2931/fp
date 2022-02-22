nombre =str(input("cual es tu nombre completo:"));
edad =str(input("cual es edad:"));
grado=int(input("grado:"));
calif=int(input("calificacion del semestre anterio:"));
lg=str(input("donde vives:"));
mr=str(input ("tienes materias reprovadas si o no?"));
print(nombre);
print(edad);
print(grado);
print(calif);
print(lg);
print(mr);
sn= str(input("llena el formulario"));
if sn == "si":
    print("procede la solictud");
else:
    nombre=str(input("cual es tu nombre completo:"));
    edad =str(input("cual es edad:"));
    grado=int(input("grado:"));
    calif=int(input("calificacion del semestre anterio:"));
    lg=str(input("donde vives:"));
    mr=str(input ("tienes materias reprovadas si o no?"));
    if calif >=8:
        print("si te tocara la beca");
    else:
         print("no te tocara la beca");
         mr = str(input("tienes materias reprovadas si o no:"));
         if mr == "si":
            print("no te tocara la beca");	
         else:
            if lg =="pabellon de artega":
                print("no te tocara la beca");
            else:	
                print("si te toco la beca");
                print("has sido seleccionado");