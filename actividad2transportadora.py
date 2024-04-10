class Transportadora:
    def __init__(self):
        self.despachos = {}
        self.numero_despacho = 1

    def agregar_despacho(self, placa, descripcion_vehiculo, nombre_conductor, ruta, descripcion_carga):
        self.despachos[self.numero_despacho] = {
            'placa': placa,
            'descripcion_vehiculo': descripcion_vehiculo,
            'nombre_conductor': nombre_conductor,
            'ruta': ruta,
            'descripcion_carga': descripcion_carga
        }
        self.numero_despacho += 1

    def mostrar_despachos(self):
        if not self.despachos:
            print("No hay despachos registrados.")
        else:
            for numero, despacho in self.despachos.items():
                print(f"Despacho número {numero}:")
                print(f"Placa del vehículo: {despacho['placa']}")
                print(f"Descripción del vehículo: {despacho['descripcion_vehiculo']}")
                print(f"Nombre del conductor: {despacho['nombre_conductor']}")
                print(f"Ruta: {despacho['ruta']}")
                print(f"Descripción de la carga: {despacho['descripcion_carga']}")
                print()

transportadora = Transportadora()

import os
sw = True

while sw:
    os.system('cls')
    opcion = input('1. Agregar Despacho\n2. Mostrar Despachos\n3. Salir\n- > ')
    if opcion == '1':
        os.system('cls')
        placa = input('Placa del vehículo: ')
        descripcion_vehiculo = input('Descripción del vehículo: ')
        nombre_conductor = input('Nombre del conductor: ')
        ruta = input('Ruta: ')
        descripcion_carga = input('Descripción de la carga: ')
        transportadora.agregar_despacho(placa, descripcion_vehiculo, nombre_conductor, ruta, descripcion_carga)
        input(f'\nDespacho registrado con éxito. <ENTER>')
    elif opcion == '2':
        os.system('cls')
        transportadora.mostrar_despachos()
        input('\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False
