class MenuItem:
    """Definir cada elemento del menu"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Definir composicion de las bebidas"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Devuelve todos los nombres de los elementos de menú disponibles"""
        options = ""
        for item in self.menu:
            options += f'{item.name}/'
        return options

    def find_drink(self, order_name):
        """Buscar en el menú una bebida determinada por su nombre.
         Devuelve ese elemento si existe, en caso contrario devuelve Ninguno"""
        for item in self.menu:
            if item.name == order_name:
                return item
            print('Lo sentimos, ese artículo no está disponible.')