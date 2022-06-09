class Beverage:
    def description(self):
        pass

    def cost(self):
        pass

    def __str__(self):
        return "Beverage: {}; ${}".format(self.description(), self.cost())


class Espresso(Beverage):
    def description(self):
        return "Espresso"

    def cost(self):
        return 0.75


class DarkRoast(Beverage):
    def description(self):
        return "Dark Roast"

    def cost(self):
        return 1


class Decaf(Beverage):
    def description(self):
        return "Decaf"

    def cost(self):
        return 0.5


class AddOnDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage


class Milk(AddOnDecorator):
    def description(self):
        return self._beverage.description() + ", milk"

    def cost(self):
        return self._beverage.cost() + 0.2


class Sugar(AddOnDecorator):
    def __init__(self, beverage, amount: int = 1):
        super().__init__(beverage)
        self._amount = amount

    def description(self):
        return self._beverage.description() + ", sugar x {}".format(self._amount)

    def cost(self):
        return self._beverage.cost()


class Creme(AddOnDecorator):
    def description(self):
        return self._beverage.description() + ", creme"

    def cost(self):
        return self._beverage.cost() + 0.15


class Whip(AddOnDecorator):
    def description(self):
        return self._beverage.description() + ", whip"

    def cost(self):
        return self._beverage.cost() + 0.34


coffee = Espresso()
coffee = Sugar(coffee, 2)
print(coffee)

coffee = DarkRoast()
coffee = Whip(coffee)
coffee = Sugar(coffee, 2)
print(coffee)

coffee = DarkRoast()
coffee = Creme(coffee)
coffee = Sugar(coffee)
print(coffee)

coffee = Decaf()
coffee = Milk(coffee)
coffee = Sugar(coffee, 3)
print(coffee)
