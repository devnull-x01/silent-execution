# app/gui.py
import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    """
    A modern, dark-themed calculator GUI built with Tkinter.
    
    This class encapsulates all the components and logic for the calculator,
    serving as the legitimate frontend application for the malware simulation project.
    """
    def __init__(self, root):
        """
        Initializes the Calculator application.

        Args:
            root: The main Tkinter window (tk.Tk).
        """
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Configure the dark theme style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        # Expression that will be displayed on the screen
        self.expression = ""
        
        # StringVar to link the display with the expression
        self.display_var = tk.StringVar()
        
        self.create_widgets()

    def configure_styles(self):
        """Configures the custom dark theme styles for the calculator widgets."""
        # Backgrounds
        self.root.configure(bg='#2E2E2E')
        
        # Display Style
        self.style.configure('TFrame', background='#2E2E2E')
        self.style.configure('TLabel', background='#2E2E2E', foreground='white', font=('Arial', 30))
        
        # Button Styles
        self.style.configure('TButton', font=('Arial', 18), borderwidth=0, focuscolor='#2E2E2E')
        self.style.map('TButton',
                       background=[('active', '#6E6E6E')],
                       foreground=[('active', 'white')])

        # Specific styles for different button types
        self.style.configure('Num.TButton', background='#4F4F4F', foreground='white')
        self.style.configure('Op.TButton', background='#FF9500', foreground='white')
        self.style.configure('Clear.TButton', background='#D4D4D2', foreground='black')

    def create_widgets(self):
        """Creates and arranges all the widgets in the calculator window."""
        # Main frame
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Display Screen
        display_label = ttk.Label(main_frame, textvariable=self.display_var, anchor='e', style='TLabel')
        display_label.pack(expand=True, fill='both', ipady=20)

        # Button Grid
        button_grid = ttk.Frame(main_frame, style='TFrame')
        button_grid.pack(expand=True, fill='both')

        # Define button layout and properties
        buttons = [
            ('7', 1, 0, 'Num.TButton'), ('8', 1, 1, 'Num.TButton'), ('9', 1, 2, 'Num.TButton'), ('/', 1, 3, 'Op.TButton'),
            ('4', 2, 0, 'Num.TButton'), ('5', 2, 1, 'Num.TButton'), ('6', 2, 2, 'Num.TButton'), ('*', 2, 3, 'Op.TButton'),
            ('1', 3, 0, 'Num.TButton'), ('2', 3, 1, 'Num.TButton'), ('3', 3, 2, 'Num.TButton'), ('-', 3, 3, 'Op.TButton'),
            ('0', 4, 0, 'Num.TButton'), ('.', 4, 1, 'Num.TButton'), ('=', 4, 2, 'Op.TButton'), ('+', 4, 3, 'Op.TButton'),
            ('Clear', 5, 0, 'Clear.TButton', 4) # Clear button spans 4 columns
        ]

        # Create and place buttons in the grid
        for (text, row, col, style, *span) in buttons:
            button = ttk.Button(button_grid, text=text, style=style,
                                command=lambda t=text: self.on_button_press(t))
            colspan = span[0] if span else 1
            button.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=5, pady=5)

        # Configure grid rows and columns to expand equally
        for i in range(6):
            button_grid.rowconfigure(i, weight=1)
        for i in range(4):
            button_grid.columnconfigure(i, weight=1)

    def on_button_press(self, char):
        """
        Handles all button press events.

        Args:
            char (str): The character of the button that was pressed.
        """
        if char == 'Clear':
            self.clear()
        elif char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

    def calculate(self):
        """
        Evaluates the current expression and updates the display.
        Uses a try-except block to handle potential syntax or math errors.
        """
        try:
            # Security Note: eval() can be dangerous if used with untrusted input.
            # In this controlled environment, it's acceptable as the input is
            # limited to calculator buttons.
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except (SyntaxError, ZeroDivisionError):
            self.display_var.set("Error")
            self.expression = ""

    def clear(self):
        """Clears the current expression and resets the display."""
        self.expression = ""
        self.display_var.set("")

def run_gui():
    """
    Initializes and runs the Tkinter Calculator application.
    This function is the main entry point for the GUI.
    """
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == '__main__':
    run_gui()