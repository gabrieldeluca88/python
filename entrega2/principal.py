from cliente.entrega2 import *

# Función principal 
def main():
    # Creo una lista vacia para guardar los clientes
    lista_clientes = []

    # Creo clientes y los agrego
    cliente1 = Cliente("Juan", "juan@email.com", "123456789", "Calle Buenos Aires 555")
    cliente2 = Cliente("Pedro", "pedro@email.com", "987654321", "Avenida Belgrano 222")
    
    lista_clientes.append(cliente1)
    lista_clientes.append(cliente2)

    # Imprimir info de los clientes
    for cliente in lista_clientes:
        print(cliente)
        print("*" * 100)

    # Actualizo la información de un cliente
    cliente1.actualizar_direccion("Calle Nueva 876")
    cliente1.actualizar_email("juan.nuevo@email.com")
    cliente1.actualizar_telefono("123123456")

    # Imprimir info actualizada del cliente
    print("*" * 100)
    print(cliente1)

# Ejecuto el programa principal
if __name__ == "__main__":
    main()