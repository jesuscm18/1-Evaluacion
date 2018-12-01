def discoteca():
    sumaper=0
    while(sumaper<=10):
        e=input("Cuantos años tienes? ")
        if(sumaper>10):
            print "El aforo esta lleno"
        else:
            if(e>=18):
                print "Perfecto, adelante"
                sumaper=sumaper+1
            if(sumaper>=10):
                print "El aforo esta lleno"
            else:
                print "Vete a tu casa, no puedes entrar"
            
        
    

discoteca()
