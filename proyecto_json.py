import json, funciones_json

with open("TasaParo.json") as f:
    datos=json.load(f)

#Menú
def funcion():
    while True:
        try:
            menu=int(input('''Menú
==============================================================================
1. Lista de ámbitos geográficos para los que hay registro
2. Número de registros para cada ámbito geográfico
3. Consulta de la tasa de paro por ámbito geográfico y grupo de edad
4. Consulta de ámbitos geográficos dentro de un rango
5. Consulta del dato mayor y menor de cada ámbito geográfico y grupo de edad
6. Salir

'''))
            break
        except:
            print("Error. Usa un número de la lista para elegir una función del siguiente menú:")
    return menu

menu=funcion()

while menu != 6:

    if menu > 6 or menu < 0:
        print("Error. Usa un número de la lista para elegir una función del siguiente menú:")
        menu=funcion()

    if menu == 1:
        funciones_json.listaambitos(datos)

        print()
        menu=funcion()

    if menu == 2:
        funciones_json.registros(datos)

        print()
        menu=funcion()

    if menu == 3:
        funciones_json.buscador(datos)

        print()
        menu=funcion()

    if menu == 4:
        funciones_json.intervalo(datos)

        print()
        menu=funcion()

    if menu == 5:
        funciones_json.limites(datos)

        print()
        menu=funcion()