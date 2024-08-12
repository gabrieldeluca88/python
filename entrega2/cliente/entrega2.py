class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return (f"Cliente: {self.nombre}\n"
                f"Email: {self.email}\n"
                f"Teléfono: {self.telefono}\n"
                f"Dirección: {self.direccion}")

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección de {self.nombre} ha sido actualizada a: {self.direccion}")

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"El email de {self.nombre} ha sido actualizado a: {self.email}")

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"El telefono de {self.nombre} ha sido actualizado a: {self.telefono}")


