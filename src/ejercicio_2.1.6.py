# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def preguntar_nombre():
    try:
        nombre = input("Introduce el nombre: ")
        return nombre
    except ValueError:
        return preguntar_nombre()

def preguntar_sexo():
    try:
        sexo = input("Introduce el sexo (Escribir H o M): ")
        return sexo
    except ValueError:
        return preguntar_sexo()
    
def procesar_grupo(nombre:str, sexo:str):
    if sexo == "M":
        if nombre[0].upper() < "M":
            grupo = "A"
        else:
            grupo = "B"

    if sexo == "H":
        if nombre[0].upper() > "N":
            grupo = "A"
        else:
            grupo = "B"
    
    return grupo

def salida(grupo):
    print("Perteneces al grupo -->", grupo)

def main():
    # Entrada
    nombre = preguntar_nombre()
    sexo = preguntar_sexo()

    # Procesamiento
    grupo = procesar_grupo(nombre, sexo)

    # Salida
    salida(grupo)


if __name__ == "__main__":
    main()
