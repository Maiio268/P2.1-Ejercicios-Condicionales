# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        return edad
    except ValueError:
        print("ERROR. Introduce el tipo de dato correcto")
        return pedir_edad()
    
def pedir_ingresos():
    try:
        ingresos_mensuales = float(input("Introduce tus ingresos mensuales: "))
        return ingresos_mensuales
    except ValueError:
        print("ERROR. Introduce el tipo de dato correcto")
        return pedir_ingresos()

def procesar_condiciones(edad:int, ingresos_mensuales:float):
    if edad > 16:
        edad_valida = 1
    else:
        edad_valida = 0
    
    if ingresos_mensuales >= 1000:
        ingresos_valido = 1
    else:
        ingresos_valido = 0
    
    return edad_valida, ingresos_valido

def salida(edad_valida:bool, ingresos_valido:bool):
    if edad_valida == 1 and ingresos_valido == 1:
        print("Tienes que tributar, ya que eres mayor de 16 años y tienes ingresos superiores a 1000 € mensuales")
    else:
        print("No tienes que tributar")

def main():
    # Entrada
    edad = pedir_edad()
    ingresos_mensuales = pedir_ingresos()

    # Procesamiento
    edad_valida, ingresos_valido = procesar_condiciones(edad, ingresos_mensuales)

    # Salida
    salida(edad_valida, ingresos_valido)

if __name__ == "__main__":
    main()