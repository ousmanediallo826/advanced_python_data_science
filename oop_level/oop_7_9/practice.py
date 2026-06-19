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




#=======Exercise 1: Magic Methods (The "Smart Playlist")================

class Playlist:
    def __init__(self, name: str, songs: list):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"PlayList: {self.name}, {[ {song} for i, song in enumerate(self.songs)]}"

    def __add__(self, other):
        return Playlist(self.name + other.name, self.songs + other.songs)

    def __getitem__(self, position):
        return self.songs[position]



rock = Playlist("80s Rock", ["Jump", "Livin' on a Prayer"])
pop = Playlist("Modern Pop", ["Blinding Lights", "Jump"])

print(rock)

mega_mix = rock + pop
print(mega_mix)

print(mega_mix[2])


#===================Exercise 2: Dynamic Data Transformation (The "API Payload Sanitizer")===============

def sanitize_payload(raw_data, blueprint):
    transformed_data = {}

    for raw_key, (new_key, transform_func) in blueprint.items():
        if raw_key in raw_data:
            raw_value = raw_data[raw_key]
            transformed_data[new_key] = transform_func(raw_value)
        else:
            transformed_data[new_key] = None
    return transformed_data



RAW_API_RESPONSE = {
    "user_identifier": "10492",
    "USER_EMAIL": "  Alex@Example.com ", # Needs whitespace stripping
    "account_balance_usd": "150.50",     # Needs to be a float
    "unnecessary_spy_metadata": "xyz123" # Should be dropped
}

BLUEPRINT = {
    "user_identifier": ("id", int),
    "USER_EMAIL": ("email", lambda s: s.strip().lower()),
    "account_balance_usd": ("balance", float),
    "missing_profile_pic": ("avatar_url", str) # Not in payload, should become None
}

clean_data = sanitize_payload(RAW_API_RESPONSE, BLUEPRINT)
print(clean_data)