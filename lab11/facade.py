class Accelerator:
    def press(self):
        print("Pressing accelerator down")

    def lift(self):
        print("Lifting accelerator up")


class Clutch:
    def press(self):
        print("Pressing clutch down")

    def lift(self):
        print("Lifting clutch up")


class GearStick:
    _gear = 0

    def change_gear(self, gear: int = 0):
        print("Changing gear to ",  gear)
        self._gear = gear


class Handbrake:
    _is_up = True

    def push_down(self):
        print("Pushing down handbrake")
        self._is_up = False

    def lift_up(self):
        print("Lifting up handbrake")
        self._is_up = True


class Ignition:
    _is_on = False

    def turn_on(self):
        print("Turning ignition on")
        self._is_on = True

    def turn_off(self):
        print("Turning ignition off")
        self._is_on = False


class CarFacade:
    def drive(self):
        ignition = Ignition()
        clutch = Clutch()
        accelerator = Accelerator()
        gearStick = GearStick()
        handbrake = Handbrake()

        ignition.turn_on()
        clutch.press()
        gearStick.change_gear(1)
        accelerator.press()
        clutch.lift()
        handbrake.push_down()
        accelerator.press()
        clutch.press()
