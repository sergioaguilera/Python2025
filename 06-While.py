"""Lesson: While 
Same excercise but with a little improvement, now it only shows the line 19 if are more than 19 apples, and using a while.
"""

apples = input("How many apples do you have?:")
print("lets count it!!")
apples = int(apples)
counting = int(0)

if apples <= 19:
    while counting < apples:
        counting = counting+1
        print(f"""{counting} Apple(s)""")
        if counting % 2 == 0:
            print(f"{counting} is an even number!")
else:
    print(f"""Wow! you have {apples} of apples, these are a lot!""")


print("Created by: Sergio.aaguilera@gmail.com.")
print("October 2025.")
