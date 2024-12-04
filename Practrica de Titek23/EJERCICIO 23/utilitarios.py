def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

def calcularSubtotal(val1,val2,val3):
    subtotalSinDescuento =val1*val2
    porcentajeDescuento = subtotalSinDescuento*val3 /100
    subtotal = subtotalSinDescuento - porcentajeDescuento
    return subtotal

def calcularValorDescuento(val1,val2):
    valorDescuento = val1*val2
    calculardescuento = valorDescuento / 100
    return calculardescuento

<<<<<<< HEAD
def consultarMulta(tipomMulta):
    if tipomMulta == 1:
        return 10/100*100
    elif tipomMulta == 2:
        return 15/100*100
    elif tipomMulta == 3:
        return 20/100*100
    elif tipomMulta == 4:
        return 30/100*100
    else:
        return -1
=======
def calcularValorHora(salario):
    resultado=salario*160
    return resultado
>>>>>>> 73743633695a1b63c14a7494a34da131e71546ac
