#=================6. Decorators and Decoration=======================
def whisper(text):
    return text.lower()

def greet(func):
    def wrapper():
        message = func("Hello World!")
        return message
    return wrapper

print(greet(whisper))


def multiplier_factory(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier_factory(2)
print(double(10))


def my_decorator(func):
    def wrapper():
        print("[Before] Injecting security clearance validation...")
        func()
        print("[After] Logging activity history...")
    return wrapper

@my_decorator
def fetch_data():
    print("-> Fetching secure payroll files database...")
fetch_data()



def audit_log(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__} with inputs: {args}")
        result = func(*args, **kwargs)
        print(f"Execution complete.")
        return result
    return wrapper

@audit_log
def calculate_tax(salary, state="NY"):
    return salary * 0.08

print(calculate_tax(100000, state="CA"))


from functools import wraps

def tag_decorators(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<h1>{func(*args, **kwargs)}</h1>"
    return wrapper


def repeat(num_times):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat(num_times=3)
def ping():
    print("Pong!")
ping()


#====Challenge 1: Type Checking Validator===
def require_integers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if type(args[1]) is not int:
            raise TypeError("Integer required")
        return func(*args, **kwargs)
    return wrapper

@require_integers
def multiply(a, b):
    return a * b

print(multiply(5, 10))
# print(multiply(5, "hello"))


#===Challenge 2: API Call Speed Monitor===

import time

def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = end_time - start_time
        print(f"[Performance Monitor] '{func.__name__}' took {duration:.6f} seconds to execute.")
        return result
    return wrapper

@time_execution
def add(a, b):
    time.sleep(0.1)
    return a + b

print(f"Result: {add(10, 20)}")

print(add(10, 20))



#=======7. Memoization and Decorators=======
from functools import wraps, lru_cache
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"[Cache HIT] Returning cached result for inputs {args}")
            return cache[args]
        print(f"[Cache MISS] Calculating result for inputs {args}")
        result = func(*args)
        cache[args] = result
    return wrapper

@memoize
def expensive_calculation(n):
    return n * 2

print(expensive_calculation(10))
print(expensive_calculation(10))
print(expensive_calculation(20))

@lru_cache(maxsize=128)
def fetch_user_profile(user_id):
    return f"User Profile Data for {user_id}"


#===Practice Problem: The Factorial Speed Test===
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"[Cache HIT] Returning cached result for inputs {args}")
            return cache[args]
        print(f"[Cache MISS] Calculating result for inputs {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))
print(factorial(6))


#================8. Functional Programming OOP=======================

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


user1 = User("Ousmane", "User")
user1.role = "Admin"
print(user1.username)
print(user1.role)

from dataclasses import dataclass, replace

@dataclass(frozen=True)
class ImmutableUser:
    username: str
    role: str


user1 = ImmutableUser("Ousmane", "User")
user2 = replace(user1, role="Admin")
print(user2.username)
print(user2.role)




#===================9. List Comprehension=========================
squares = []
for x in range(1,10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(1,10)]
print("squares:", squares)



numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = [x for x in numbers if x % 2 ==0]
print("evens",evens)


labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1,10)]
print("labels", labels)

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat_list = [element for row in matrix for element in row]
print("flat_list", flat_list)


#===Problem 1: The Domain Email Extractor===
emails = ["user1@gmail.com", "admin@company.org", "dev@yahoo.com", "info@school.edu"]
domains = [domain.split("@")[1] for domain in emails  if domain.endswith("com")]
print("domains", domains)

#===Problem 2: Transposing Coordinates====
coords = [[-1, 10], [2, 20], [0, 30], [4, 40]]

flipped_cords = [(x,y) for x, y in coords if x > 0]
print("flipped_cords", flipped_cords)








#=========================Dictionary & Set Comprehensions===================
cubes = {x: x**3 for x in range(1, 10)}
print("cubes", cubes)


original = {"admin": 101, "editor": 102, "guest": 103}
inverted = {v: k for k, v in original.items()}
print("original", original)
print("inverted", inverted)


filenames = ["data.csv", "LOG.txt", "script.py", "backup.CSV", "notes.TXT"]

unique_ext = {flip.split(".")[1] for flip in filenames}
print("unique_ext", unique_ext)

#====Problem 1: The ID Filter (Dictionary Comprehension)=====

employees = {"Alice": True, "Bob": False, "Charlie": True, "David": False}
active_uppercase = {name: active for name, active in employees.items() if active == True}
print("active_uppercase", active_uppercase)



#+===Problem 2: The Character Unique Scanner (Set Comprehension)====
words = "Supercalifragilisticexpialidocious"
vowels = 'a', 'e', 'i', 'o', 'u'
unique_vowels = {word for word in words if word in vowels}
print("unique_vowels", unique_vowels)



#===================Context Managers======================
file = open("data.csv", "w")
try:
    file.write("Processing sensitive data...")
finally:
    file.close()


with open("text.txt", "w") as file:
    file.write("Processing sensitive data...")


class DataConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"[ENTER] Connecting to database: {self.db_name}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[EXIT] Disconnecting from database: {self.db_name}...")

        if exc_type:
            print(f"-> A crash occurred: {exc_val}. Cleaning up connection safely.")
        return True



with DataConnection("production_db") as pd:
    print("   Inside the with block: Fetching user metrics...")

    raise RuntimeError("Lost network packet connection.")

print("Program successfully continued running because __exit__ handled the error!")

from contextlib import contextmanager

@contextmanager
def simple_file_manager(filename, mode):
    print(f"Opening {filename}...")
    file_obj = open(filename, mode)
    try:
        yield file_obj
    finally:
        print(f"Closing {filename}...")
        file_obj.close()


with simple_file_manager("test.txt", "w") as f:
    f.write("Hello from contextlib!")


class Transaction:

    def __enter__(self):
        print(f"[START] Beginning Database Transaction")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"   Inside the with block: Fetching Transaction metrics...")

        if exc_type:
            print("[ROLLBACK] Undoing partial database writes!")

        else:
            print("[COMMIT] Saving changes permanently!")
        return True


with Transaction() as tx:
    print("Writing user details...")

print("-" * 20)
with Transaction() as tx:
    print("Writing item stock...")
    raise ValueError("Invalid item count detected.")



#=========================11. Currying in Python==========================

def standard_add(x,y, z):
    return x + y + z

def curried_add(x):
    def next_y(y):
        def next_z(z):
            return x + y + z
        return next_z
    return next_y


print(standard_add(1, 2, 3))
print(curried_add(1)(2)(3))


curried_multiply = lambda x: lambda y: x * y
double = curried_multiply(2)
triple = curried_multiply(3)
print(triple(20))
print(double(30))







#=======================15. Regular Expressions======================
import re

text = "The agent code is secret 007 agent."

pattern = r"\d\d\d"

match = re.search(pattern, text)
if match:
    print(f"Found a match: {match.group()}")


log_data = "Error on device ABC-9812 at terminal station."
pattern = r"\w{3}-\d{4}"

match = re.search(pattern, log_data)
if match:
    print(f"Found a match: {match.group()}")


invoice = "The ledger includes laptop ($999), mouse ($25), and secondary monitor ($200)."

pattern = r"\$\d+"
match = re.findall(pattern, invoice)
if match:
    print(f"Found a match: {match}")


contact_sheet = "Call office lines at 555-123-4567 or emergency dispatch at 800-555-9999 immediately."

phone_pattern = r"\d{3}-\d{3}-\d{4}"

numbers= re.findall(phone_pattern, contact_sheet)
print(numbers)


tweet = "Learning #python programming is amazing! #coding #regex_mastery2026"

hashtag_pattern = r"#\w+"
hashtags = re.findall(hashtag_pattern, tweet)
print(hashtags)


#======================16. Advanced Regular Expressions==========================

import re

log_data = "LOG_2026: [ERROR] Code:404 at runtime. [WARNING] Code:200 during boot."

pattern = r"\[(\w+)\] Code:(\d+)"
for match in re.finditer(pattern, log_data):
    full_match = match.group(0)
    status_level = match.group(1)
    error_code = match.group(2)
    print(f"Matched: '{full_match}' -> Level: {status_level}, Code: {error_code}")

