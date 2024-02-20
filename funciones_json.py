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

def volver():
    while True:
        volver=input('''
Pulsa INTRO para volver al menú''')
        if volver == "":
            seguir=False
            break
        else:
            print("¿Te has confundido de tecla?")
    return seguir

def listaambitos(a):
    seguir=True
    while seguir:
        ambitos=[]
        for elemento in a:
            for i in elemento["MetaData"]:
                if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                    ambito=i["Nombre"]
                    if ambito not in ambitos:
                        ambitos.append(ambito)

        print('''
Se pueden consultar los siguientes ámbitos geográficos: ''')
        for i,ambito in zip(range(20),ambitos):
            print(i+1,ambito)

        seguir=volver() 

def registros(a):
    seguir=True
    while seguir:
        registros=[]
        ambitos=[]
        for elemento in a:
            for i in elemento["MetaData"]:
                if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                    ambito=i["Nombre"]
                    if ambito not in ambitos:
                        ambitos.append(ambito)
                    registros.append(len(elemento["Data"]))
        print('''
Ámbito geográfico           Registros
======================================''')
        for ambito,registro in zip(ambitos,registros):
            print(ambito," "*(33-len(ambito)),registro)
        print('''======================================

Total
=====
''',
sum(registros)," registros.")

        seguir=volver()

def buscador(datos):
    seguir=True
    while seguir:
        def ambitos():
            ambitos=[]
            for elemento in datos:
                for i in elemento["MetaData"]:
                    if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                        ambito=i["Nombre"]
                        if ambito not in ambitos:
                            ambitos.append(ambito)

            print('''
Elige uno de los siguientes ámbitos geográficos: ''')
            for i,ambito in zip(range(20),ambitos):
                print(i+1,ambito)
            return ambitos

        def edades():
            edades=[]
            for elemento in datos:
                for i in elemento["MetaData"]:
                    if i["Variable"]["Nombre"] == "Semiintervalos de edad" or i["Variable"]["Nombre"] == "Totales de edad" or i["Variable"]["Nombre"] == "Grupos de edad":
                        edad=i["Nombre"]
                        if edad not in edades:
                            edades.append(edad)
            print('''
Elige uno de los siguientes rangos de edades: ''')
            for i,edad in zip(range(20),edades):
                print(i+1,edad)
            return edades

        def recopilar():
            lista=[]
            respuestas=[]
            for elemento in datos:
                for i in elemento["MetaData"]:
                    if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                        if i["Nombre"] == ambito[a-1]:
                            lista.append(elemento)

            for elemento in lista:
                for i in elemento["MetaData"]:
                    if i["Variable"]["Nombre"] == "Semiintervalos de edad" or i["Variable"]["Nombre"] == "Totales de edad" or i["Variable"]["Nombre"] == "Grupos de edad":
                        if i["Nombre"] == edad[b-1]:
                            for j in elemento["Data"]:
                                respuesta={}
                                respuesta["Año"]=j["Anyo"]
                                respuesta["Trimestre"]=j["T3_Periodo"]
                                respuesta["Valor"]=j["Valor"]
                                respuestas.append(respuesta)
            return respuestas

        while True:
            try:
                while True:    
                    try:
                        ambito=ambitos()
                        a=int(input('''
'''))
                        break
                    except:
                        print("Dato erróneo, por favor, indica un número de la lista.")

                while True:
                    try:
                        edad=edades()
                        b=int(input('''
'''))
                        break
                    except:
                        print("Dato erróneo. Por favor, indica un número de la lista.")

                respuestas=recopilar()
                break
            except:
                print("Los número introducidos no se corresponden a ningún registro. Por favor, elija una de las opciones de cada lista.")

        print('''
Datos de paro para el ámbito geográfico "%s" y el rango de edad "%s":

Año    Trimestre        Dato
=============================
        '''%(ambito[a-1],edad[b-1]))
        for respuesta in respuestas:
            for dato in dict.values(respuesta):
                print(dato,end='        ')
            print()

        seguir=volver()

def intervalo(a):
    seguir=True
    while seguir:
        while True:
            try:
                min=float(input('''
Indica el dato menor: '''))
                break
            except:
                print("Dato erróneo. Si quieres consultar un número con decimales asegúrate de usar un punto (.) para separar ambas partes del número.")
        while True:
            try:        
                max=float(input("Indica el dato mayor: "))
                break
            except:
                print("Dato erróneo. Si quieres consultar un número con decimales asegúrate de usar un punto (.) para separar ambas partes del número.")


        ambitos=[]
        for elemento in a:
            for i in elemento["Data"]:
                valor=i["Valor"]
                if valor:
                    if valor > 0:
                        if float(valor) > min and float(valor) < max:
                            for i in elemento["MetaData"]:
                                if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                                    ambito=i["Nombre"]
                                    if ambito not in ambitos:
                                        ambitos.append(ambito)

        if len(ambitos) == 0:
            print("No hay registros entre %.2f y %.2f para ningún ámbito geográfico."%(min,max))
        elif len(ambitos) == 1:
            print("Hay valores registrados entre %.2f y %.2f para el ámbito geográfico "%(min,max),end='')
            for ambito in ambitos:
                print(ambito)
        else:
            print("Los ámbitos en los que hay valores registrados entre %.2f y %.2f son: "%(min,max))
            for ambito in ambitos:
                print(ambito)
        
        seguir=volver()

def limites(a):
    seguir=True
    while seguir:
        max=0
        min=100
        for elemento in a:
            for i in elemento["Data"]:
                valor=i["Valor"]
                if valor:
                    if valor > max:
                        max = valor
                        añomax = i["Anyo"]
                        trimestremax = i["T3_Periodo"]
                        for i in elemento["MetaData"]:
                            if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                                ambitomax=i["Nombre"]
                            elif i["Variable"]["Nombre"] == "Semiintervalos de edad" or i["Variable"]["Nombre"] == "Totales de edad" or i["Variable"]["Nombre"] == "Grupos de edad":
                                edadmax=i["Nombre"]
                    elif valor < min:
                        min = valor
                        añomin = i["Anyo"]
                        trimestremin = i["T3_Periodo"]
                        for i in elemento["MetaData"]:
                            if i["Variable"]["Codigo"] == "CCAA" or i["Variable"]["Codigo"] == "NAC":
                                ambitomin=i["Nombre"]
                            elif i["Variable"]["Nombre"] == "Semiintervalos de edad" or i["Variable"]["Nombre"] == "Totales de edad" or i["Variable"]["Nombre"] == "Grupos de edad":
                                edadmin=i["Nombre"]

        print("La tasa de paro más alta es del ",max,"% y se registró en el trimestre ",trimestremax," del año ",añomax," en el ámbito geográfico ",ambitomax," para el grupo de edad ",edadmax,". \nLa tasa de paro más alta es del ",min,"% y se registró en el trimestre ",trimestremin," del año ",añomin," en el ámbito geográfico ",ambitomin," para el grupo de edad",edadmin,".")

        seguir=volver()