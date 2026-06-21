from dataclasses import dataclass, field
from datetime import datetime
from types import new_class


@dataclass
class Event:
    event_type: str
    payload_dict: dict
    timestamp: float = field(default_factory=datetime.now)

class SubscriberRegistryMeta(type):
    routing_table = {}
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        if name == "EventSubscriber": return new_class

        routing_rules = dct.get("LISTEN_TO", [])
        for event_type in routing_rules:
            if event_type not in cls.routing_table:
                cls.routing_table[event_type] = []
            cls.routing_table[event_type].append(new_class)
        return new_class


class EventSubscriber(metaclass=SubscriberRegistryMeta):
    def handle(self, event: Event):
        raise NotImplementedError("Subscribers must implement handle_event!")


class InventoryManager(EventSubscriber):
    LISTEN_TO = ["ORDER_PLACED"]
    def handle_event(self, event: Event):
        if event.payload_dict:
           print(f"[Inventory] Checking stock for item: {event.payload_dict['item_name']}")

class EmailNotifier(EventSubscriber):
    LISTEN_TO = ["ORDER_PLACED", "ORDER_CANCELLED"]
    def handle_event(self, event: Event):
        print(f"[Email] Sending notification to: {event.payload_dict['email']}")


class EventMeshBroker:
    def __init__(self):
        self.active_subscribers = {}

        routing = SubscriberRegistryMeta.routing_table

        for event_type, subscriber_classes in routing.items():
            self.active_subscribers[event_type] = []
            for cls in subscriber_classes:
                instance = cls()
                self.active_subscribers[event_type].append(instance)


    def publish(self, event: Event):
       if event.event_type in self.active_subscribers:
           execution_stream = map(lambda sub: sub.handle_event(event), self.active_subscribers[event.event_type])
           list(execution_stream)
       else:
           return " No active subscribers"



broker = EventMeshBroker()

print("--- Publishing: ORDER_PLACED ---")
order_payload = {"item_name": "Mechanical Keyboard", "email": "dev@example.com"}
order_event = Event(event_type="ORDER_PLACED", payload_dict=order_payload)
broker.publish(order_event)

print("\n--- Publishing: ORDER_CANCELLED ---")
cancel_event = Event(event_type="ORDER_CANCELLED", payload_dict=order_payload)
broker.publish(cancel_event)