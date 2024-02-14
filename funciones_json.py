def volver():
    volver=input('''
Pulsa INTRO para volver al menú''')
    if volver == "":
        seguir=False
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
        print()
        for ambito,registro in zip(ambitos,registros):
            print('''Para "%s" hay %d registros'''%(ambito,registro))

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

        ambito=ambitos()
        a=int(input('''
'''))

        edad=edades()
        b=int(input('''
'''))

        respuestas=recopilar()

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