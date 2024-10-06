import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def trig_function(func, x):
    if func == 'sin':
        return math.sin(math.radians(x))
    elif func == 'cos':
        return math.cos(math.radians(x))
    elif func == 'tan':
        return math.tan(math.radians(x))
    else:
        return "Error! Unsupported trigonometric function."

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Trigonometric Function")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print("Select trigonometric function:")
            print("1. sin")
            print("2. cos")
            print("3. tan")
            trig_choice = input("Enter choice (1/2/3): ")

            angle = float(input("Enter angle in degrees: "))

            if trig_choice == '1':
                print(f"sin({angle}) = {trig_function('sin', angle)}")
            elif trig_choice == '2':
                print(f"cos({angle}) = {trig_function('cos', angle)}")
            elif trig_choice == '3':
                print(f"tan({angle}) = {trig_function('tan', angle)}")
            else:
                print("Invalid input")

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
