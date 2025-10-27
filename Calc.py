"""Excercise: Create a calculator"""
n1 = input("enter the first number:")
n2 = input("enter the second number:")
n1 = int(n1)
n2 = int(n2)

add = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2

print(f"""The numbers are {n1} and {n2}
The result of the sum is: {add}
The result of the subtraction is:{sub}
The result of the multiplication is:{mult}
The result of the division is:{div}
""")

print("Created by: Sergio.aaguilera@gmail.com.")
print("October 2025.")
