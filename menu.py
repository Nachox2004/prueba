import json



while True:
    print("Bienvenido a Mundo Libro")
    print("Escoja entre las siguientes 3 opciones")
    print(f"1°- Mantenedor de usuarios\n2°- Reportes\n3°- Salir")
    op  = int(input("Ingrese su opcion: "))
    if op == 1:
        print("A ingresado al mantenedor de usuarios")
        print(f"1° Agregar usuario\n2° Editar usuario\n3° Eliminar usuario \n4° Buscar usuario\n5° Volver")
        mu = int(input("Ingrese su opcion "))
        if mu == 1:
            with open ("biblioteca.json", mode="r") as archivoJson:
                Leerjson = json.load(archivoJson)
                Usuario = {
                    "UsuarioID": len(Leerjson["Usuario"])+1,
                    "Nombre": "Jose Mondaca",
                    "Email": "walala@gmail.com",
                    "FechaRegistro": "2024-06-25"
                }

        if mu ==3:
            def eliminarUsuario(UsuarioID:int):
                with open ("biblioteca.json", mode = "r") as eliminarJson:
                    Leerjson = json.load(eliminarJson)
                    for Usuario in (Leerjson["Usuario"]):
                        if Usuario["ID"] == UsuarioID:
                            Leerjson["UsuarioID"].pop

                
                    
    
    if op == 2:
        print("A escogido ver los reportes de la biblioteca")

    if op == 3 :
        print("Va saliendoo!!")
        break