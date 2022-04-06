class CoffeeMaker:
    """Modelar la máquina que hace el café"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Imprime un informe de todos los recursos."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """RDevuelve True cuando se puede hacer el pedido, False si los ingredientes son insuficientes."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Lo siento, no hay suficientes {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deduce los ingredientes necesarios de los recursos."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aquí tienes tu {order.name} ☕️. ¡Que lo disfrutes!")
