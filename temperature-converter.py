import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (value * 9/5) + 32
            k = value + 273.15
            label_result.config(text=f"{value} °C = {f:.2f} °F\n{value} °C = {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (value - 32) * 5/9
            k = c + 273.15
            label_result.config(text=f"{value} °F = {c:.2f} °C\n{value} °F = {k:.2f} K")
        elif unit == "Kelvin":
            c = value - 273.15
            f = (c * 9/5) + 32
            label_result.config(text=f"{value} K = {c:.2f} °C\n{value} K = {f:.2f} °F")
        else:
            label_result.config(text="Please select a unit.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for temperature.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# Widgets
label_title = ttk.Label(root, text="Temperature Converter", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

entry_temp = ttk.Entry(root, width=20)
entry_temp.pack(pady=5)
entry_temp.insert(0, "Enter value")

combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=18)
combo_unit.pack(pady=5)
combo_unit.set("Select unit")

button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

label_result = ttk.Label(root, text="", font=("Arial", 12), anchor="center", justify="center")
label_result.pack(pady=10)

root.mainloop()

