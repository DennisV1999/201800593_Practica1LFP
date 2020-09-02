import os
import sys

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
        main()    

def Seleccionar():
    input("Presione Cualquier tecla para continuar..")

def Maximo():
    input("Presione Cualquier tecla para continuar..")

def Minimo():
    input("Presione Cualquier tecla para continuar..")

def Suma():
    input("Presione Cualquier tecla para continuar..")

def Cuenta():
    input("Presione Cualquier tecla para continuar..")

def Reportar():
    input("Presione Cualquier tecla para continuar..")

def Salir():
    sys.exit()

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

if __name__ == "__main__":
    main()