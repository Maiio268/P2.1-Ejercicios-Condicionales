# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
'''
- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú 
con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
def preguntar_tipo_pizza():
    tipo_pizza = input("Pizzas disponibles: Escribe el tipo de pizza que quieres\n--> Vegetariana\n--> No vegetariana\nIntroduce la pizza: ")
    if tipo_pizza.lower() not in ["vegetariana", "no vegetariana"]:
        print("ERROR. Introduce una de las 2 opciones.")
        return preguntar_tipo_pizza()
    return tipo_pizza
            
def elegir_ingrediente(tipo_pizza:str):
    if tipo_pizza.lower() == "no vegetariana":
        print("----Ingredientes disponibles----\n(Solo puedes elegir 1 ingrediente)\n--> Peperoni\n--> Jamón\n--> Salmón")
        ingrediente_elegido = input("Introduce tu ingrediente a elegir: ")
        if ingrediente_elegido.lower() == "peperoni":
            return "peperoni"
        elif ingrediente_elegido.lower() == "jamon":
            return "jamon"
        elif ingrediente_elegido.lower() == "salmon":
            return "salmon"

    if tipo_pizza.lower() == "vegetariana":
        print("----Ingredientes disponibles----\n(Solo puedes elegir 1 ingrediente)\n--> Pimiento\n--> Tofu ")
        ingrediente_elegido = input("Introduce tu ingrediente a elegir: ")
        if ingrediente_elegido.lower() == "pimiento":
            return "pimiento"
        elif ingrediente_elegido.lower() == "tofu":
            return "tofu"

def salida(ingrediente_elegido:str, tipo_pizza:str):
    print("Pizza elegida:", tipo_pizza, "\nIngredientes de la pizza: mozzarella, tomate y", ingrediente_elegido)

def main():
    # Entrada
    tipo_pizza = preguntar_tipo_pizza()
    
    # Procesamiento
    ingrediente_elegido = elegir_ingrediente(tipo_pizza)
    
    # Salida
    salida(ingrediente_elegido, tipo_pizza)

if __name__ == "__main__":
    main()
