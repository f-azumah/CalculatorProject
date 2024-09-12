import re
import math


def tokenise(expr):
    tokens = re.findall(r'\d+|\S', expr)
    return tokens

def parse(tokens):
    #dictionary storing the operators as keys 
    operators = {'+' : 1, '-' : 2, '*' : 3, '^' : 4, '/':5, "/'" : 6, "sqrt" : 7, "log" : 8}
    output = []
    operator_stack = []

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            output_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and operators.get(operator_stack[-1]) >= operators.get(token):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output.append(operator_stack.pop())
    return output 

def evaluate(expr):
    tokens = tokenize(expression)
    postfix_expression = parse(tokens)
    res = []

    for token in postfix_expression:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                res.append(a + b)
            elif token == '-':
                res.append(a - b)
            elif token == '*':
                res.append(a * b)
            elif token == '^':
                res.append( a ** b)
            elif token == '/':
                res.append(a / b)
            elif token == "/'":
                res.append((a//b),(a%b))
            elif token = 'sqrt':
                if a >= 0:
                    res.append(a ** 0.5)
            elif token == 'log':
                if a > 0 and b > 0:
                    res.append(math.log(a,b))

    return res[0]


