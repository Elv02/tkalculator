"""
    GUI Advanced Calculator in Python using Tkinter!
    By Warren Hoeft.
"""
import utils

def main():
    """
        Entry point of program.  Setup GUI.
    """
    res = utils.infix_to_postfix("(3*(6+2)/6)^(4/2)")
    print(res)
    res = utils.eval_postfix(res)
    print(res)
    res = utils.infix_to_postfix("12*12+2*3/(4*5)^(6-3)")
    print(res)
    res = utils.eval_postfix(res)
    print(res)

# Call main function
if __name__ == "__main__":
    main()
