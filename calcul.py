while True:
    num1 = float(input("First number: "))
    op = input("Operation (+, -, *, /, **): ")
    num2 = float(input("Second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        print("Result:", "Cannot divide by 0" if num2 == 0 else num1 / num2)
    elif op == '**':
        print("Result:", num1 ** num2)
    else:
        print("Invalid operation")

    if input("Continue? (yes/no): ").lower() != 'yes':
        break
