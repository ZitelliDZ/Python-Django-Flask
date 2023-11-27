


try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregamos Info.\n')
    archivo.write('asd')
except Exception as e:
    print(e)
finally:
    archivo.close()



try:
    archivo = open('prueba.txt', 'r')
    print(archivo.read(4))
    print(archivo.read(4))
    print(archivo.readline())
    print(archivo.readline())

    archivo.close()
    archivo = open('prueba.txt', 'r')

    print('_________________________')
    for linea in archivo:
        print(linea)

    print('_________________________')

    archivo.close()
    archivo = open('prueba.txt', 'r')
    print(archivo.readlines())
    archivo.close()
    archivo = open('prueba.txt', 'r')
    print(archivo.readlines()[0])

    archivo.close()
    archivo = open('prueba.txt', 'r')
    # archivo2 = open('copy.txt','w')
    archivo2 = open('copy.txt','a')
    for linea in archivo:
        archivo2.write(linea+'\n')

except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
