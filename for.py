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

"""
Un Zoólogo pretende determinar el porcentaje de animales que hay en las
siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
de 3 o mas años. El zoológico todavía no está seguro del animal que va
estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
40.  
"""
def porcentaje_animales(elefantes, jirafas, chimpances):
    animal = input('Digite la raza del animal que se va a estudiar: ')
    categoria_uno = 0
    categoria_dos = 0
    categoria_tres = 0
    if(animal == 'elefante'): 
        for valor in range(elefantes):
            edad = int(input(f'Digite la edad {valor + 1}: '))
            if(edad >= 0 and edad <= 1):
                categoria_uno = categoria_uno + 1
                porcentaje_uno = (categoria_uno * 100) / 20
            elif(edad > 1 and edad < 3):
                categoria_dos =  categoria_dos + 1
                porcentaje_dos = (categoria_dos * 100) / 20
            elif(edad >= 3):
                categoria_tres = categoria_tres + 1
                porcentaje_tres = (categoria_tres * 100) / 20
            else:
                print('La edad ingresada no se encuntra entre el rango de edad permitida')
        print(f'El porcentaje de elefantes entre el rango de edad de 0 y 1 años es: {porcentaje_uno}% ')
        print(f'El porcentaje de elefantes entre el rango de edad 1 y 3 años es: {porcentaje_dos}% ')
        print(f'El porcentaje de elefantes entre el rango de edad de 3 ó más años es: {porcentaje_tres}% ')
    if(animal == 'jirafa'):
        for valor in range(jirafas):
            edad = int(input(f'Digite la edad {valor + 1}: '))
            if(edad >= 0 and edad <= 1):
                categoria_uno = categoria_uno + 1
                porcentaje_uno = (categoria_uno * 100) / 15
            elif(edad > 1 and edad < 3):
                categoria_dos = categoria_dos + 1
                porcentaje_dos = (categoria_dos * 100) / 15
            elif(edad >= 3):
                categoria_tres = categoria_tres + 1
                porcentaje_tres = (categoria_tres * 100) / 15
            else:
                print('La edad ingresada no se encuentra entre el rango de edad permitida')
        print(f'El porcentaje de jirafas entre el rengo de edad de 0 y 1 años es: {porcentaje_uno}% ')
        print(f'El porcentaje de jirafas entre el rango de edad de 1 y 3 años es: {porcentaje_dos}% ') 
        print(f'El porcentaje de jirafas entre el rango de edad  de 3 ó más años es: {porcentaje_tres}% ')
    if(animal == 'chimpance'):
        for valor in range(chimpances):
            edad = int(input(f'Digite la edad {valor + 1}: '))
            if(edad >= 0 and edad <= 1):
                categoria_uno = categoria_uno + 1
                porcentaje_uno = (categoria_uno * 100) / 40
            elif(edad > 1 and edad < 3):
                categoria_dos = categoria_dos + 1
                porcentaje_dos = (categoria_dos * 100) / 40
            elif(edad >= 3):
                categoria_tres = categoria_tres + 1
                porcentaje_tres = (categoria_tres * 100) / 40
            
            else:
                print('La edad ingresada no se encuentra entre el rango de edad permitida')
        print(f'El porcentaje de chimpancés entre el rango de edad de 0 y 1 años es: {porcentaje_uno}% ')
        print(f'El porcentaje de chimpancés entre el rango de edad de 1 y 3 años es: {porcentaje_dos}% ')
        print(f'El porcentaje de chimpancés entre el rango de edad de 3 ó más años es: {porcentaje_tres}% ')
porcentaje_animales(20, 15, 40) 

"""    
Una empresa se requiere calcular el salario semanal de cada uno de los n
obreros que laboran en ella. El salario se obtiene de la siguiente forma:
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
b. Si trabaja mas de 40 horas se le paga $20 por cada una de
lasprimeras 40 horas y $25 por cada hora extra.
"""

def salario_trabajador(numero_trabajadores):
    if(numero_trabajadores > 0):
        for valor in range(numero_trabajadores):
            numero_horas = int(input(f'Digite las horas trabajadas del obrero {valor + 1}: '))
            if(numero_horas <= 40):
                total_pagar = numero_horas * 20
                print(f'El salario del obrero es: {total_pagar}')
            elif(numero_horas > 40):
                salario = numero_horas - 40
                total_salario = ((salario * 25) + (20 * 40))
                print(f'El salario total del obrero es de : ${total_salario}')
    else:
        print('El número de obreros digitado esta equivocado')
salario_trabajador(5) 
              


                
    
         
        
        
        
   

