import os
import sys
import JsonReader

jsonlist = []

def main():
    print("Seleccione una opción:\n"+
    "1-Cargar\n"+
    "2-Seleccionar\n"+
    "3-Máximo\n"+
    "4-Mínimo\n"+
    "5-Suma\n"+
    "6-Cuenta\n"+
    "7-Reportar\n"+
    "0-Salir\n\n")
    arg = input()
    if not arg:
        print("Elija una opción")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    else:
        switch(arg)

def Cargar():
    print("Ingrese una ubicación de archivo Ej: C:\\Usuario\\Archivo.json")
    path = input()
    if not path:
        print("Debe ingresar una ubicación de archivo.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif not path.endswith('.json'):
        print("Debe elegir un archivo con extensión .json")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif not os.path.exists(path):
        print("El archivo no existe.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    else:
        global jsonlist
        jsonlist.append(path)
        print("¡Archivo cargado exitosamente!")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()    

def Seleccionar():
    print("Ingrese su seleccion. Ej.: SELECCIONAR nombre,edad,promedio,activo DONDE nombre = \"Francisco\"\n")
    query = input("")
    queryAnalizer(query)
    os.system('cls')

def Maximo():
    global jsonlist
    values = []
    print("Ingrese el atributo a evaluar. Ej.: MAXIMO edad")
    rawquery = input("")
    query = rawquery.lower()
    atributes = query.split(' ')
    if len(atributes) == 2:
        if atributes[1] == "edad" or atributes[1] == "promedio":
            for each in jsonlist:
                jreader = JsonReader.JsonReader(each)
                regvalues = jreader.getValues(atributes[1])
                for x in regvalues:
                    values.append(x)
            maxvalue = max(values)
            print("El valor máximo de "+atributes[1].capitalize()+" es: "+str(maxvalue))
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
        else:
            print("Solo puede buscar el valor máximo para edad o promedio.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    elif len(atributes) == 1:
        if not atributes[0] == "maximo":
            print("Debe ingresar una consulta válida.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
        else:
            print("Debe ingresar un atributo a buscar.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    else:
        print("Debe ingresar una consulta válida.")
        input("Presione Cualquier tecla para continuar..")
        os.system('cls')
        main()
    

def Minimo():
    global jsonlist
    values = []
    print("Ingrese el atributo a evaluar. Ej.: MINIMO edad")
    rawquery = input("")
    query = rawquery.lower()
    atributes = query.split(' ')
    if len(atributes) == 2:
        if atributes[1] == "edad" or atributes[1] == "promedio":
            for each in jsonlist:
                jreader = JsonReader.JsonReader(each)
                regvalues = jreader.getValues(atributes[1])
                for x in regvalues:
                    values.append(x)
            minvalue = min(values)
            print("El valor mínimo de "+atributes[1].capitalize()+" es: "+str(minvalue))
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
        else:
            print("Solo puede buscar el valor mínimo para edad o promedio.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    elif len(atributes) == 1:
        if not atributes[0] == "maximo":
            print("Debe ingresar una consulta válida.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
        else:
            print("Debe ingresar un atributo a buscar.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    else:
        print("Debe ingresar una consulta válida.")
        input("Presione Cualquier tecla para continuar..")
        os.system('cls')
        main()

def Suma():
    input("Presione Cualquier tecla para continuar..")

def Cuenta():
    input("Presione Cualquier tecla para continuar..")

def Reportar():
    input("Presione Cualquier tecla para continuar..")

def Salir():
    raise SystemExit

def switch(arg):
    switcher={
        '1': Cargar,
        '2': Seleccionar,
        '3': Maximo,
        '4': Minimo,
        '5': Suma,
        '6': Cuenta,
        '7': Reportar,
        '0': Salir
    }
    if arg not in switcher:
        print("Opción Invalida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    else:
        func = switcher.get(arg, lambda: "Opción Invalida")
        return func()

def queryAnalizer(rawquery):
    query = rawquery.lower()
    words = query.split(' ',5)
    global jsonlist
    if len(words) == 0:
        print("Debe ingresar una consulta de seleccion.")
        input("Presione cualquier tecla para continuar..")
    elif len(words) == 2:
        if words[0] == "seleccionar":
            if words[1] == "*":
                for each in jsonlist:
                    jread = JsonReader.JsonReader(each)
                    jread.selectAll()
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                input("\nPresione cualquier tecla para continuar..")
                main()
            elif "," in words[1] or words[1] == "nombre" or words[1] == "edad" or words[1] == "activo" or words[1] == "promedio":
                for each in jsonlist:
                    jread = JsonReader.JsonReader(each)
                    jread.selectSome(words[1])
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                input("\nPresione cualquier tecla para continuar..")
                main()
            else:
                print("Revise que los atributos se hayan ingresado correctamente.")
                input("Presione cualquier tecla para continuar..")
                main()
        else:
            print("No se reconoce el comando "+words[0])
            input("Presione cualquier tecla para continuar..")
            main()
    elif len(words) == 6:
        if words[0] == "seleccionar":
            if words[1] == "*":
                for each in jsonlist:
                    jread = JsonReader.JsonReader(each)
                    jread.selectAllCondition(words[3]+"="+words[5])
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                input("\nPresione cualquier tecla para continuar..")
                main()
            elif "," in words[1] or words[1] == "nombre" or words[1] == "edad" or words[1] == "activo" or words[1] == "promedio":
                for each in jsonlist:
                    jread = JsonReader.JsonReader(each)
                    jread.selectSomeCondition(words[1],words[3]+"="+words[5])
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                input("\nPresione cualquier tecla para continuar..")
                main()
            else:
                print("Revise que los atributos se hayan ingresado correctamente.")
                input("Presione cualquier tecla para continuar..")
                main()
        else:
            print("No se reconoce el comando "+words[0])
            input("Presione cualquier tecla para continuar..")
            main()
    else:
        print("Ingrese una consulta válida.")
        input("Presione cualquier tecla para continuar..")
        main()

if __name__ == "__main__":
    main()