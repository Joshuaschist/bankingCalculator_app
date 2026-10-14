from .exceptions import InvalidOperationError

class Calculator:

    def __init__(self):
        self.ops = {
            "add": lambda a,b: a+b,
            "sub": lambda a,b: a-b,
            "mul": lambda a,b: a*b,
            "div": lambda a,b: a/b if b!=0 else "Error"
        }

    def calculate(self, op, a, b):
        if op not in self.ops:
            raise InvalidOperationError("Invalid operation")
        return self.ops[op](a,b)