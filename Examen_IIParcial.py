# -*- coding: utf-8 -*-
# Programa: Examen_IIParcial
# Objetivo: Control de estacionamiento segun el tipo de vehiculo
# Repositorio: https://github.com/LuisBauti/examen-Multiplataforma/tree/develop
# Autor: Luis Enrique COnsuegra Bautista
# Fecha: 13/03/2020

import sys
import os
import platform
class automovil(self):
    """Se encarga de la funcionalidad del ingreso y cobro 
       del aparcamento"""

    self.vehiculo = list()
    sel.options = {"1", self.agregar_vehiculo,
                   "2", self.buscar_vehiculo,
                   "3",self.reporte,
                   "4", self.close}



class Menu(self):
    """Muestra las opciones para las acciones que se pueden realizar
       dentro del programa"""
    
    print("""
            Control de Estacionamiento
            1. Agregar un nuevo vehiculo

            2. Crear tiket
            3. Ver reporte
            4. Salir""")

def continuar(self):
    """Realiza una pausa y solicita una tecla"""
    imput("\Presione enter para continuar")

def agregar_vehiculo(self)
    """Agregar un nuevo vehiculo"""

    self.vehiculo.append(
        imput("Ingrese el tipo de vehiculo")
    )

