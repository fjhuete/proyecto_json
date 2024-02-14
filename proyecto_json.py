import json, funciones_json

with open("TasaParo.json") as f:
    datos=json.load(f)

menu=funciones_json.funcion()

while menu != 6:

    if menu > 6 or menu < 0:
        print("Error. Usa un número de la lista para elegir una función del siguiente menú:")
        menu=funciones_json.funcion()

    if menu == 1:
        funciones_json.listaambitos(datos)

        print()
        menu=funciones_json.funcion()

    if menu == 2:
        funciones_json.registros(datos)

        print()
        menu=funciones_json.funcion()

    if menu == 3:
        funciones_json.buscador(datos)

        print()
        menu=funciones_json.funcion()

    if menu == 4:
        funciones_json.intervalo(datos)

        print()
        menu=funciones_json.funcion()

    if menu == 5:
        funciones_json.limites(datos)

        print()
        menu=funciones_json.funcion()