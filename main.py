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
        if not atributes[0] == "minimo":
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
    global jsonlist
    values = []
    print("Ingrese el atributo a sumar. Ej.: SUMA edad")
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
            sumvalue = sum(values)
            print("El valor total de la suma de "+atributes[1].capitalize()+" es: "+str(sumvalue))
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
        else:
            print("Solo puede buscar la suma para edad o promedio.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    elif len(atributes) == 1:
        if not atributes[0] == "suma":
            print("Debe ingresar una consulta válida.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
        else:
            print("Debe ingresar un atributo a sumar.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    else:
        print("Debe ingresar una consulta válida.")
        input("Presione Cualquier tecla para continuar..")
        os.system('cls')
        main()

def Cuenta():
    global jsonlist
    print("Inicie el conteo de registros escribiendo 'CUENTA'")
    rawquery = input()
    query = rawquery.lower()
    regs = 0
    if query == "cuenta":
        for each in jsonlist:
            jreader = JsonReader.JsonReader(each)
            regs += jreader.countRegs()
        print("¡Hay un total de "+str(regs)+" registros!")
        input("Presione Cualquier tecla para continuar..")
        os.system('cls')
        main()
    else:
        print("Debe escribir 'CUENTA' sin las comillas.")
        input("Presione Cualquier tecla para continuar..")
        os.system('cls')
        main()
    

def Reportar():
    global jsonlist
    print("Ingrese el número de registros que desea reportar. Ej.: REPORTAR 10")
    rawquery = input()
    query = rawquery.split()
    regs = 0
    if len(query) == 2:
        if query[1].isnumeric():
            rowstoadd = ""
            rows = []
            jreader = None
            counter = 0
            for each in jsonlist:
                jreader = JsonReader.JsonReader(each)
                regs += jreader.countRegs()
            if int(query[1]) <= regs:
                for each in jsonlist:
                    jreader = JsonReader.JsonReader(each)
                    jreader.setCounter(counter)
                    rows.append(jreader.getAllValues(query[1]))
                    counter = jreader.getCounter()
                jreader.resetCounter()
    
                for x in rows:
                    for y in x:
                        rowstoadd += "<tr>"
                        for z in y:
                            rowstoadd += "<td>"+str(z)+"</td>\n"
                        rowstoadd += "</tr>"

                htmlfile = """<!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Reporte de Registros</title>
            <link href="csspagina.css" rel="stylesheet" type="text/css">
        </head>
        <body>
            <header id="head">
                <h1 id="titulo" align="center">Reporte de Registros</h1><br>
                <br>
            </header>
        <section id="sect">
            <div id="divsect" align="center">
                <table id="tabladatos">
                    <tr>
                        <th class="first">Nombre</th>
                        <th>Edad</th>
                        <th>Activo</th>
                        <th>Promedio</th>
                    </tr>"""+rowstoadd+"""
                </table>
            </div>
        </section>
        <footer id="foot">Dennis Andre Lopez Mendez &copy;2020</footer>
        </body>
    </html>"""

                cssfile = """
        @charset "utf-8";
#sect {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 15px;
	background-color:#CFEFFA;
	width: 70%;
	height: 100%;
	margin: 0 auto 0 auto;
	padding-bottom: 25px;
	padding-top: 15px;
}
.form {
		margin: 0 auto;
		width: 80%;
	}

.form label{
		display: inline-block;
		text-align: right;
		float: left;
	}

.form input{
		display: inline-block;
		text-align: left;
		float: right;
	}
	
.form input[type="text"]{
		width: 50%;
	}
	
.form input[type="password"]{
		width: 50%;
	}
	
.form input[type="date"]{
		width: 50%;
	}
.form input[type="image"]{
	width: auto !important;
  	float: none !important;
	text-align:center;
}
.form input[type="button"]{
	width: auto !important;
  	float: none !important;
	text-align:center;
}
#head #titulo {
	font-family: "Courier New", Courier, monospace;
	position:relative;
	margin: auto;
	text-align:center;
	top: 27px;
}

	
.form #countr{
		display: inline-block;
		text-align: left;
		float: right;
		width: 50.5%
	}
	
body{
	height: 100%;
	background-color:#FBEFD7
}

#foot{
	width: 100%;
	height:auto;
	text-align: center;
	background-color:#000000;
	color: #FFFFFF;
	position: fixed;
	left: 0;
	bottom: 0;
}

#head{
	width:100%;
	background-color:#FC9C32;
	padding-bottom: 20px;
	text-align:center;
}
#tabladatos {
	font-family: Verdana, Geneva, sans-serif;
	font-size: 14px;
	border-top-width: thin;
	border-right-width: thin;
	border-bottom-width: thin;
	border-left-width: thin;
	border-top-style: none;
	border-right-style: none;
	border-bottom-style: none;
	border-left-style: none;
}
td {
	border-top-style: none;
	border-right-style: solid;
	border-bottom-style: solid;
	border-left-style: solid;
	border-top-width: medium;
	border-right-width: medium;
	border-bottom-width: medium;
	border-left-width: medium;
}
#sect #divsect #tabladatos tr .first {
	border-left-style: solid;
	border-top-width: medium;
	border-right-width: medium;
	border-bottom-width: medium;
	border-left-width: medium;
}


th {
	border-top-width: medium;
	border-right-width: medium;
	border-bottom-width: medium;
	border-left-width: medium;
	border-top-style: double;
	border-right-style: solid;
	border-bottom-style: solid;
	border-left-style: double;
}
        """

                report = open('reporte.html', 'w')
                report.write(htmlfile)
                report.close()
                css = open('csspagina.css','w')
                css.write(cssfile)
                css.close()
                os.startfile("reporte.html")
                print("¡Se generó el reporte con éxito!")
                input("Presione Cualquier tecla para continuar..")
                os.system('cls')
                main()
            else:
                print("Hay menos registros de los que desea reportar, elija una cantidad válida.")
                input("Presione Cualquier tecla para continuar..")
                os.system('cls')
                main()
        else:
            print("Debe ingresar un valor númerico.")
            input("Presione Cualquier tecla para continuar..")
            os.system('cls')
            main()
    else:
        print("Debe ingresar una consulta válida.")
        input("Presione Cualquier tecla para continuar..")
        os.system('cls')
        main()

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