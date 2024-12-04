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

def calcularValorHora(salario):
    resultado=salario*160
    return resultado