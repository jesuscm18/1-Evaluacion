def cambio_moneda():
    cantidad=input("Cuantos euros quiere cambiar? ")
    moneda=raw_input ("A que moneda desea cambiar? ")
    if(moneda == "dolares"):
        print "Seran "+ str(cantidad*1.15)+ " dolares"
    else:
        if(moneda == "libras"):
            print "Seran "+ str(cantidad*0.88)+ " libras"
        else:
            if(moneda == "yuanes"):
                print "Seran "+ str(cantidad*8.02)+ " yuanes"
            else:
                if(moneda == "rupias"):
                    print "Seran "+ str(cantidad*14614.77)+ " rupias"
                else:
                    if(moneda == "rublos"):
                        print "Seran "+ str(cantidad*76.04)+ " rublos"
                    else:
                        if(moneda == "zlotys"):
                            print "Seran "+ str(cantidad*4.28)+ " zlotys"
                        else:
                            if(moneda == "kunas"):
                                print "Seran "+ str(cantidad*7.41)+ " kuna"
                            else:
                                if(moneda == "karinas"):
                                    print "Seran "+ str(cantidad*0.5)+ " karinas"
                                else:
                                    if(moneda == "pesetas"):
                                        print "Seran "+ str(cantidad*166)+ " pesetas"
                                    else:
                                        if(moneda == "euros"):
                                            print "Seran "+ str(cantidad)+ " euros"
                                        else:
                                            print "No disponemos de esa moneda. Disculpe las molestias"


cambio_moneda()
