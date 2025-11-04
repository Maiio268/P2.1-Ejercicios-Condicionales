# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla 
# si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def entrada():
    return input("Introduce la contraseña: ")

def procesar_contraseña(contrasenia:str, contrasenia_entrada:str):
    if contrasenia_entrada == contrasenia:
        contraseña_valida = True
    else:
        contraseña_valida = False
    return contraseña_valida

def salida(contraseña_valida):
    if contraseña_valida == 1:
        print("La contraseña introducida coincide con la almacenada")
    else:
        print("La contraseña introducida NO coincide con la almacenada")


def main():
    contrasenia = "contraseña"
    # Entrada
    contrasenia_entrada = entrada()
    
    # Procesamiento
    contraseña_valida = procesar_contraseña(contrasenia, contrasenia_entrada)
    
    # Salida
    salida(contraseña_valida)

if __name__ == "__main__":
    main()

