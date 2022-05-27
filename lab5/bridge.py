class Beverage:
    def __init__(self, sugar):
        self.sugar = sugar

    def prepare(self):
        pass

    def drink(self):
        pass

    def cost(self) -> int:
        pass


class Tee(Beverage):
    def __init__(self, sugar=0):
        super().__init__(sugar)

    def prepare(self):
        print('Put some tee...')

    def cost(self) -> int:
        return 7


class BlackTee(Tee):
    def __init__(self, sugar, water_volume):
        super().__init__(sugar)
        self.water_volume = water_volume

    def drink(self):
        print('"Drink black tee!')

    def prepare(self):
        super().prepare()
        print('Put some hot watter: {}'.format(self.water_volume))
        print('Put some sugar: {}'.format(self.sugar)) if self.sugar else None

    def cost(self):
        return super().cost()


class TeeWithMilk(Tee):
    def __init__(self, sugar, milk_volume=1):
        super().__init__(sugar)
        self.milk_volume = milk_volume

    def drink(self):
        print('"Drink tee with milk!')

    def prepare(self):
        super().prepare()
        print('Put some milk: {}'.format(self.milk_volume))
        print('Put some sugar: {}'.format(self.sugar)) if self.sugar else None

    def cost(self):
        return super().cost() + self.milk_volume/20


class Bridge:
    def __init__(self, type, beverage):
        self._type = type # inside or outside
        self._beverage = beverage

    def prepare(self):
        self._beverage.prepare()
        print('For {}'.format(self._type))

    def cost(self):
        return self._beverage.cost()

    def drink(self):
        self._beverage.drink()


beverage = TeeWithMilk(1)
beverage1 = Bridge('inside', beverage)
beverage1.prepare()
print('cost - ' + str(beverage1.cost()))
beverage1.drink()
