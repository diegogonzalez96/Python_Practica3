def sumNumber(*args):
    result = sum(args)
    print(result)

def function(**kargs):
    text = ''
    for key, value in kargs.items():
        text += key + '=' + value + '/ '
    print(text)

sumNumber(1, 2, 3, 4, 5, 6, 7, 8, 9)
function(nombre='fulanito', apellido='menganito', sexo='masculino')
