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