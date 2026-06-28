#================1. Lambda — anonymous functions===============
square = lambda x: x * x
print(square(3))


#==============2. map() — transform every item===========
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

names = ["John", "Michael", "David"]
names_copy = dict(map(lambda x: (x, x[::-1]), names))
print(names_copy)

def celsius_to_fahrenheit(temp):
    return (temp - 32) * 5 / 9 + 32

temps = [0, 20, 37, 100]
converted = list(map(celsius_to_fahrenheit, temps))
print(converted)


#================3. filter() — keep only matching items====================
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

words = ["cat", "elephant", "dog", "rhinoceros", "ox"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)


#===================4. reduce() — collapse to a single value=================
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)
print(total)

price_total = reduce(lambda x,y: x + y, numbers, 100)
print(price_total)


nums = [3, 7, 2, 9, 1]
maximum = reduce(lambda x,y: x if x > y else y, nums)
print(maximum)

numbers = [1, 2, 3, 4, 5, 6, 7]
result = reduce(
    lambda x, y: x * y,
    map(
        lambda num: num ** 2,
        filter(
            lambda num: num % 2 != 0,
            numbers
        )
    )
)
print(result)


#====================Exercise 1: Name formatter================
print(20 * "*")

names = ["alice", "BOB", "cHaRliE", "DIANA"]

title_case = list(map(lambda name: name.title(), names))
print(title_case)



#==================Exercise 2: Score filter===================
scores = {"Alice": 85, "Bob": 55, "Charlie": 72, "Diana": 40, "Eve": 91}
filter_score = list(filter(lambda score: score[1] >= 70, scores.items()))
names = [name for name, score in filter_score]
print(names)




#+==================Exercise 3: Shopping cart total=======================

shopping_cart = [("book", 12, 3), ("laptop", 999, 1), ("pen", 2, 10), ("headphones", 79, 1), ("notebook", 8, 5)]

total_price = reduce(
    lambda x, y: x + y,
    map(
        lambda item: item[1] * item[2],
        filter(
            lambda item: item[1] <= 50,
            shopping_cart
        )

    )
)

print(total_price)


#=========+Exercise 1: Filter and Capitalize==============
employees = [("alice", "HR", "active"), ("bob", "IT", "inactive"), ("charlie", "Sales", "active")]

active_employees = list(
    map (
        lambda employee: employee[0].title(),
        filter(
            lambda employee: employee[2] == "active",
            employees
        )
    )
)

print(active_employees)


#============Exercise 2: Calculate Stock Value==============

inventory = [(101, "Desk", 150, 4), (102, "Chair", 45, 12), (103, "Lamp", 25, 0)]

total_cost = reduce(
    lambda x, y: x + y,
    map(
        lambda item: item[2] * item[3],
        filter(
            lambda item: item[3] > 0,
            inventory
        )
    )
)
print(total_cost)


#===============Exercise 3: Filter by Text Length===============

usernames = ["al", "bob_99", "cj", "developer_one", "user4"]

covert_usernames = list(map(
    lambda user: user.upper(),
    filter(
        lambda user: len(user) > 3,
        usernames
    )
))
print(covert_usernames)


