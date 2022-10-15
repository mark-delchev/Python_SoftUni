def calculation(operation, num1, num2):
    if operation == "multiply":
        return (num1 * num2)
    elif operation == "divide":
        return int(num1 / num2)
    elif operation == "add":
        return (num1 + num2)
    elif operation == "subtract":
        return (num1 - num2)

op = input()
n1 = int(input())
n2 = int(input())

print(calculation(op, n1, n2))