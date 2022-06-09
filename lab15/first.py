class Command():
    def __init__(self, dev):
        self.dev = dev

    def do(self):
        pass


class CommandOn(Command):
    def do(self):
        self.dev.light_on()


class CommandOff(Command):
    def do(self):
        self.dev.light_off()


class Controller:
    def __init__(self, on_, off_):
        self.on_ = on_
        self.off_ = off_

    def on(self):
        self.on_.do()

    def off(self):
        self.off_.do()


class Lamp:
    def __init__(self, name="my lamp"):
        self.name = name
        self.is_on = False

    def light_on(self):
        if not self.is_on:
            print("{} is on".format(self.name))
            self.is_on = True

    def light_off(self):
        if self.is_on:
            print("{} is off".format(self.name))
            self.is_lamp_on = False


lamp = Lamp()
controller = Controller(CommandOn(lamp), CommandOff(lamp))

controller.on()
controller.on()
controller.off()
controller.on()
