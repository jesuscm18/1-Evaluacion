def tabla_multiplicar_while():
    tabla=input("Que tabla de multiplicar quieres que haga? ")
    i=input("Desde que numero desea comenzar a multiplicar? ")
    f=input("En que numero desea finalizar su tabla? ")
    while (i<f+1):
        print str(tabla)+ " x "+ str (i)+" = "+ str (tabla*i)
        i=i+1    

tabla_multiplicar_while()
