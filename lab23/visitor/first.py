class Employee:

    def getSalry(self) -> float:
        pass


class StaffList(Employee):
    def __init__(self):
        self._salaries = []

    def addEmployee(self, employee):
        self._salaries.append(employee)

    def getSalary(self) -> float:
        sum = 0
        for i in self._salaries:
            sum += i.getSalary()
        return sum

    def accept(self, visitor):
        for employee in self._salaries:
            visitor.visit_list(employee)


class Manager:
    def __init__(self, salary):
        self._salary = salary

    def setSalary(self, salary):
        self._salary = salary

    def getSalary(self) -> float:
        return self._salary

    def accept(self, visitor):
        visitor.visit_manager(self)


class ITSupport:
    def __init__(self, salary):
        self._salary = salary

    def setSalary(self, salary):
        self._salary = salary

    def getSalary(self) -> float:
        return self._salary

    def accept(self, visitor):
        visitor.visit_itsupport(self)


class SalaryDownVisitor:
    def __init__(self, rate):
        self.rate = rate

    def visit_list(self,  manager):
        if isinstance(manager, ITSupport):
            self.visit_itsupport(manager)
        if isinstance(manager, Manager):
            self.visit_manager(manager)

    def visit_itsupport(self, manager):
        manager.setSalary(manager.getSalary() * (1 - self.rate))

    def visit_manager(self, manager):
        manager.setSalary(manager.getSalary() * (1 - self.rate))


salary_up = SalaryDownVisitor(0.05)
team = StaffList()
team.addEmployee(Manager(5000))
team.addEmployee(ITSupport(3500))
print("Team salary before: {}".format(team.getSalary()))
team.accept(salary_up)
print("Team salary after: {}".format(team.getSalary()))
