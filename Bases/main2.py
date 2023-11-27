# from modules import modulo_aritmetica as arit
import modules.modulo_aritmetica as arit
from modules.modulo_aritmetica import Aritmetica

from abc import ABC, abstractmethod

print('Hola Mundo')
# Variables
miVariable: str = 'Hola'
print(miVariable)
# miVariable = 2
# print(miVariable)
miVariable: str = 'Hola'
print(miVariable)

false = False

x: int = 10
y: int = 2
z: int = x + y
print(z)
print(type(z))
print(type(miVariable))
print(type(false))

xx: float = 10.0
print(type(xx))

##############
miGrupo: str = 'Metallica' + ' ' + 'asdnakls'
print(miGrupo + ' ' + 'asdasiiioio')
print('asid:', miGrupo + ' ' + 'asdasiiioio')
print(type(miGrupo))
#############
numero1: str = '1'
numero2: str = '2'
print('Concatenacion: ', numero1 + numero2)
print('Suma: ', int(numero1) + int(numero2))
#############
bandera: bool = 3 < 2
print(bandera)

if bandera:
    print('Verdadero')
else:
    print('Falso')

# resultado1: str = input('Escribe un numero: ')
# resultado2: int = int(input('Escribe un numero: '))
# print(int(resultado1) + resultado2)
# resultado3 = int(resultado1) + resultado2
# print(f'El resultado es: {resultado3} .')

# and, or, not
# >, <, ==, <=, >=, !=
# +, -, *, **, /, //, %
############
if bandera:
    print()
elif bandera:
    print()
else:
    print()
############
i: int = 1
while i < 10:
    print(f'1: {i}')
    i += 1
else:
    print('fin while')

print('fin')

############
cadena = 'Hola Diego'

for letra in cadena:
    print(letra)
    if letra == 'e':
        break
else:
    print('Fin For')

for i in range(20):
    print(f'Valor i: {i}')
    continue

###########
# Listas

nombres = ['Juan', 'Carla', 'Ricardo', 0, 100, True]
print(nombres)
print(nombres[1])
print(nombres[-2])
print(nombres[1:2])
print(nombres[1:3])
print(nombres[1:])
nombres[1] = 'Maria'
print(nombres)
print(nombres[1])
print(nombres[-2])
print(nombres[1:2])
print(nombres[1:3])
print(nombres[1:])
print(len(nombres))
nombres.append('Pepe')
print(nombres)
nombres.pop(1)
print(nombres)
nombres.insert(1, 'Pepe')
print(nombres)
# nombres.remove('Pepe')
# print(nombres)
del nombres[0]
print(nombres)
nombres.clear()
print(nombres)
# del nombres
# print(nombres)


# Tuplas
frutas = ('Naranjas', 'Manzanas', 'Bananas')
print(frutas)
print(frutas[1])
print(len(frutas))
frutaList = list(frutas)
frutaList[1] = 'asd'
frutas = tuple(frutaList)
print(frutas)

for fruta in frutas:
    print(fruta, end=' ')

# Set
planetas = {'Martes', 'Tierra', 'Venus'}
print(planetas)
print('Tierra' in planetas)
print(len(planetas))
planetas.add('Jupiter')
print(planetas)
planetas.add('Jupiter')
print(planetas)
planetas.remove('Jupiter')
print(planetas)
planetas.discard('Jupiter')
print(planetas)
planetas.clear()
print(planetas)
del planetas

# Diccionario
diccionario = {
    'IDE': 'hola',
    'OOP': 'Object',
    'asd': {
        'name': 'asd',
        'edad': 123
    }
}

print(diccionario)
print(diccionario['asd'])
print(diccionario.get('asd'))
diccionario['IDE'] = {
    'name': 'asd',
    'edad': 123
}
print(diccionario)
print(len(diccionario))

for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(diccionario[termino])
for valor in diccionario.values():
    print(valor)

print('IDE' in diccionario)

diccionario['pp'] = {
    'name': 'asd',
    'edad': 123
}
print(diccionario)
diccionario.pop('IDE')
print(diccionario)
diccionario.clear()
print(diccionario)


# Funciones
def miFunction(nombre: str = 'asd'):
    print('Holla', nombre)


miFunction('Diego')
miFunction()


# Clases
class Persona:
    name: str
    apellido: str
    edad: int

    def __init__(self, name: str, apellido: str, edad: int):
        self.name = name
        self.apellido = apellido
        self.edad = edad


Persona.name = 'Diego'
Persona.apellido = 'Zitelli'
Persona.edad = 30
print(Persona)
print(Persona.name)
print(Persona.apellido)
print(Persona.edad)

persona1 = Persona('Mariela', 'Ortellado', 26)
print(persona1.name)
print(persona1.apellido)
print(persona1.edad)
print(id(persona1))
print(id(Persona))


class Persona2:
    __name: str
    __apellido: str
    __edad: int

    def __init__(this, *v, **d):
        this.__name = v[0]
        this.__apellido = v[1]
        this.__edad = v[2]
        this.__diccionario = d

    def desplegar(this):
        print('Nombre:', this.__name)
        print('apellido:', this.__apellido)
        print('edad:', this.__edad)
        print('diccionario:', this.__diccionario)

    def get_nombre(self):
        return self.__name

    def set_nombre(self, name):
        self.__name = name
        return


p1 = Persona2('a1111sd', 'asd', 2, m='asd', p='oo', j='jj')
p1.desplegar()
print(p1.get_nombre())
p1.set_nombre('ooooooos')
print(p1.get_nombre())


class Persona3:
    name: str
    _ape_materno: str
    __ape_paterno: str
    __edad: int

    def __init__(this, nombre, ape_materno, ape_paterno, edad):
        this.name = nombre
        this._ape_materno = ape_materno
        this.__ape_paterno = ape_paterno
        this.__edad = edad

    def print(self):
        self.__desplegar()
        return

    def __desplegar(this):
        print('name:', this.name)
        print('_ape_materno:', this._ape_materno)
        print('__ape_paterno:', this.__ape_paterno)
        print('__edad:', this.__edad)


p2 = Persona3('Diego', 'Solonezen', 'Zitelli', 30)
p2.print()


class Persona4:
    __name: str
    __edad: int

    def __init__(this, nombre, edad):
        this.__name = nombre
        this.__edad = edad

    def print(self):
        self.__desplegar()
        return

    def __desplegar(this):
        print('name:', this.__name)
        print('__edad:', this.__edad)

    def get_nombre(self):
        return self.__name

    def set_nombre(self, nombre):
        self.__name = nombre
        return


p4 = Persona4('Diego', 30)
p4.print()
print('________________________')


class Empleado(Persona4):
    __salario: float

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.__salario = salario

    def print(self):
        super().print()
        print(self.__salario)

    def __str__(self):
        super().print()
        print(self.__salario)


p5 = Empleado('Diego', 30, 35.5)
p5.print()
print('________________________')
# print(p5)
print('________________________')

aritmetica = arit.sumar(50, 50)
print(aritmetica)

clase = Aritmetica(50, 40)
print(clase.sumar())

print('________________________')

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto


class Color:
    def __init__(self, color):
        self.color = color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    def area(self):
        return self.alto*self.ancho

cuadrado = Cuadrado(5,'red')
print(cuadrado.area())
print(Cuadrado.mro())


print('________________________')


class FiguraGeometrica2(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @abstractmethod
    def area(self):
        pass


class Color2:
    def __init__(self, color):
        self.color = color


class Cuadrado2(FiguraGeometrica2, Color2):
    def __init__(self, lado, color):
        FiguraGeometrica2.__init__(self, lado, lado)
        Color2.__init__(self, color)
    def area(self):
        return self.alto*self.ancho

cuadrado2 = Cuadrado2(25,'red')
print(cuadrado2.area())
print(Cuadrado2.mro())



print('________________________')

class MiClase:
    variable_clase = 'Variable de clase'

    def __init__(self, variable_de_instancia):
        self.variable_de_instancia = variable_de_instancia

mi_clase = MiClase('hola')
mi_clase2 = MiClase('hola2')
print(MiClase.variable_clase)
mi_clase.variable_clase = 'sda'
print(MiClase.variable_clase)
print(mi_clase.variable_clase)
print(mi_clase2.variable_clase)



print('________________________')

class MiClase2:

    variable_clase = 'Variable de clase'

    def __init__(self, variable_de_instancia):
        self.variable_de_instancia = variable_de_instancia
    @staticmethod
    def metodo_Statico():
        print('Statico method')
        print(MiClase2.variable_clase)
        # No se puede acceder a variable_de_instancia

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        # No se puede acceder a variable_de_instancia

    def metodo_instancia(self):
        self.metodo_Statico()
        self.metodo_clase()



MiClase2.metodo_Statico()
MiClase2.metodo_clase()
print('________________________')
obj = MiClase2('asd')
obj.metodo_instancia()



print('________________________')
# from constantes import *
# from constantes import MI_CONSTANTE
# from constantes import Matematicas as mate

MI_CONSTANTE = 'Hola'
print(MI_CONSTANTE)

class Matematicas:
    PI = 3.1416
Matematicas.PI = 33.3
print( Matematicas.PI)