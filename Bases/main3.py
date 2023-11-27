from disenio_clases.producto import Producto
from disenio_clases.order import Order
from disenio_clases.empleado import Empleado
from disenio_clases.gerente import Gerente

producto1 = Producto('Reloj',300.0)
producto2 = Producto('Pulsera',120.0)
producto3 = Producto('Elastico',10.0)

productos = [producto1,producto2,producto3]
productos = list(productos)
orden1 = Order(productos)
orden2 = Order(productos)

print(orden1)
productos.append(producto3)
orden2.agregar_producto(producto2)
print(orden2)

print(orden2.calcular_total())


# sobrecarga de operadores

a = 1
b = 2
print(a + b)
a = 'Hola '
b = 'Mundo'
print(a + b)

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    def __add__(self, other):
        return self.__nombre+' - '+other.nombre
class Persona2:
    def __init__(self, nombre):
        self.nombre = nombre
    def __add__(self, other):
        return self.nombre+' - '+other.__nombre

p1 = Persona('Juan')
p2 = Persona2('Diego')

print(p1 + p2)

print('_________________________')
def imprimir_detalle(obj):
    print(obj)
    print(type(obj))
    if isinstance(obj,Gerente):
        print(obj.departamento)

empleado = Empleado('Juan',1000.0)
imprimir_detalle(empleado)
empleado = Gerente('Juan',1000.0,'Misiones')
imprimir_detalle(empleado)

