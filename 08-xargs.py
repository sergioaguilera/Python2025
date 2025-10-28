"""Lesson: Xargs
"""


def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


add(2, 20)
add(20, 20, 20, 20)
add(2100, 3040, 234, 21, 20)


print("Created by: Sergio.aaguilera@gmail.com.")
print("October 2025.")
