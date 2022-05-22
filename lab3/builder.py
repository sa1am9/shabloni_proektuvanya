class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPizza(self):
        pizza = Pizza()

        # First goes the body
        body = self.__builder.getBody()
        pizza.setBody(body)

        # And products
        filling = self.__builder.getFilling()
        pizza.attachFilling(filling)

        return pizza


# The whole product
class Pizza:
    def __init__(self):
        self.__filling = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachFilling(self, filling):
        self.__filling = filling

    def specification(self):
        print("size: {}".format(self.__body.size))
        print("filling is: {}".format(", ".join(self.__filling.product)))


class Builder:
    def getFilling(self): pass

    def getBody(self): pass


class PizzaBuilder(Builder):
    def __init__(self, size, products):
        self._size = size
        self._products = products

    def getFilling(self):
        wheel = Filling()
        wheel.product = self._products
        return wheel

    def getBody(self):
        body = Body()
        body.size = self._size
        return body


# Pizza parts
class Filling:
    product = None


class Body:
    size = None


def main():
    pizza_builder = PizzaBuilder('small', ['chicken', 'banana'])  # initializing the class

    director = Director()

    # Build Pizza
    print("Pizza Hawaii")
    director.setBuilder(pizza_builder)
    pizza = director.getPizza()
    pizza.specification()


if __name__ == "__main__":
    main()
