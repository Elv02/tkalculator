"""
    GUI Advanced Calculator in Python using Tkinter!
    By Warren Hoeft.
"""
from tkinter.constants import DISABLED, E, END, N, NORMAL, S, W, WORD
import tkinter as tk
from tkinter import scrolledtext
from functools import partial
import utils
import btree


class Calculator:
    """
        Tkinter Calculator.
        Contains all logic for the frontend of the calculator.
    """
    def __init__(self) -> None:
        """
            Create a new instance of the Calculator.
            Initializes GUI then starts main loop.
        """
        self.root = tk.Tk()
        self.root.title("Tkalculator")

        self.output = scrolledtext.ScrolledText(self.root, height = 4, wrap=WORD)
        self.output.grid(row=0, column=0, sticky=N+S+E+W, columnspan=6)

        self.input = tk.Text(self.root, height=2)
        self.input.grid(row=1, column=0, sticky=N+S+E+W, columnspan=6)

        button_0 = tk.Button(self.root, text="0", command=partial(self.entered, "0"))
        button_0.grid(row=5, column=0, sticky=N+S+E+W)

        button_dot = tk.Button(self.root, text=".", command=partial(self.entered, "."))
        button_dot.grid(row=5, column=1, sticky=N+S+E+W)

        button_per = tk.Button(self.root, text="%", command=partial(self.entered, "%"))
        button_per.grid(row=5, column=2, sticky=N+S+E+W)

        button_1 = tk.Button(self.root, text="1", command=partial(self.entered, "1"))
        button_1.grid(row=4, column=0, sticky=N+S+E+W)

        button_2 = tk.Button(self.root, text="2", command=partial(self.entered, "2"))
        button_2.grid(row=4, column=1, sticky=N+S+E+W)

        button_3 = tk.Button(self.root, text="3", command=partial(self.entered, "3"))
        button_3.grid(row=4, column=2, sticky=N+S+E+W)

        button_4 = tk.Button(self.root, text="4", command=partial(self.entered, "4"))
        button_4.grid(row=3, column=0, sticky=N+S+E+W)

        button_5 = tk.Button(self.root, text="5", command=partial(self.entered, "5"))
        button_5.grid(row=3, column=1, sticky=N+S+E+W)

        button_6 = tk.Button(self.root, text="6", command=partial(self.entered, "6"))
        button_6.grid(row=3, column=2, sticky=N+S+E+W)

        button_7 = tk.Button(self.root, text="7", command=partial(self.entered, "7"))
        button_7.grid(row=2, column=0, sticky=N+S+E+W)

        button_8 = tk.Button(self.root, text="8", command=partial(self.entered, "8"))
        button_8.grid(row=2, column=1, sticky=N+S+E+W)

        button_9 = tk.Button(self.root, text="9", command=partial(self.entered, "9"))
        button_9.grid(row=2, column=2, sticky=N+S+E+W)

        button_div = tk.Button(self.root, text="÷", command=partial(self.entered, "÷"))
        button_div.grid(row=2, column=3, sticky=N+S+E+W)

        button_del = tk.Button(self.root, text="←", command=self.del_input)
        button_del.grid(row=2, column=4, sticky=N+S+E+W)

        button_clr = tk.Button(self.root, text="C", command=self.clr_input)
        button_clr.grid(row=2, column=5, sticky=N+S+E+W)

        button_mul = tk.Button(self.root, text="×", command=partial(self.entered, "×"))
        button_mul.grid(row=3, column=3, sticky=N+S+E+W)

        button_lbr = tk.Button(self.root, text="(", command=partial(self.entered, "("))
        button_lbr.grid(row=3, column=4, sticky=N+S+E+W)

        button_rbr = tk.Button(self.root, text=")", command=partial(self.entered, ")"))
        button_rbr.grid(row=3, column=5, sticky=N+S+E+W)

        button_min = tk.Button(self.root, text="-", command=partial(self.entered, "-"))
        button_min.grid(row=4, column=3, sticky=N+S+E+W)

        button_exp = tk.Button(self.root, text="xʸ", command=partial(self.entered, "^"))
        button_exp.grid(row=4, column=4, sticky=N+S+E+W)

        button_sqr = tk.Button(self.root, text="√", command=partial(self.entered, "√"))
        button_sqr.grid(row=4, column=5, sticky=N+S+E+W)

        button_plu = tk.Button(self.root, text="+", command=partial(self.entered, "+"))
        button_plu.grid(row=5, column=3, sticky=N+S+E+W)

        button_equ = tk.Button(self.root, text="=", command=self.calc_exp)
        button_equ.grid(row=5, column=4, sticky=N+S+E+W, columnspan=2)

        for x in range(6):
            self.root.columnconfigure(x, weight=1)
            self.root.rowconfigure(x, weight=1)

        self.root.mainloop()

    def entered(self, num: str) -> None:
        """
            Called when any key on the pad is pressed, adds it to the input field.
        """
        self.input.insert(END, num)
    
    def del_input(self) -> None:
        """
            Clear the last entered character from the input field.
        """
        if(self.input.get(1.0, END) == ""):
            return
        else:
            self.input.delete(len(self.input.get(1.0, END)) - 1.0, END)
    
    def clr_input(self) -> None:
        """
            Clear the entire input field.
        """
        self.input.delete(1.0, END)
    
    def calc_exp(self) -> None:
        """
            Calculates the value of the expression in the input field.
            Clears input after completion and appends result to the output field.
        """
        if(self.input.get(1.0, END) == ""):
            return
        else:
            infix = self.input.get(1.0, END)
            print("INFIX: " + infix)
            postfix = utils.infix_to_postfix(infix)
            print("POSTFIX: " + postfix)
            #bin_tree = btree.construct_tree(postfix)
            #if not btree.is_tree_valid(bin_tree):
            #    self.output.configure(state=NORMAL)
            #    self.output.insert(END, "ERROR: Invalid expression format provided.\n")
            #    self.output.configure(state=DISABLED)
            #    return
            res = utils.eval_postfix(postfix)
            print("RESULT: " + str(res))
            self.output.configure(state=NORMAL)
            self.output.insert(END, infix + " = " + str(res) + "\n")
            self.output.configure(state=DISABLED)
            self.clr_input()


def main():
    """
        Entry point of program.  Create the calculator.
    """
    Calculator()

# Call main function
if __name__ == "__main__":
    main()
