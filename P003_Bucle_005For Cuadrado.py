def piramide():
    print"***********************"
    print"*CONSTRUYE TU CUADRADO*"
    print"***********************"
    altura=input("Cuanto quieres que mida el lado de tu cuadrado? ")
    if(altura<99):
        for fil in range(1,altura+1):
            for col in range(1,altura+1):
                print"X",
            print " "
    else:
        print "No puedo hacer una piramide tan grande"
piramide()
