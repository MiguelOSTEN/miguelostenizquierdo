mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, nombre_cliente, direccion, contacto, sexo, descripcion, nombre_producto, referencia, cantidad):
    if nombre_cliente == '' or direccion == '' or contacto == '' or sexo == '' or descripcion == '' or nombre_producto == '' or referencia == '' or cantidad == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        if nombre_cliente not in diccionario:
            diccionario[nombre_cliente] = []
        diccionario[nombre_cliente].append({'direccion': direccion, 'contacto': contacto, 'sexo': sexo, 'descripcion': descripcion, 'producto': {'nombre': nombre_producto, 'referencia': referencia, 'cantidad': cantidad}})
        enter = input(f'\nEl pedido del cliente {nombre_cliente} ha sido registrado con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        nombre_cliente = input('Nombre del cliente: ')
        direccion = input('Dirección: ')
        contacto = input('Contacto: ')
        sexo = input('Sexo: ')
        descripcion = input('Descripción del lugar: ')
        nombre_producto = input('Nombre del producto: ')
        referencia = input('Referencia del producto: ')
        cantidad = input('Cantidad del producto: ')
        fnt_agregar(mi_diccionario, nombre_cliente, direccion, contacto, sexo, descripcion, nombre_producto, referencia, cantidad)
        
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar Pedido\n2. Mostrar Pedidos\n3. Salir\n- > ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nPedidos Registrados:')
        for cliente, pedidos in mi_diccionario.items():
            print(f"Cliente: {cliente}")
            for pedido in pedidos:
                print("Dirección:", pedido['direccion'])
                print("Contacto:", pedido['contacto'])
                print("Sexo:", pedido['sexo'])
                print("Descripción del lugar:", pedido['descripcion'])
                print("Producto:", pedido['producto']['nombre'])
                print("Referencia:", pedido['producto']['referencia'])
                print("Cantidad:", pedido['producto']['cantidad'])
                print("-------------------")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False