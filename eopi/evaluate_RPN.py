def evaluate(expression: str):
    exp = expression.split(",")
    
    stack = []
    operators = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : x / y
    }

    for e in exp:
        if e in operators:
            op2 = stack.pop()
            op1 = stack.pop()

            res = operators[e](op1, op2)
            stack.append(res)

        else:
            stack.append(int(e))

    return stack[-1]
    

if __name__ == "__main__":
    print(evaluate("3,4,+,2,*,1,+"))
