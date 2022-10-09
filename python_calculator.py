print("Hello! Welcome to my calculator project. Enjoy!!!")

print("Type 1 to add.")
print("Type 2 to subtract.")
print("Type 3 to multiply.")
print("Type 4 to divide.")

operator = input("Select operator: ")
num1 = float(input("Type a number: "))
num2 = float(input("Type a number: "))

if operator == "1":
    print(num1 + num2)

elif operator == "2":
    print(num1 - num2)

elif operator == "3":
    print(num1 * num2)

elif operator == "4":
    print(num1 / num2)

else:
    print("Invalid operator")
