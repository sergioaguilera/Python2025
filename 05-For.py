"""Lesson: For / For else """

apples = input("How many apples do you have?:")
print("lets count it!!")
apples = int(apples)
alot = 20
even = 0
even = int(even)

for counting in range(apples):
    print(f"""{counting+1} Apple(s)""")
    even = even+1
    if even % 2 == 0:
        print(f"{even} is an even number!")

if apples >= 20:
    print(f"""Wow! you have {apples} of apples, these are a lot!""")

print("Created by: Sergio.aaguilera@gmail.com.")
print("October 2025.")
