# ========================4. Creating Immutable Classes In Python======================

class ImmutableRobot:
    def __init__(self, name, brandname):
        self.__name = name
        self.__brandname = brandname

    def getName(self):
        return self.__name

    def getBrandName(self):
        return self.__brandname


robot = ImmutableRobot(name="RoboX", brandname="TechBot")
print(robot.getName())
print(robot.getBrandName())