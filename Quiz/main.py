num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

for number in range(num1,num2):
    if number % 3 == 0 and number % 5 == 0:
        print(number, "Fizzbuzz")
    elif number % 3 == 0:
        print(number, "Fizz")
    elif number % 5 == 0:
        print(number, "Buzz")
    else:
        print(number)
