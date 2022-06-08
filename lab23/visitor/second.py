class GeneralStaff:
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} геренералів та {self.secretPaper} секретних паперів."

    def accept(self, visitor):
        visitor.visit_staff(self)


class MilitaryBase:
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

    def accept(self, visitor):
        visitor.visit_base(self)


class SecretAgent:
    def visit_staff(self, staff):
        print("Тупо винесли {} секретних папирив.".format(staff.secretPaper))

    def visit_base(self, base):
        print("Зібрали інформацію {}.".format(base))


class Saboteur:
    def visit_base(self, base):
        base.soldiers = 0
        print("{} поранено.".format(base.soldiers))

    def visit_staff(self, staff):
        staff.secretPaper = 0
        print("Знищено {} секретних папирив.".format(staff.secretPaper))


generalStaff = GeneralStaff(10, 20)
print(generalStaff)

militaryBase = MilitaryBase(10, 2000, 150, 30)
print(militaryBase)

agent = SecretAgent()
saboteur = Saboteur()

generalStaff.accept(agent)
generalStaff.accept(saboteur)

militaryBase.accept(agent)
militaryBase.accept(saboteur)