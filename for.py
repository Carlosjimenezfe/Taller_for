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

"""   
Calcular el promedio de edades de hombres, mujeres y de todo un grupo
de alumnos
"""   

def total_grupo(total_grupo, hombres, mujeres):
    promedio_grupo = 0
    promedio_hombres = 0
    promedio_mujeres = 0
    for valor in range(total_grupo):
        edad_alumno = int(input(f'Digite la edad del alumno {valor + 1}: '))
        sexo_alumno = input(f'Digite si es hombre o mujer el alumno {valor + 1}: ')
        if(sexo_alumno == 'hombre' or sexo_alumno == 'mujer'):
            promedio_grupo = promedio_grupo + edad_alumno           
            total = promedio_grupo / total_grupo            
            if(sexo_alumno == 'hombre'):
                promedio_hombres = promedio_hombres + edad_alumno                
                total_alumnos = promedio_hombres / hombres               
            elif(sexo_alumno == 'mujer'):
                promedio_mujeres = promedio_mujeres + edad_alumno               
                total_alumnas = promedio_mujeres / mujeres
                
        
    print(f'El promedio de edad de todo el grupo es: {total}')
    print(f'El promedio de edad de los alumnos es de : {total_alumnos}')
    print(f'El promedio de edad de las alumnas es de : {total_alumnas}')
total_grupo(6, 3, 7)

"""               
Encontrar el menor valor de un conjunto de n números dados
"""   

def menor_valor(numeros):
    import math
    numero_menor = math.inf
    for valor in range(numeros):
        digitar_numero = float(input(f'Digite el número {valor+1}: '))
        if(digitar_numero < numero_menor):
            numero_menor = digitar_numero
    print(f'El número menor es: {numero_menor}')
menor_valor(5)

"""  
Cinco miembros de un club contra la obesidad desean saber cuanto han
bajado o subido de peso desde la última vez que se reunieron. Para esto se
debe realizar un ritual de pesaje en donde cada uno se pesa en diez
básculas distintas para así tener el pormedio mas exacto de su peso. Si 
"""  
def peso_miembros(miembros):
   for valor in range (0,5):  
        peso_acumulado = 0
        peso_promedio  = 0
        resta = 0
        peso_ultimo = float (input(f'Digitar el ultimo peso del paciente {valor + 1} : '))
        for valor_dos in range (0,10): 
         peso = float (input(f'Digitar el ultimo peso de la básculas {valor_dos + 1} : '))
        peso_acumulado = peso_acumulado + peso
        peso_promedio = peso_acumulado / 10
        resta = peso_promedio - peso_ultimo
        if(resta > 0):
            print(f'La persona subio de peso', resta, 'Kg')
        else:
            print(f'La persona bajo de peso', resta, 'Kg')
peso_miembros(4) 

"""              
En un supermercado una ama de casa pone en su carrito los artículos que
va tomando de los estantes. La señora quiere asegurarse de que el cajero
le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
artóculo anota su precio junto con la cantidad de artículos iguales que ha
tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
que irá gastando en los demás artículos, hasta que decide que ya tomó
todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
compra.      
"""  
def carrito_articulos(numero_productos):
    total_compra = 0
    for x in range(numero_productos):
        precio_producto = int(input(f'Digite el valor del precio del producto {x+1}: '))
        if(precio_producto > 1):
            cantidad_producto = int(input('Digite que cantidad del producto que desea llevar: '))
            pago = precio_producto * cantidad_producto
            total_compra = total_compra + pago
        else:
            precio_producto = 0
    print(f'El valor total de la compra es de: ${total_compra}')
carrito_articulos(5) 

"""     
Un teatro otorga descuentos según la edad del cliente, determinar la
cantidad del dinero que el teatro deja de percibir por cada ua de las
categorias. Tomar en cuenta que los niños menores de 5 años no pueden
entrar al teatro y que existe un precio único en los asientos. Los descuentos
se hacen tomando en cuenta el siguiente cuadro:
"""     
def personas(numero_de_personas):
    precio_boleta = int(input("Digite el precio de la boleta "))   
    limite_edad_uno = 0
    limte_edad_dos = 0
    limite_edad_tres = 0
    limite_edad_cuatro = 0
    limite_edad_cinco = 0
    for valor in range(numero_de_personas):
        edad = int(input(f'Digite la edad de la persona {valor + 1}: '))
        if edad < 5:
            print("Los niños menores de 5 años no pueden entrar")
        if edad > 5 and edad <= 14:
            limite_edad_uno += 1
        if edad > 15 and edad <= 19:
            limte_edad_dos += 1
        if edad > 20 and edad <= 45:
            limite_edad_tres += 1
        if edad > 46 and edad <= 65:
            limite_edad_cuatro += 1
        if edad > 66:
            limite_edad_cinco += 1
    print('la cantidad del dinero que el teatro deja de percibir en la categoría 5-14 es: ',
         limite_edad_uno * precio_boleta * 0.35)
    print('la cantidad del dinero que el teatro deja de percibir en la categoría 15-20 es: ',
          limte_edad_dos * precio_boleta * 0.25)
    print('la cantidad del dinero que el teatro deja de percibir en la categoría 20-45 es: ',
          limite_edad_tres * precio_boleta * 0.10)
    print('la cantidad del dinero que el teatro deja de percibir en la categoría 46-65 es: ',
          limite_edad_cuatro * precio_boleta * 0.25)
    print('la cantidad del dinero que el teatro deja de percibir en la categoría 66-adelante es: ',
          limite_edad_cinco * precio_boleta * 0.35)
personas(3)

"""   
Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
siguiente tabla:
 """   
def vendedores(numero_vendedores):
    for valor in range(numero_vendedores):
        venta = int(input(f'Digite cuanto vendío el empleado {valor + 1}: '))
        if(venta < 20):
            comision_uno = venta * 0.1
            print(f"La comisión del empleado es de {comision_uno}")
        if(venta < 40 and venta > 20):
            comision_dos = venta * 0.15
            print(f"La comisión del empleado es de {comision_dos} ")
        if(venta < 80 and venta >= 40):
            comision_tres = venta * 0.20
            print(f"La comisión del empleado es de {comision_tres}")
        if(venta < 160 and venta >= 80):
            comision_cuatro = venta * 0.25
            print(f"La comisión del empleado es de {comision_cuatro} ")
        if(venta > 160):
            comision_cinco = venta * 0.30
            print(f"La comisión del empleado es de {comision_cinco}")
vendedores(100) 

""" 
La empresa Encuestas S.A desea crear una función que les permita
conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue
el ganador o indicar si hubo empate y la cantidad de votos obtenidos.
""" 
def empresa_encuesta(personas):
    candidato_uno = 0
    candidato_dos = 0
    candidato_tres = 0
    ganador = 0
    for valor in range(personas):
        voto = int(input(f'Votante {valor + 1}, digite el numero del candidato a votar: '))
        if (voto == 1):
            candidato_uno += 1
        if (voto == 2):
            candidato_dos += 1
        if (voto == 3):
            candidato_tres += 1
    if (candidato_uno > candidato_dos and candidato_uno > candidato_tres):
        ganador = 1
    if (candidato_dos > candidato_uno and candidato_dos > candidato_tres):
        ganador = 2
    if (candidato_tres > candidato_uno and candidato_tres > candidato_dos):
        ganador = 3
    print(f'Votos del primer candidato: {candidato_uno}')
    print(f'Votos del segundo candidato: {candidato_dos}')
    print(f'Votos del tercer candidato: {candidato_tres}')
    print(f'El ganador es: {ganador}')
empresa_encuesta(50000)