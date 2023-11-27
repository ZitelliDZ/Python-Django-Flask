from disenio_clases.numeros_identicos_exception import NumerosIdenticosException
resultado = None
try:
    a = int(input('Primer numero:'))
    b = int(input('Seg numero:'))
    if a == b:
        raise NumerosIdenticosException('Numeros iguales')
    resultado = a / b
except ZeroDivisionError as e:
    print('Error:',e)
    print(type(e))
except Exception as e:
    print('Error:',e)
    print(type(e))
else:
    print('No hubo ningun error')
finally:
    print('siempre')
print('Resultado:',resultado)
