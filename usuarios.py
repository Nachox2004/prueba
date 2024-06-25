import json
"""def agregarUsuario(UsuarioID:int):
    with open ("biblioteca.json", mode="r") as archivoJson:
    Leerjson = json.load(archivoJson)
    Usuario = {
        "UsuarioID": len(Leerjson["Usuario"])+1,
            "Nombre": "Jose Mondaca",
            "Email": "walala@gmail.com",
            "FechaRegistro": "2024-06-25"
    }
    Leerjson["Usuario"].append(Usuario)

with open("biblioteca.json", mode = "w") as archivoJson:
    json.dump(Leerjson, archivoJson, indent=4)"""
def eliminarUsuario(UsuarioID:int):
    with open ("biblioteca.json", mode = "r") as eliminarJson:
        Leerjson = json.load(eliminarJson)
    for Usuario in (Leerjson["Usuario"]):
        if Usuario["ID"] == UsuarioID:
            Leerjson["UsuarioID"].pop
        

def editarJson(UsuarioID:int):
    with open ("biblioteca.json", mode="w") as archivoJson:
        Leerjson = json.dump(editarJson)
    for Usuario in (Leerjson["Usuario"])
    

