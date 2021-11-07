
running = True
while running:
    Promedio1 = float(input('Ingresa tu promedio: '))
    Pro = float(Promedio1)
    if Pro >= 6 :
        print('Felicidades,aprobado.')
       
        running = False
    elif Pro < 6:
        print('esfuerzate mas,reprobado')
else:
    print('El semestre while ha terminado.')
    

print('Fin')