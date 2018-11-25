def piramide():
    h=input("De que altura quieres que haga la piramide? ")
    for i in range(h+1):
        x=(2*i)-(i-1)
        v=h-i
        #vacio
        print " "*v + " X"*x

piramide()
