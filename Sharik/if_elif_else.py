# Program to find the largest among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)
elif b > a and b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# Check if a number is positive, and whether it is even or odd

num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
else:
    print("Number is not positive.")
