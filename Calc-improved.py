"""Exercise:Calc improved
The user needs to enter a number, if not enter a  number the app doesnt will stop.
Then he needs to enter a kind of operation
Then a second number
Finally you will show the total
"""
execute = True
print("Calc 2.0 - Now you can execute just the operation that you needs :) ")
while execute:
    n1 = input("Enter the first number: ")
    n1 = int(n1)
    operation = input(" select an operation[add/sub/mult/div]: ")
    n2 = input("Enter the second number: ")
    n2 = int(n2)
    total = int(0)

    if operation == "add":
        total = n1+n2
        print(f"""The total is {total}""")
        execute = False
    elif operation == "sub":
        total = n1-n2
        print(f"""The total is {total}""")
        execute = False
    elif operation == "mult":
        total = n1*n2
        print(f"""The total is {total}""")
        execute = False
    elif operation == "div":
        total = n1/n2
        print(f"""The total is {total}""")
        execute = False


print("Created by: Sergio.aaguilera@gmail.com.")
print("October 2025.")
