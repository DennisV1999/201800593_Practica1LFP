# 201800593_Practica1LFP
Practica 1 de Lenguajes Formales

# SimpleQL

SimpleQL es una aplicación diseñada para poder leer la información contenida dentro de un archivo de extensión **.json**. En ningún momento este intenta ser una alternativa
a SQL, si no más solo una herramienta para analizar datos.

## Funcionalidades:

* ### 1. Cargar:
    Esta función permite al usuario cargar diferentes archivos **.json** a la aplicación para que esta después pueda hacer uso de ellos.
    Para hacer esto lo unico que se debe ingresar es la **ubicación** del archivo en su computador.
    
* ### 2. Seleccionar:
    Esta función le permite al usuario seleccionar los registros que están contenidos dentro del archivo, como si de SQL se tratase, la sintaxis es:
    
    SELECCIONAR 'atributos' DONDE 'condicional'
    
    Cabe destacar que **'atributos'** se puede intercambiar por un '*' para seleccionar todos los atributos del archivo, también es importante saber que
    la aplicación solo acepta **UNA** sola condicional de **igualación** por consulta de selección.
    
* ### 3. Máximo:
    Permite al usuario encontrar el **valor máximo** de la edad o promedio en uno de los registros que se encuentran en los archivos **.json**.
    Su sintaxis es:
    
    MAXIMO edad
    MAXIMO promedio
    
* ### 4. Mínimo:
    Permite al usuario encontrar el **valor mínimo** de la edad o promedio en uno de los registros que se encuentran en los archivos **.json**.
    Su sintaxis es:
    
    MINIMO edad
    MINIMO promedio
    
* ### 5. Suma:
    Permite al usuario sumar todos los valores de promedio o edad que estén presentes en cada uno de los archivos **.json**.
    Su sintaxis es:
    
    SUMA edad
    SUMA promedio
    
* ### 6. Cuenta:
    Cuenta el número de registros que se han cargado en la memoria.
    Su sintaxis es:
    
    CUENTA (sin comillas ni nada mas)
    
* ### 7. Reportar:
    Permite al usuario generar un reporte html sobre una cierta cantidad de registros existentes, los registros que aparecen en el reporte son elegidos desde
    el primero que está en memoria hasta el número deseado de registros en el reporte.
    Su sintaxis es:
    
    REPORTAR N
    
    Donde N es el número deseado de reportes.
    
    
   
