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