# coding = utf-8

# 12 eventos de inundaciones hola

inundacion = 1
fluv = 0
cost = 0
urb = 0
hogaresfluvc = 0
hogarescostc = 0
hogaresurbc = 0

def calcular_promedio_afectacion(total_hogares, total_eventos, tipo):
    if total_eventos == 0:
        print(f"\nNo hubo casos de inundación {tipo}.")
        return
    
    print(f'\nResumen de inundación tipo {tipo}')
    print(f'Número de eventos: {total_eventos}')
    print(f'Número de casas afectadas {total_hogares}')
    promedio = total_hogares / total_eventos
    print(f"Promedio de hogares afectados por inundación {tipo}: {promedio:.2f}")


print('Hola')

while inundacion <= 12:
    try:
        print(f'\nQué tipo de inundación se presentó en el caso {inundacion}')
        print('Tipo 1: Inundación fluvial')
        print('Tipo 2: Inundación costera')
        print('Tipo 3: Inundación urbana')
        tipo = int(input(f'Inserte el tipo de inundación según su número de tipo: '))
        inundacion +=1

        if tipo == 1:
            try:
                hogaresfluv = int(input('\nCuántos hogares fueron afectados '))
                hogaresfluvc += hogaresfluv
                fluv += 1
            except ValueError:
                print('\nEl número ingresado no es válido')
                inundacion -=1
                continue

        elif tipo == 2:
            try:
                hogarescost = int(input('\nCuántos hogares fueron afectados '))
                hogarescostc += hogarescost
                cost += 1
            except ValueError:
                print('\nEl número ingresado no es válido')
                inundacion -=1
                continue

        elif tipo == 3:
            try:
                hogaresurb = int(input('\nCuántos hogares fueron afectados '))
                hogaresurbc += hogaresurb
                urb += 1
            except ValueError:
                print('\nEl número ingresado no es válido')
                inundacion -=1
                continue
        else:
            print('\nOpción no válida, inserte un número entre 1 y 3')
            inundacion -=1

    except ValueError:
        print('\nEl número ingresado no es válido')
        continue

calcular_promedio_afectacion(hogaresfluvc, fluv, "fluvial")
calcular_promedio_afectacion(hogarescostc, cost, "costera")
calcular_promedio_afectacion(hogaresurbc, urb, "urbana")
