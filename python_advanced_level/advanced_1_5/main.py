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

