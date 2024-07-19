#Lucas Godoy
#Seccion 1
import math
import csv
import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignar_sueldos_rand():
    sueldos = {}
    for i in trabajadores:
        sueldos[i] = random.randint(300000, 2500000)
    with open('sueldos.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sueldos.keys())
        writer.writeheader()
        writer.writerow(sueldos)

    print('\nSueldos asignados!')
    print(' ')
    return sueldos

def clasificar_sueldos():
    sueldos_menores = {}
    sueldos_entre = {}
    sueldos_superiores = {}

    try:
        for i in sueldos:
            if sueldos[i] < 800000:
                sueldos_menores[i] = sueldos[i]
            elif sueldos[i] > 800000 and sueldos[i] < 2000000:
                sueldos_entre[i] = sueldos[i]
            elif sueldos[i] > 2000000:
                sueldos_superiores[i] = sueldos[i]
        print(f'\nSueldos menores a $800.000 TOTAL: {len(sueldos_menores)}\n\nNombre empleado\t\tSueldo')
        for trabajador, sueldo in sueldos_menores.items():
            print(f'{trabajador}\t\t${sueldo}')
        print(f'\nSueldos entre $800.000 y $2.000.000 TOTAL: {len(sueldos_entre)}\n\nNombre empleado\t\tSueldo')
        for trabajador, sueldo in sueldos_entre.items():
            print(f'{trabajador}\t\t${sueldo}')
        print (f'\nSueldos superiores a $2.000.000 TOTAL: {len(sueldos_superiores)}\n\nNombre empleado\t\tSueldo')
        for trabajador, sueldo in sueldos_superiores.items():
            print(f'{trabajador}\t\t${sueldo}')
    except NameError:
        print('\nError, lista de sueldos no encontrado, asigne los sueldos con la opcion 1 e intentelo denuevo.')
    except:
        print('\nError, intentelo denuevo')
    print(' ')
    
def ver_estadisticas():
    try:
        sueldoMinimo = min(sueldos.values())
        sueldoMaximo = max(sueldos.values())
        contadorPromedio = 0
        contadorMedia = 1
        for i in sueldos:
            contadorPromedio += sueldos[i]
            contadorMedia *= sueldos[i]
        promedio = contadorPromedio/10
        mediaGeometrica = math.sqrt(contadorMedia)
        print(f'\nSueldo minimo: ${sueldoMinimo}')
        print(f'Sueldo maximo: ${sueldoMaximo} ')
        print(f'Promedio: {promedio}')
        print(f'Media geometrica: {mediaGeometrica}')
    except NameError:
        print('\nError, lista de sueldos no encontrado, asigne los sueldos con la opcion 1 e intentelo denuevo.')
    except:
        print('\nError, intentelo denuevo')
    print(' ')
        
def reporte_sueldos():
    try:
        print(f'\nNombre Empleado\t\tSueldo base\t\tDescuento Salud\t\tDescuento AFP\t\tSueldo liquido')
        for i in sueldos:
            print(f'{i}\t\t${sueldos[i]}\t\t${sueldos[i]*7/100}\t\t${sueldos[i]*12/100}\t\t${math.trunc(sueldos[i] - (sueldos[i]*7/100) - (sueldos[i]*12/100))}')
    except NameError:
        print('\nError, lista de sueldos no encontrado, asigne los sueldos con la opcion 1 e intentelo denuevo.')
    except:
        print('\nError, intentelo denuevo')
    print(' ')


while True:
    print('Menu de opciones ET\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadisticas\n4. Reporte de sueldos\n5. Salir del programa\n')
    try:
        userInput = int(input('Eliga una opcion: '))
        while userInput < 1 or userInput > 5:
            userInput = int(input('Error, input invalido, intentelo denuevo: '))
    except:
        userInput = int(input('Error, input invalido, intentelo denuevo: '))
        while userInput < 1 or userInput > 5:
            userInput = int(input('Error, input invalido, intentelo denuevo: '))

    if userInput == 1:
        sueldos = asignar_sueldos_rand()

    if userInput == 2:
        clasificar_sueldos()

    if userInput == 3:
        ver_estadisticas()

    if userInput == 4:
        reporte_sueldos()

    if userInput == 5:
        print('Finalizando programa...\nDesarrollado por Lucas Godoy\nRUT 21.713.335-1')
        break
