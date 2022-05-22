class Vehicle:
    def __init__(self, age=0, model="default", damaged=0, mileage=0):
        self.age = age
        self.model = model
        self.damaged = damaged
        self.mileage = mileage

    def get_age(self):
        return self.age

    def get_model(self):
        return self.model

    def get_damaged(self):
        return self.damaged

    def get_mileage(self):
        return self.mileage


class VehicleCalculator:
    def set_vehicle(self, vehicle):
        pass

    def calculate_price(self) -> tuple:
        pass


class Car(Vehicle):
    def __init__(self, age, model, damaged):
        super(Car, self).__init__(age, model, damaged, 0)


class CarCalculator(VehicleCalculator):
    averageCarPrice = 6000
    vehicle = None

    def get_retail_price(self):
        assert self.vehicle != None

        if self.vehicle.get_model() == "Ford":
            return 3000
        elif self.vehicle.get_model() == "BMW":
            return 5000
        else:
            return self.averageCarPrice

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def calculate_price(self) -> tuple:
        assert self.vehicle != None
        price = self.vehicle.get_damaged() * max(self.get_retail_price() - (self.vehicle.get_age() * 100), 0)
        return price, "USD"


class Auto(Vehicle):

    def create_from_another_transport(self, vehicle):
        self.age = vehicle.age
        self.model = vehicle.model
        self.damaged = vehicle.damaged
        self.mileage = vehicle.mileage


class Customs:

    def vehiclePrice(self, auto: Auto) -> tuple:
        car_calculator = CarCalculator()
        car_calculator.set_vehicle(auto)
        return car_calculator.calculate_price()

    def tax(self, auto: Auto) -> tuple:
        # add 15% and convert to uah
        price_usd = self.vehiclePrice(auto)
        return price_usd[0]*1.15*30, 'UAH'


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


if __name__ == "__main__":

    objects = []
    car_calculator = CarCalculator()
    car = Car(1, 'Ford', 1)
    car_calculator.set_vehicle(car)
    objects.append(Adapter(car, price=car_calculator.calculate_price()))
    car = Car(5, 'BMW', 1)
    car_calculator.set_vehicle(car)
    objects.append(Adapter(car, price=car_calculator.calculate_price()))
    print("For USA")
    for obj in objects:
        print("For {0} costing is {1}".format(obj.model, obj.price))

    print("For Ukraine")
    for obj in objects:
        auto = Auto()
        auto.create_from_another_transport(obj)
        print("For {0} costing is {1}".format(obj.model, Customs().tax(auto)))
