from functools import reduce

def operacion(operador, *args, **kwargs):
    text = ''
    if operador == '+':
        result = sum(args)
    if operador == '*':
        result = reduce((lambda x,y: x*y), args)
    for key, value in kwargs.items():
        text += key + ' = ' + value + ' /'

    print('La operacion solicitada fue {}, el resultado es: {} por {}'.format(operador, result, text))

operacion('+', 3, 4, 5, 6, 7, nombre='Diego', apellido='Gonzalez', edad='21', direccion='Av. Siempre Viva')
