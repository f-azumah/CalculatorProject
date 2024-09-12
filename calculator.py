from collections import deque
import math

#operator precedence
PRECEDENCE = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
    '^': 3,
    'sqrt': 4, 'log': 4,
    'sin': 4, 'cos': 4, 'tan': 4
}

#associativity of operators
ASSOCIATIVITY = {
    '+': 'LEFT', '-': 'LEFT',
    '*': 'LEFT', '/': 'LEFT',
    '^': 'RIGHT',
    'sqrt': 'RIGHT', 'log': 'RIGHT',
    'sin': 'RIGHT', 'cos': 'RIGHT', 'tan': 'RIGHT'
}

def shunting_yard(expression):
    output = deque()
    operators = deque()
    tokens = deque(expression.split())

    while tokens:
        token = tokens.popleft()

        if token.isdigit():
            output.append(token)
        elif token in PRECEDENCE:
            while (
                operators and
                operators[-1] in PRECEDENCE and
                (PRECEDENCE[operators[-1]] > PRECEDENCE[token] or
                 (PRECEDENCE[operators[-1]] == PRECEDENCE[token] and
                  ASSOCIATIVITY[token] == 'LEFT'))
            ):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators:
                operators.pop()  # Discard '('
            else:
                raise ValueError("Mismatched parentheses")
        else:
            raise ValueError(f"Invalid token: {token}")

    while operators:
        if operators[-1] == '(' or operators[-1] == ')':
            raise ValueError("Mismatched parentheses")
        output.append(operators.pop())

    return output

def evaluate_postfix(expression):
    stack = deque()

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                result = a + b
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                result = a - b
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                result = a * b
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            elif token == '^':
                b = stack.pop()
                a = stack.pop()
                result = a ** b
            elif token == 'sqrt':
                a = stack.pop()
                result = math.sqrt(a)
            elif token == 'log':
                a = stack.pop()
                result = math.log10(a)
            elif token == 'sin':
                a = stack.pop()
                result = math.sin(a)
            elif token == 'cos':
                a = stack.pop()
                result = math.cos(a)
            elif token == 'tan':
                a = stack.pop()
                result = math.tan(a)
            else:
                raise ValueError(f"Invalid operator: {token}")
            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack.pop()

def prompt_menu():
    print("""
Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Square root
7. Logarithm (base 10)
8. Trigonometric functions (sin, cos, tan)
""")
    choice = int(input("Choice Number: "))
    if choice == 1:
        a = input("Enter expression for addition: ")
        postfix = shunting_yard(a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 2:
        a = input("Enter expression for subtraction: ")
        postfix = shunting_yard(a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 3:
        a = input("Enter expression for multiplication: ")
        postfix = shunting_yard(a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 4:
        a = input("Enter expression for exponentiation: ")
        postfix = shunting_yard(a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 5:
        a = input("Enter expression for division: ")
        postfix = shunting_yard(a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 6:
        a = input("Enter expression for square root: ")
        postfix = shunting_yard('sqrt ' + a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 7:
        a = input("Enter expression for logarithm (base 10): ")
        postfix = shunting_yard('log ' + a)
        result = evaluate_postfix(postfix)
        print(f"Result: {result}")
    elif choice == 8:
        print("Enter expression for:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        trig_choice = int(input("Choice Number: "))
        if trig_choice == 1:
            a = input("Enter expression for sine: ")
            postfix = shunting_yard('sin ' + a)
            result = evaluate_postfix(postfix)
            print(f"Result: {result}")
        elif trig_choice == 2:
            a = input("Enter expression for cosine: ")
            postfix = shunting_yard('cos ' + a)
            result = evaluate_postfix(postfix)
            print(f"Result: {result}")
        elif trig_choice == 3:
            a = input("Enter expression for tangent: ")
            postfix = shunting_yard('tan ' + a)
            result = evaluate_postfix(postfix)
            print(f"Result: {result}")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

    loop()

def loop():
    choice = input("Do you have another operation? (Y/N): ")
    if choice.upper() == "Y":
        prompt_menu()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input")
        loop()

prompt_menu()
