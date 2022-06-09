class Command():
    def __init__(self, aim):
        self._aim = aim

    def do(self):
        pass


class CommandOff(Command):
    def do(self):
        self._aim.light_off()


class CommandOn(Command):
    def do(self):
        self._aim.light_on()


class Lamp:
    def __init__(self, room):
        self._room = room
        self._is_light_on = False
        self._is_light_off = False

    def light_on(self):
        if self._is_light_on:
            return
        self._is_light_on = True
        print('Light"s on in {}'.format(self._room))

    def light_off(self):
        if self._is_light_off:
            return
        self._is_light_off = True
        print('Light"s off in {}'.format(self._room))


class Controller:
    def __init__(self, goal):
        self._commands_on = []
        self._commands_off = []
        if isinstance(goal, Lamp):
            self._commands_on.append(CommandOn(goal))
            self._commands_off.append(CommandOff(goal))
        elif isinstance(goal, list):
            for t in goal:
                self._commands_on.append(CommandOn(t))
                self._commands_off.append(CommandOff(t))

    def on(self):
        for command in self._commands_on:
            command.do()

    def off(self):
        for command in self._commands_off:
            command.do()


bd_lamp = Lamp('Kitchen')
bath_lamp = Lamp('Bathroom')

controller_bedroom_lamp = Controller(goal=bd_lamp)
controller_bathroom_lamp = Controller(goal=bath_lamp)

controller_universal = Controller(goal=[bd_lamp, bath_lamp])

controller_bedroom_lamp.on()
controller_bedroom_lamp.off()

controller_bedroom_lamp.on()
controller_bathroom_lamp.on()

controller_universal.off()
