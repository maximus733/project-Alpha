import tkinter as tk
from math import *

class SuperCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Calculator")
        self.root.geometry("400x600")
        
    
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('sqrt', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('!', 7, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)
        
        self.expression = ""
    
    def on_button_click(self, char):
        if char == '=':
            try:
                
                expr = self.expression.replace('^', '**')
                
                if '!' in expr:
                    expr = self.handle_factorial(expr)
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        elif char == 'C':
            self.display.delete(0, tk.END)
            self.expression = ""
        elif char in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            self.expression += f"{char}("
            self.display.insert(tk.END, f"{char}(")
        elif char == 'pi':
            self.expression += str(pi)
            self.display.insert(tk.END, str(pi))
        elif char == 'e':
            self.expression += str(e)
            self.display.insert(tk.END, str(e))
        elif char == '!':
            self.expression += '!'
            self.display.insert(tk.END, '!')
        else:
            self.expression += char
            self.display.insert(tk.END, char)
    
    def handle_factorial(self, expr):
        # Simple factorial replacement (assumes single ! at end)
        if expr.endswith('!'):
            num = expr[:-1]
            try:
                return str(factorial(int(num)))
            except:
                return "Error"
        return expr

if __name__ == "__main__":
    root = tk.Tk()
    calc = SuperCalculator(root)
    root.mainloop()