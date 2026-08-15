try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input, Please enter an integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("An unexpected error occurred")
else:
    print("Division successful, no exceptions occurred")
