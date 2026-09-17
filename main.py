import numpy
import scipy
import numpy as np


def suma(a, b):
    return a + b



if __name__ == "__main__":
    numero_entero = 1
    numero_float = 1.0
    cadena = "hola"
    nombre= "Pepe"
    edad = 21
    edad_annio_que_viene = suma(edad, 1)

    print(f"La persona {nombre} tiene {edad} años")

    mi_array = numpy.zeros([5,5])
    mi_array[1:3,1:2] = 3


    mi_lista_colores = ["rojo", "verde", "azul"]

    mi_lista_colores.append("amarillo")
    mi_lista_colores.append("violeta")

    for i,mi_color in enumerate(mi_lista_colores):
        print(mi_color)
        print(i)
        print(mi_lista_colores[i])
        if mi_color == "rojo":
            print("hola rojo")
        elif mi_color == "verde":
            print("me gusta el verde")
        else:
            print("otros colores")

    mi_lista_colores[0]
    