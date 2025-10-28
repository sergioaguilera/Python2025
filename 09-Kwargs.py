"""Exercise:Kwargs
A function with the name, the job and the level of your character.
"""
print("Character sheet - Now on python")


def character(**data):
    print(data)


character(name="Dekkek",
          job="Wizard",
          lvl=int(10))

print("Created by: Sergio.aaguilera@gmail.com.")
print("October 2025.")
