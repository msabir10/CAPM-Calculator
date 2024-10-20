import tkinter as tk
from tkinter import messagebox

# Function to calculate CAPM
def calculate_capm():
    try:
        rf = float(risk_free_rate_entry.get())
        beta = float(beta_entry.get())
        rm = float(market_return_entry.get())
        ra = rf + beta * (rm - rf)
        result_label.config(text=f"Expected Return (Ra): {ra:.2f}%")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Tooltips for input fields
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify="left",
                         background="#ffffff", relief="solid", borderwidth=1,
                         font=("Arial", 10))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# Function to show the About section with detailed info
def show_about():
    about_text = (
        "This Python app creates a simple GUI to calculate the expected return using the CAPM formula. "
        "The user inputs the risk-free rate, the asset’s beta, and the expected market return, and the program calculates the expected return.\n\n"
        "Explanation of the Program:\n"
        "• The program prompts the user to input the risk-free rate, asset beta, and market return.\n"
        "• Upon clicking 'Calculate CAPM,' the program computes the expected return using the CAPM formula and displays the result as a percentage.\n"
        "• The program can be expanded to include live market data from various APIs to automatically include the risk-free rate and calculate the beta of the specific stock investment and the expected market return (for stocks, the user will just need to enter the ticker symbol).\n\n"
        "Application of the CAPM Calculator:\n"
        "The CAPM calculator can be used by investors to evaluate the expected return on various assets based on their individual risk profiles. It helps in making more informed investment decisions by quantifying the trade-off between risk and return."
    )
    messagebox.showinfo("About CAPM Calculator", about_text)

# Function to show CAPM formula and description
def show_help():
    help_text = (
        "Capital Asset Pricing Model (CAPM) Formula:\n\n"
        "Ra = Rf + β(Rm - Rf)\n\n"
        "Where:\n"
        "- Ra: Expected return on the investment\n"
        "- Rf: Risk-free rate (usually government bonds)\n"
        "- β: Beta of the asset (volatility compared to the market)\n"
        "- Rm: Expected return of the market\n\n"
        "The CAPM formula calculates the expected return of an asset based on its risk relative to the overall market."
    )
    messagebox.showinfo("CAPM Formula & Description", help_text)

# Creating the main window
window = tk.Tk()
window.title("CAPM Calculator")
window.geometry("500x450")  # Increased window size

# Title label
title_label = tk.Label(window, text="CAPM Calculator", font=("Arial", 16, "bold"), fg="blue")
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(window, text="Enter the values below to calculate the expected return:")
instruction_label.pack(pady=10)

# Risk-free rate input
risk_free_rate_label = tk.Label(window, text="Risk-Free Rate (Rf) %:")
risk_free_rate_label.pack(pady=8)
risk_free_rate_entry = tk.Entry(window)
risk_free_rate_entry.pack(pady=8)

# Beta input
beta_label = tk.Label(window, text="Beta (β):")
beta_label.pack(pady=8)
beta_entry = tk.Entry(window)
beta_entry.pack(pady=8)

# Market return input
market_return_label = tk.Label(window, text="Market Return (Rm) %:")
market_return_label.pack(pady=8)
market_return_entry = tk.Entry(window)
market_return_entry.pack(pady=8)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Frame for buttons (Calculate and Clear) with wider buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Calculate button with increased width
calculate_button = tk.Button(button_frame, text="Calculate CAPM", command=calculate_capm, 
                             bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
calculate_button.pack(side=tk.LEFT, padx=10, pady=5)

# Clear button with increased width
clear_button = tk.Button(button_frame, text="Clear", command=lambda: risk_free_rate_entry.delete(0, tk.END) or beta_entry.delete(0, tk.END) or market_return_entry.delete(0, tk.END) or result_label.config(text=""), 
                         bg="#f44336", fg="white", font=("Arial", 12), width=20)
clear_button.pack(side=tk.LEFT, padx=10, pady=5)

# Creating a menu bar
menubar = tk.Menu(window)
window.config(menu=menubar)

# Adding the Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="CAPM Formula", command=show_help)
help_menu.add_command(label="About", command=show_about)

# Run the application
window.mainloop()
