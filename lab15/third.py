class Command:
    def __init__(self, goal):
        self._goal = goal

    def do(self):
        pass


class CommandOn(Command):
    def do(self):
        self._goal.on()


class CommandOff(Command):
    def do(self):
        self._goal.off()


class CommandVolumeUp(Command):
    def do(self):
        self._goal.vol_up()


class CommandVolumeDown(Command):
    def do(self):
        self._goal.vol_down()


class CommandNextChannel(Command):
    def do(self):
        self._goal.next_channel()


class CommandPrevChannel(Command):
    def do(self):
        self._goal.prev_channel()


class Device:
    def on(self):
        pass

    def off(self):
        pass

    def vol_up(self):
        pass

    def vol_down(self):
        pass

    def next_channel(self):
        pass

    def prev_channel(self):
        pass


class Radio(Device):
    def __init__(self):
        self._is_on = False
        self._channel = 12
        self._volume = 5

    def on(self):
        if self._is_on:
            return
        self._is_on = True

    def off(self):
        if not self._is_on:
            return
        self._is_on = False

    def vol_up(self):
        if not self._is_on:
            return
        self._volume += 1
        print('Radio new volume = {}'.format(self._volume))

    def vol_down(self):
        if not self._is_on:
            return
        self._volume -= 1
        print('Radio new volume = {}'.format(self._volume))

    def next_channel(self):
        if not self._is_on:
            return
        self._channel += 1
        print('Radio new channel = {}'.format(self._channel))

    def prev_channel(self):
        if not self._is_on:
            return
        self._channel -= 1
        print('Radio new channel = {}'.format(self._channel))


class TV(Device):
    def __init__(self):
        self._is_on = False
        self._volume = 5
        self._channel = 12

    def on(self):
        if self._is_on:
            return
        self._is_on = True

    def off(self):
        if not self._is_on:
            return
        self._is_on = False

    def vol_up(self):
        if not self._is_on:
            return
        self._volume += 1
        print('TV new vol = {}'.format(self._volume))

    def vol_down(self):
        if not self._is_on:
            return
        self._volume -= 1
        print('TV  new vol = {}'.format(self._volume))

    def next_channel(self):
        if not self._is_on:
            return
        self._channel += 1
        print('TV new channel = {}'.format(self._channel))

    def prev_channel(self):
        if not self._is_on:
            return
        self._channel -= 1
        print('TV new channel = {}'.format(self._channel))


class ControllerBase:
    def device_on(self):
        pass

    def device_off(self):
        pass

    def device_vol_up(self):
        pass

    def device_vol_down(self):
        pass

    def device_next_channel(self):
        pass

    def device_prev_channel(self):
        pass


class Controller(ControllerBase):
    def __init__(self, goal):
        self._on = []
        self._off = []
        self._vol_up = []
        self._vol_down = []
        self._next_ch = []
        self._prev_ch = []
        if isinstance(goal, Device):
            self._on.append(CommandOn(goal))
            self._off.append(CommandOff(goal))
            self._vol_up.append(CommandVolumeUp(goal))
            self._vol_down.append(CommandVolumeDown(goal))
            self._next_ch.append(CommandNextChannel(goal))
            self._prev_ch.append(CommandPrevChannel(goal))
        elif isinstance(goal, list):
            for t in goal:
                self._on.append(CommandOn(t))
                self._off.append(CommandOff(t))
                self._vol_up.append(CommandVolumeUp(t))
                self._vol_down.append(CommandVolumeDown(t))
                self._next_ch.append(CommandNextChannel(t))
                self._prev_ch.append(CommandPrevChannel(t))

    def device_on(self):
        for command in self._on:
            command.do()

    def device_off(self):
        for command in self._off:
            command.do()

    def device_vol_up(self):
        for command in self._vol_up:
            command.do()

    def device_vol_down(self):
        for command in self._vol_down:
            command.do()

    def device_next_channel(self):
        for command in self._next_ch:
            command.do()

    def device_prev_channel(self):
        for command in self._prev_ch:
            command.do()

tv = TV()
radio = Radio()

controller_tv = Controller(tv)
controller_radio = Controller(radio)

controller_universal = Controller([tv, radio])

controller_tv.device_on()
for i in range(3):
    controller_tv.device_next_channel()

controller_tv.device_vol_down()

controller_radio.device_on()

for i in range(3):
    controller_radio.device_vol_down()
controller_radio.device_next_channel()

controller_universal.device_off()
