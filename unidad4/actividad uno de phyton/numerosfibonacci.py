###el programa pedira los numerosque se sumaron de los numeros fibonacci
##reyna yamile calzada campos 
###actividad 1 unidad 4

n=int(input('dame un numero:'))
def fibonacci_iter(n):
 	a=1
 	b=1
 	if n == 1:
 	    print('0')
 	elif n==2:
 	     print('0','1')
    else:
 	    print('0')
 	    print(a)
 	    print(b)
 	    for i in range(n-3):
 	    	    total = a + b
 	    	    b=a
 	    	    a=total
 	    	    print(total)
fibonacci_iter(n)
