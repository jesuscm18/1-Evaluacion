def tabla_de_multiplicar_2():
    n_tabla=input("Que tabla deseas que haga? ")
    i=input("Hasta que numero desea multiplicar? ")
    for i in range(0,i+1):
        print str(n_tabla)+ " x "+ str(i) +" = "+ str(n_tabla*i)

tabla_de_multiplicar_2()
