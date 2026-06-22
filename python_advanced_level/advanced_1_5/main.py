#===============1. Recursive Functions======================
def countdown(n):
    if n <= 0:
        print("Blastoff")
        return

    print(n)
    countdown(n - 1)

countdown(5)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 0: return 0
    if n == 1: return 1


    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

print(fib_memo(50))

#======Practice recursion========
def recursive_sum(numbers):
    if len(numbers) == 0: return 0

    return numbers[0] + recursive_sum(numbers[1:])

print(recursive_sum([1, 2, 3, 4, 5]))


def reversal_string(text):
    if text == "":
        return ""
    return text[-1] + reversal_string(text[:-1])

print(reversal_string("hello"))



#===========2. Iterators and Iterables====================
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)



class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


timer = Countdown(3)

for num in timer:
    print(num)



#===Problem 1: Manual Extraction===
text = "AI"

iterator = iter(text)

while True:
    try:
        texts = next(iterator)
        print(texts)
    except StopIteration:
        break


#===Problem 2: The Custom Multiplier Iterator===
class PowerOfTwo:
    def __init__(self, max_component):
        self.max_component = max_component
        self.exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.exponent == self.max_component:
            raise StopIteration
        result =  2 ** self.exponent
        self.exponent += 1
        return result



for val in PowerOfTwo(5):
    print(val)



#==========3. Generators and Iterators====================
def process_steps():
    print("-> Waking up for Step 1")
    yield "Data Pack A"

    print("-> Waking up for Step 2")
    yield "Data Pack B"


stream = process_steps()

print("Firing first next():")
print(f"Received: {next(stream)}")

print("\nFiring second next():")
print(f"Received: {next(stream)}")


#==Problem 1: The Infinite Multiples Stream====
def infinite_multiples(n):
    multiplier = 1
    while True:
        yield n * multiplier
        multiplier += 1



gen = infinite_multiples(5)
print(next(gen))
print(next(gen))
print(next(gen))


#=====================4. Lambda Operator, filter, reduce and map==================
def square(x):
    return x * x

square_lambda = lambda x: x * x
print(square_lambda(5))
print(square(5))

numbers = [1, 2, 3, 4, 5]
doubled_stream = map(lambda x: x * 2, numbers)
print(list(doubled_stream))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_stream = filter(lambda x: x % 2 == 0, numbers)
print(list(even_stream))


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers)
print(product)

#==Problem 1: The String Cleansing Pipeline (map + filter)==
raw_inputs = ["hi", "alex", "am", "python", "ok"]

clean_stream = map(lambda s: s.upper(), raw_inputs)
filtered_stream = filter(lambda s: len(s) > 3, clean_stream)
print(list(filtered_stream))


#==Problem 2: Finding the Maximum Value (reduce)==
dataset = [12, 45, 2, 67, 34, 9]

max_value = reduce(lambda x,y: x if x > y else y, dataset)
print(max_value)