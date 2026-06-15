# 1. Object Oriented Programming



class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())



# =============================2. Class vs. Instance Attributes=================================
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot.__counter
    @classmethod
    def RoneInstances(cls):
        return cls, Robot.__counter


if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())

    print(Robot.RoneInstances())
    print(Robot.RobotInstances())
    z = Robot()
    print(z.RoneInstances())
    f = Robot()
    print(z.RoneInstances())
    print(Robot.RoneInstances())




#===================3. Properties vs. Getters and Setters=========================
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        print("Fetching salary....")
        return self._salary
    @salary.setter
    def salary(self, value):
        print(f"Attempting to set salary to {value}...")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value



emp = Employee("Henry", 100)
print(emp.salary, emp.name)
emp2 = Employee("Henry", -100)
print(emp2.salary, emp2.name)