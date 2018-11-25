def factorizador():
    np=1,2,3,5,7,11,13,17,19,23
    #lista de numeros primos
    nd=input("Que numero desea factorizar? ")
    #numero a descomponer
    true=nd>1
    print np
    if(n==nd):
        print "El numero",nd,"es un numero primo"
    else:
        print "El numero",nd,"no es un numero primo"
        rp=raw_input("Quieres factorizarlo? ")
        if(rp=="no"):
            print "Vale, hasta luego"
        else:
            print "Ahora lo haremos..."
factorizador()
