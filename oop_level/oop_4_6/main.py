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



#==========================5. Dataclasses In Python+++===============================
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableRobot:
    name: str
    brandname: str


robot1 = ImmutableRobot("Marvin", "NanoGuardian XR-2000")
robot2 = ImmutableRobot("R2D2", "QuantumTech Sentinel-7")
robot3 = ImmutableRobot("Marva", "MachinaMaster MM-42")

robots = {robot1, robot2, robot3}

print("The robots in the set robots:")
for robo in robots:
    print(robo)
activity = {robot1: 'activated', robot2: 'activated', robot3: 'deactivated'}
print("\nAll the activated robots:")
for robo, mode in activity.items():
    if mode == 'activated':
        print(f"{robo} is activated")
