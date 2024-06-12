'''

Esta linea es prueba de que se modifico el archivo original

crear un sistema para una empresa de informatica.
El sistema cuenta con el sgte menu
1-agregar producto
2-listar todos los productos
3-eliminar un producto por id
4-generar archivo csv
5-cargar archivo csv
6-estadisticas
0-salir

a-El producto tiene un ID, nombre y precio
b-En la opcion de estadisticas se imprimen los sgtes datos
    1.Precio total de todos los productos
    2.Promedio del precio de los productos

Puede desarrollar el ejercicio usando listasa anidadas o lista de diccionario
Recuerde usar la libreria csv
Debe utilizar al menos 3 funciones.
'''
import csv
opc=-1
lista=[]
prod_id=0
def menu():
    print("\n"*3)
    print(".-.-.-.-.-.-.-")
    print("M E N U")
    print(".-.-.-.-.-.-")
    print("1 AGREGAR PRODUCTO")
    print("2 LISTAR TODOS LOS PRODUCTOS")
    print("3 ELIMINAR PRODUCTO POR ID")
    print("4 GENERAR ARCHIVO CSV")
    print("5 CARGAR ARCHIVO CSV")
    print("6 ESTADISTICAS")
    print("7 print lista")
    print("0 SALIR")
while opc!=0:
    try:
        menu()
        opc=int(input("Ingrese una opción: \n"))
        if opc==1:
            print("")
            print("")
            print("A G R E G A R   P R O D U C T O")
            prod=input("Ingrese el nombre del producto: ")
            prod_id=prod_id+1
            prod_precio=int(input("Ingrese el precio del producto: "))
            dic_prod={"Producto":prod,"ID":prod_id,"Precio":prod_precio}
            lista.append(dic_prod)
        if opc==2:
            print("")
            print("")
            print("L I S T A    P R O D U C T O S")
            for x in lista:
                print(f"Producto: {x['Producto']}   ID: {x['ID']}   Precio: {x['Precio']}")
        if opc==3:
            print("")
            print("")
            print("E L I M I N A R     P R O D U C T O")
            print("")
            elim_id=int(input("Ingrese el ID del producto a eliminar: "))
            print("Buscando producto...")
            encontrado=False
            for x in lista:
                while elim_id==x['ID']:
                    print("Detalle del producto: ")
                    print(f"Producto: {x['Producto']}   ID: {x['ID']}   Precio: {x['Precio']}")
                    print("Realmente desea eliminar este producto?")
                    elim=input("[S/N]")
                    if elim=="S":
                        lista.remove(x)
                        print("Producto eliminado correctamente!")
                        print("Volviendo al menu...")
                        break
                    if elim=="N":
                        print("El producto no ha sido eliminado")
                        print("Volviendo al menu...")
                        break
                    else:
                        print("Error. ingrese S o N")
        if opc==4:
            print("Generando archivo csv...")
            print(".."*3)
            with open('bbdd_prod.csv','w',newline='') as bbdd_prod:
                campo=['Producto','ID','Precio']
                escritor_csv = csv.DictWriter(bbdd_prod,fieldnames=campo)
                escritor_csv.writeheader()
                escritor_csv.writerows(lista)
                        
            print("Archivo generado correctamente!")
        if opc==5:
            with open('bbdd_prod.csv','r',newline='')as bbdd_prod:
                lector_csv=csv.DictReader(bbdd_prod)
                for fila in lector_csv:
                    lista.append(fila)
            print("Archivo cargado correctamente!")
            for x in lista:
                int(x['ID'])
                int(x['Precio'])
                prod_id=(int(x['ID']))+1
        if opc==6:
            print("E S T A D I S T I C A S")
            print("")
            total_precio=0
            for x in lista:
                total_precio=total_precio+(x['Precio'])
            print("Precio Total de todos los Productos")
            print(total_precio)
        if opc==7:
            print(lista)
    except:
        print("ERROR FATAL...")
        print("VOLVIENDO AL MENU PRINCIPAL...")
    
