def sumar():
    total = 0
    acumulado = 0
    while True:
        a = int(input ('ingrese un numero: '))
        acumulado = a + acumulado
        decision = input('deseas finalizar? si/no: ')
        if decision == 'si':
            break
    total = acumulado
    #print (total)
#sumar()

def sumar_lista(numeros):
    total = 0
    acumulado = 0
    for i in numeros:
        acumulado = i + acumulado
    total = acumulado
    return  total
#sumar_lista([2,6,2])
#print(sumar_lista([2,6,2]))

def test_armar_resultado():
    resultado = sumar_lista([2,6,2])
    assert resultado ==  10