class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Imprimir el beneficio actual"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Devuelve el total calculado de las monedas insertadas."""
        print("Por favor inserte las monedas.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Devuelve True cuando se acepta el pago, o False si es insuficiente."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Lo siento, no es suficiente dinero. Dinero reembolsado.")
            self.money_received = 0
            return False