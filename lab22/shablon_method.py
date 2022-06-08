class Creature:
    def defend_against_attack(self):
        self.pick_up_weapon()
        self.defense_action()
        self.move_to_safety()

    def pick_up_weapon(self):
        pass

    def defense_action(self):
        pass

    def move_to_safety(self):
        pass


class Pirate(Creature):
    def pick_up_weapon(self):
        print("Pick up sword")

    def defense_action(self):
        print("Defend with sword")

    def move_to_safety(self):
        print("Return to the ship")


class Troll(Creature):
    def pick_up_weapon(self):
        print("Pick up club")

    def defense_action(self):
        print("Defend with club")

    def move_to_safety(self):
        print("Return to the mountain")


print("Pirate:")
pirate = Pirate()
pirate.defend_against_attack()
print("Troll:")
troll = Troll()
troll.defend_against_attack()
