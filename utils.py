"""
    Helper functions for my AdvCalc program.
    Mainly converting Infix expressions to Postfix format.
"""
from typing import List

def op_precedence(to_check: str) -> int:
    """
        Return the precedence of the operator [4, 1] or 0 if there is an error.
    """
    if to_check in ("(", ")"):
        return 4
    if to_check == "^":
        return 3
    if to_check in ("*", "/"):
        return 2
    if to_check in ("+", "-"):
        return 1
    return 0

def find_lp(postfix: List[str], op_stack: List[str]) -> None:
    """
        Pops and appends all elements from
        the stack to the postfix until
        the left parenthesis is found.
    """
    while len(op_stack) > 0:
        to_app = op_stack.pop()
        if to_app == "(":
            return postfix
        postfix.append(" " + to_app)

def is_op(to_check: str) -> bool:
    """
        Check whether the character passed in is an operator.
    """
    if len(to_check)>1:
        return False
    if to_check in ("+", "-", "*", "/", "^", "(", ")"):
        return True
    return False

def precedence_checks(to_check: str, postfix: List[str], op_stack: List[str]) -> None:
    """
        Performs the 3 kinds of precedence checks for a given character against the stack
    """
    check_score = op_precedence(to_check)
    stack_score = op_precedence(op_stack[len(op_stack) - 1])
    if check_score > stack_score:
        op_stack.append(to_check)
        return
    if check_score < stack_score:
        postfix.append(" " + op_stack.pop() + " ")
        if(len(op_stack) != 0):
            precedence_checks(to_check, postfix, op_stack)
        return
    if check_score == stack_score:
        postfix.append(" " + op_stack.pop() + " ")
        op_stack.append(to_check)

def infix_to_postfix(infix: str) -> str:
    """
        Converts an infix algebraic expression to postfix.
        Constructed with the algorithm from:
        https://www.javatpoint.com/convert-infix-to-postfix-notation
    """
    postfix = []
    op_stack = []
    for char in infix:
        if char == " ":
            continue
        if not is_op(char):
            postfix.append(char)
        else:
            postfix.append(" ")
            if len(op_stack)==0 or op_stack[len(op_stack) - 1] == '(' or char=="(":
                op_stack.append(char)
                continue
            if char==")":
                find_lp(postfix, op_stack)
                continue
            precedence_checks(char, postfix, op_stack)
    for operator in op_stack:
        postfix.append(" " + operator)
    # Eliminate double/triple spacing before returning
    to_return = "".join(postfix)
    return " ".join(to_return.split())

def perf_op(first: str, second: str, operator: str) -> float:
    """
        Perform a algebraic operation and return the result.
    """
    if operator=="+":
        return float(first) + float(second)
    if operator=="-":
        return float(first) - float(second)
    if operator=="*":
        return float(first) * float(second)
    if operator=="/":
        return float(first) / float(second)
    if operator=="^":
        return pow(float(first), float(second))
    raise ValueError("Invalid operator:", operator)

def eval_postfix(postfix: str) -> float:
    """
        Evaluate a postfix expression and return the result.
        Constructed with the algorithm from:
        https://www.javatpoint.com/convert-infix-to-postfix-notation
    """
    stack = []
    for _op in postfix.split():
        if not is_op(_op):
            stack.append(_op)
        else:
            second = stack.pop()
            first = stack.pop()
            stack.append(perf_op(first, second, _op))
    return float(stack[0])
