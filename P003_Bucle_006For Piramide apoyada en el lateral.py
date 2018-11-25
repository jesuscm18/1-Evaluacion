def piramide():
    print"***********************"
    print"*CONSTRUYE TU PIRAMIDE*"
    print"***********************"
    h=input("De cuantos pisos deseas tu piramide? ")
    if(h<99):
        for fil in range(1,h+1):
            for col in range(1,fil+1):
                print"X",
            print " "
    else:
        print "No puedo hacer una piramide tan grande"
piramide()
