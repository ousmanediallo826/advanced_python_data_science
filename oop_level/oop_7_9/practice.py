class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return f"{self.title} by {self.author}"


book = Book("Project Hail Mary", "Andy Weir")
print(book)



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self):
        return f"Vector({self.x}, {self.y})"



v1 = Vector(1, 2)
v2 = Vector(2, 3)
print(v1 + v2)




class CustomDeck:
    def __init__(self):
        self._cards = ["Ace", "King", "Queen", "Jack"]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = CustomDeck()
print(len(deck))
print(deck[1])



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


user = User("Jay", "jay@speakhire.org")
field_to_extract = "email"

transformed_data = getattr(user, field_to_extract)
print(transformed_data)




RAW_DATA = {"usr_nm": "clark_k", "pwd_hash": "12345", "is_actv": True}

SCHEMA_MAP = {
    "usr_nm": ("username", str),
    "is_actv": ("is_active", bool)

}

def transform_data(raw_dict, schema):
    transformed_data = {}
    for key, value in raw_dict.items():
        for key in schema:
            new_key, type_cast = schema[key]
            transformed_data[new_key] = type_cast(value)
    return transformed_data



print(transform_data(RAW_DATA, SCHEMA_MAP))