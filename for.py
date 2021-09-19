# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 13:20:22 2021

@author: Usuario
"""
"""
El departamento de Seguridad de Transito de Barranquilla, desea saber de
los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
color. Conociendo el último digito de la placa de cada automóvil se puede
determinar el color de la calcomanía utilizando la siguiente relación:
"""

def numero_auto(cantidad_autos):
    color_amarillo = 0
    color_rosa = 0
    color_rojo = 0
    color_verde = 0
    color_azul = 0
    for valor in range(cantidad_autos):
        digito_placa = int(input(f'Digite el ultimo digito de la placa {valor + 1}: '))
        if(digito_placa == 1 or digito_placa == 2):
           color_amarillo = color_amarillo + 1
        elif(digito_placa == 3 or digito_placa == 4):
            color_rosa = color_rosa + 1
        elif(digito_placa == 5 or digito_placa == 6):
            color_rojo = color_rojo + 1
        elif(digito_placa == 7 or digito_placa == 8):
            color_verde = color_verde + 1
        elif(digito_placa == 9 or digito_placa == 0):
            color_azul = color_azul + 1 
        else:
            print('El numero ingresado en equivocado')
    print(f'Los carros ingresados con calcomanía amarilla: {color_amarillo}')
    print(f'Los carros ingresados con calcomanía rosa: {color_rosa}')
    print(f'Los carros ingresados con calcomanía roja: {color_rojo}')
    print(f'Los carros ingresados con calcomanía verde: {color_verde}')
    print(f'Los carros ingresados con calcomanía azul: {color_azul}')
numero_auto(12)

    
