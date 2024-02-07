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

        volver=input('''
Pulsa INTRO para volver al menú''')
        if volver == "":
            seguir=False

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

        volver=input('''
Pulsa INTRO para volver al menú''')
        if volver == "":
            seguir=False