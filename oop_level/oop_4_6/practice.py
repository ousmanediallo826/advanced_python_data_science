#=================Exercise 1: The Product Inventory (dataclass)===================
import uuid
from dataclasses import dataclass, field, FrozenInstanceError
from uuid import UUID

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    serial_number: str = field(default=uuid.uuid1().hex)


    @property
    def total_value(self):
        return self.price * self.quantity


p1 = Product(name="Mechanical Keyboard", price=120.0, quantity=5)
p2 = Product(name="Ergonomic Mouse", price=80.0)
print(p1.total_value)
print(p2.quantity)
print(p1.serial_number)






#================Exercise 2: The Smart Home Device (dataclass)=========================

@dataclass(frozen=True)
class SmartDevice:
    device_id: str
    device_type: str
    wattage: float


    def __post_init__(self):
        if self.wattage <= 0:
            raise ValueError("wattage must be positive")
lamp = SmartDevice(device_id="L-101", device_type="Lamp", wattage=15.5)

try:


    lamp.device_type = "Smart Bulb"


except FrozenInstanceError:
    print("Success! Python successfully blocked the modification and raised a FrozenInstanceError.")

else:
    print("Failure: The attribute was changed, meaning the dataclass is NOT frozen.")




