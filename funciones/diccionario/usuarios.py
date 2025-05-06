usuarios = {}

while True:
    document = input("Ingresa el número de documento: ")
    name = input("Ingresa un nombre: ")
    lastname = input("Ingresa el apellido: ")
    mail = input("Ingresa un correo: ")
    usuario ={"name": name, "lastname": lastname, "mail": mail}
    usuarios["document"]= usuario
    continuar = int(input("Vas a agregar otro usuario? 1('si') / 2('no'): "))
    if continuar != 1:
        break

print(usuarios)
    