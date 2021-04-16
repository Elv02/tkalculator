"""
    Helper functions for my AdvCalc program.
    Mainly converting Infix expressions to Postfix format utilizing a custom Stack class.
"""
import math
import re
class Stack:
    """
        A custom implementation of a stack.
    """
    def __init__(self):
        """
            Create a new stack instance.
        """
        self.top = -1
        self.cust_stack = []

    def __str__(self) -> str:
        """
            String representation of the stack
        """
        res = "Stack[" + str(self.top) + "]:\n"
        for entry in self.cust_stack:
            res += str(entry) + "\n"
        return res

    def is_empty(self) -> bool:
        """
            Check if the stack is empty
        """
        return self.top == -1

    def push(self, val: str) -> None:
        """
            Push a new value onto the stack.
        """
        self.top += 1
        self.cust_stack.append(val)

    def pop(self) -> str:
        """
            Pop the top value off of the stack
        """
        self.top -= 1
        return self.cust_stack.pop()

    def peek(self) -> str:
        """
            Returns value at the top of the stack without altering it.
        """
        return self.cust_stack[self.top]

def op_precedence(to_check: str) -> int:
    """
        Return the precedence of the operator [4, 1] or 0 if there is an error.
    """
    if to_check in ("^", "√"):
        return 4
    if to_check in ("×", "*", "÷", "/", "%"):
        return 3
    if to_check in ("+", "-"):
        return 2
    if to_check in ("(", ")"):
        return 1
    return 0

def is_operator(to_check: str) -> bool:
    """
        Check whether the character passed in is an operator.
    """
    if len(to_check)>1:
        return False
    if to_check in ("+", "-", "×", "*", "÷", "/", "^", "(", ")", "√", "%"):
        return True
    return False

def is_operand(to_check: str) -> bool:
    """
        Validate if a given string matches the format for an operator.
    """
    reg_match = re.search(r"^[+-]?\d+(\.\d+)?$", to_check)
    if reg_match:
        return True
    return False

def infix_format(infix: str) -> str:
    """
        Checks through an given infix string to ensure it is in a clean format.
        Does so by putting spaces between all operators and operands.
    """
    to_return = ""

    for char in infix:
        if is_operator(char):
            to_return += " " + char + " "
        else:
            to_return += char
    return to_return

def infix_to_postfix(infix: str) -> str:
    """
        Converts an infix algebraic expression to postfix.
        Constructed with the algorithm from:
        https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
    """
    spaced_infix = infix_format(infix)
    output = []
    op_stack = Stack()
    for op_token in spaced_infix.split():
        if is_operand(op_token):
            output.append(op_token)
            continue
        if op_token == "(":
            op_stack.push(op_token)
            continue
        if op_token == ")":
            op_token = op_stack.pop()
            while op_token != '(':
                output.append(op_token)
                op_token = op_stack.pop()
            continue

        while( (not op_stack.is_empty()) and \
            (op_precedence(op_token) <= op_precedence(op_stack.peek())) ):
            output.append(op_stack.pop())
        op_stack.push(op_token)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return " ".join(output)

def perf_op(first: str, second: str, operator: str) -> float:
    """
        Perform a algebraic operation and return the result.
    """
    if operator=="+":
        return float(first) + float(second)
    if operator=="-":
        return float(first) - float(second)
    if operator=="*" or operator=="×":
        return float(first) * float(second)
    if operator=="/" or operator=="÷":
        return float(first) / float(second)
    if operator=="^":
        return math.pow(float(first), float(second))
    raise ValueError("Invalid operator:", operator)

def perf_func(num: str, operator: str) -> float:
    """
        Evaluate a function call (Square root or percentile).
        Returns the result as a floating point value.
    """
    if operator == "√":
        return math.sqrt(float(num))
    elif operator == "%":
        return float(num)/100.0
    else:
        raise ValueError("Unrecognized function: ", operator)

def eval_postfix(postfix: str) -> float:
    """
        Evaluate a postfix expression and return the result.
        Constructed with the algorithm from:
        https://www.javatpoint.com/convert-infix-to-postfix-notation
    """
    stack = []
    for _op in postfix.split():
        if not is_operator(_op):
            stack.append(_op)
        else:
            # TODO: Check for function calls! (Square and Percentage)
            if _op in ("√","%"):
                num = stack.pop()
                stack.append(perf_func(num, _op))
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(perf_op(first, second, _op))
    return float(stack[0])

def is_valid_postfix_exp(postfix: str) -> bool:
    """
        Checks whether a given postfix expression is valid through
        constructing a Binary Expression Tree and checking that.
    """
    pass