"""serie="N-02"
match serie:
    case "N-01":
        print("samsung")
    case "N-02":
        print("nokia")
    case "N-03":
        print("motorola")
    case _:
        print("no existe ese producto")"""


cliente = {"nombre":"federico",
           "edad":45,
           "ocupacion":"instructor"}

pelicula = {"titulo":"matrix",
            "ficha_tecnica":{"protagonista":"keanu reeves",
                             "director":"Lana y Lylly wachowski"}}

elementos =[cliente,pelicula,"libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad":edad,
              "ocupacion":ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo":titulo,
              "ficha_tecnica":{"protagonista":protagonista,
                               "director":director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("nose que es eso ")

                        
