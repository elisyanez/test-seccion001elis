'''
De forma precautoria se ha decidido digitalizar estos planes para tener un control y
poder saber cuando la humanidad será conquistada por el líder Cerebro. Para esto, el personal a cargo del
laboratorio lo ha contratado a usted para que genere un sistema que contenga las siguientes características.
Un menú que contenga las siguientes opciones:
1.- Agregar plan
2.- Listar planes
3.- Eliminar plan por ID
4.- Generar bbdd
5.- Cargar bbdd
6.- Estadísticas
0.- Salir.
A considerar :
a.- Los planes tienen los siguientes ítems : ID (número), nombre, porcentaje efectividad (numero entero), categoría
interna.
b.- Al agregar el porcentaje, debe validar que este NÚMERO esté entre 0 y 100. Para validar este valor, se le solicita
crear una función.
c.- La categoría interna es un dato que se genera automáticamente y que varía dependiendo del número del
porcentaje de efectividad. Guíese por los siguientes valores : 0 y 25  Chiste. 26 y 50  anécdota. 51 y 75 
peligro. 76 y 99  atención. 100  esclavitud. Para generar estas categorías deberá crear una función QUE
RETORNE este valor.
d.- Para eliminar un plan de los registros, se debe solicitar el ID del plan. Recuerde solicitar una confirmación al
usuario antes de eliminar.
e.- Cuando se genera la bbdd (opción 4) se crea un archivo CSV.

f.- Cuando se carga la bbdd se hace a partir de un archivo CSV.
g.- Las estadísticas contemplan imprimir los siguientes datos :
1.- Porcentaje de efectividad promedio
2.- Plan con el porcentaje de efectividad más alto.
Finalmente, debe subir la evaluación a su cuenta de github de forma PRIVADA y compartir el link
'''
import csv
lista=[]
opc=-1
id_plan=0
def menu():
    print("")
    print(".-.-.-.-.-M E N U.-.-.-.-")
    print("")
    print("1.- Agregar Plan")
    print("2.- Listar Planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadisticas")
    print("0.- Salir")
    print("")

def valida_porc(percent):
    while percent>100 or percent<0:
        print("El porcentaje de efectividad debe estar entre 0 y 100")
        percent=int(input("Ingrese nuevamente un porcentaje valido: "))
    return percent

def clasificacion(porcentaje):
    if porcentaje>=0 and porcentaje<26:
        clas="Chiste"
    elif porcentaje>=26 and porcentaje<51:
        clas="Anecdota"
    elif porcentaje>=51 and porcentaje<76:
        clas="Peligro"
    elif porcentaje>=76 and porcentaje<100:
        clas="Atencion"
    elif porcentaje==100:
        clas="Esclavitud"
    return clas

while opc!=0:
    try:
        menu()
        opc=int(input("Ingrese una opción: "))
        if opc==1:
            print("")
            print("A G R E G A R    P L A N")
            print("")
            id_plan=id_plan+1
            nombre=input("Ingrese el nombre del plan: ")
            porcentaje=int(input("Ingrese el porcentaje de efectividad del plan [entre 0 y 100]: "))
            porc_validado=valida_porc(porcentaje)
            clasi=clasificacion(porc_validado)
            diccionario={'Nombre':nombre,'ID':id_plan,'Efectividad':porc_validado,'Clasification':clasi}
            lista.append(diccionario)
            print("Plan agregado con éxito!")
        if opc==2:
            print("")
            print("L I S T A   D E   P L A N E S")
            print("")
            for x in lista:
                print(f"ID PLAN: {x['ID']}  Nombre Plan: {x['Nombre']}  Efectividad: {x['Efectividad']}% Clasficación: {x['Clasification']}")
            print('\n'*2)
        if opc==3:
            print("")
            print("E L I M I N A R    P L A N")
            print("")
            elim=int(input("Ingrese ID del Plan a eliminar: "))
            encontrado=False
            for x in lista:
                while elim==x['ID']:
                    print(f"ID PLAN: {x['ID']}  Nombre Plan: {x['Nombre']}  Efectividad: {x['Efectividad']}% Clasficación: {x['Clasification']}")
                    print("Seguro que quiere eliminar este plan??")
                    seguro=input("[S/N]")
                    if seguro=="S":
                        lista.remove(x)
                        print("Plan removido con exito!")
                        break
                    elif seguro=="N":
                        print("El plan no ha sido eliminado")
                        print("Volviendo...")
                        break
                    else:
                        print("Elija una opcion valida, vuelva a intentarlo...")
        if opc==4:
            print("Generando Base de Datos...")
            with open('bbdd_plan.csv','w',newline='') as bbdd_plan:
                campo=['ID','Nombre','Efectividad','Clasification']
                escritor_csv=csv.DictWriter(bbdd_plan,fieldnames=campo)
                escritor_csv.writeheader()
                escritor_csv.writerows(lista)
            print("Base de datos creada con exito!")
        if opc==5:
            print("Cargando base de datos...")
            lista=[]
            with open("bbdd_plan.csv","r",newline='') as bbdd_plan:
                lector_csv=csv.DictReader(bbdd_plan)
                for fila in lector_csv:
                    lista.append(fila)
            for x in lista:
                int(x['ID'])
                int(x['Efectividad'])
            print("Base de datos cargada con éxito!")
        if opc==6:
            print("")
            print(".-.-.-.E S T A D Í S T I C A S.-.-.-")
            print("")
            cant_plan=0
            alto=0
            acum_plan=0
            for x in lista:
                cant_plan=cant_plan+1
                acum_plan=acum_plan+x['Efectividad']
                if x['Efectividad']>alto:
                    alto=x['Efectividad']
            total=acum_plan
            promedio=total/cant_plan            
                
            print(f"Porcentaje de efectividad promedio= {promedio}%")
            print(f"Porcentaje de efectividad más alto= {alto}%")
            print("Plan con el porcentaje de efectividad más alto=")
            for x in lista:
                if alto==x['Efectividad']:
                    print(f"ID PLAN: {x['ID']}  Nombre Plan: {x['Nombre']}  Efectividad: {x['Efectividad']}% Clasficación: {x['Clasification']}")
        if opc==0:
            print("Adios, gracias por utilizar nuestros servicios ;p")
            break
    except:
        print("Error Fatal, volviendo al menu principal...")
