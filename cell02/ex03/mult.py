print("Enter the first number:")
number1 = int(input())

print("Enter the second number:")
number2 = int(input())
multnumber = number1 * number2

print(f"{number1} X {number2} = {multnumber}")

if multnumber == 0:
    print("The result is positive and negative.")
elif multnumber < 0:
    print("The result is negative.")
else:
    print("The result is positive.")