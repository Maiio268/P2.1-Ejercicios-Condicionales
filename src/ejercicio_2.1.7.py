# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
'''
    ___Renta___	        ___Tipo impositivo___
Menos de 10000€	                5%
Entre 10000€ y 20000€	        15%
Entre 20000€ y 35000€	        20%
Entre 35000€ y 60000€	        30%
Más de 60000€	                45%
'''
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def entrada():
    try:
        renta = float(input("Introduce tu renta anual: "))
        return renta
    except ValueError:
        return entrada()
    
def procesar_impositivo(renta:float):
    if renta < 10000:
        return "5%"
    elif 10000 < renta < 20000:
        return "15%"
    elif 20000 < renta < 35000:
        return "20%"
    elif 35000 < renta < 60000:
        return "30%"
    elif renta > 60000:
        return "45%"

def salida(impositivo:str):
    print("El tipo de impositivo correspondiente es:", impositivo)


def main():
    # Entrada
    renta = entrada()

    # Procesamiento
    impositivo = procesar_impositivo(renta)

    # Salida
    salida(impositivo)

if __name__ == "__main__":
    main()