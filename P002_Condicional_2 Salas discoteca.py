def condicional_2():
    edad=input("Cual es tu edad? ")
    if(edad>=18):
        print "Sala alcoholica"
    else:
        if(edad>=15):
            print "Sala adolescentes" 
        else:
            print "Sala infantil" 

condicional_2()
