def bucle_2():
    print "Iniciando cuenta atras"
    n_inicial=input("Desde que numero desea contar? ")
    n_final=input("Hasta que numero desea contar? ")
    for i in  range(n_inicial, n_final-1,-1):
            print i

bucle_2()
