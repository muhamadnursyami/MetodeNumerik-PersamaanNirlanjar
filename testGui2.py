# NAMA : MUHAMAD NUR SYAMI
# NIM : 2101020005
# MK : METODE NUMERIK
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def persamaan(t):
    return 2 * t**3 + 5 * t**2 - 10 * t - 4

def turunan_persamaan(t):
    return 6 * t**2 + 10 * t - 10

def metode_bagi_dua(func, a, b, tol=0.001, max_iter=100):
    """
    Metode Bagi Dua digunakan untuk mencari akar persamaan dalam interval [a, b].

    Parameters:
    - func (fungsi): Fungsi persamaan yang ingin diselesaikan.
    - a (float): Batas bawah interval.
    - b (float): Batas atas interval.
    - tol (float): Toleransi galat yang diinginkan.
    - max_iter (int): Jumlah maksimum iterasi.

    Returns:
    - float: Estimasi akar persamaan.
    """
    if func(a) * func(b) > 0:
        raise ValueError("Tidak dapat menentukan akar karena f(a) dan f(b) memiliki tanda yang sama.")
    
    print(f"{'Iterasi':<10}{'a':<20}{'b':<20}{'c':<20}{'f(a)':<20}{'f(b)':<20}{'f(c)':<20}{'|b - a|':<20}{'Kondisi Berhenti'}")

    for i in range(max_iter):
        c = (a + b) / 2
        f_a = func(a)
        f_b = func(b)
        f_c = func(c)
        abs_b_minus_a = abs(b - a)

        print(f"{i + 1:<10}{a:<20}{b:<20}{c:<20}{f_a:<20}{f_b:<20}{f_c:<20}{abs_b_minus_a:<20}", end="")
        
        if abs_b_minus_a < tol or f_c == 0:
            print("TRUE")
            return c

        print("FALSE")

        if f_c * f_a < 0:
            b = c
        else:
            a = c
        
    raise ValueError("Metode Bagi Dua tidak konvergen dalam jumlah iterasi yang ditentukan.")

def metode_regula_falsi(func, a, b, tol=0.001, max_iter=100):
    """
    Metode Regula Falsi digunakan untuk mencari akar persamaan dalam interval [a, b].

    Parameters:
    - func (fungsi): Fungsi persamaan yang ingin diselesaikan.
    - a (float): Batas bawah interval.
    - b (float): Batas atas interval.
    - tol (float): Toleransi galat yang diinginkan.
    - max_iter (int): Jumlah maksimum iterasi.

    Returns:
    - float: Estimasi akar persamaan.
    """
    if func(a) * func(b) > 0:
        raise ValueError("Nilai fungsi pada ujung interval harus memiliki tanda yang berlawanan.")
    
    print(f"{'Iterasi':<10}{'a':<20}{'b':<20}{'c':<20}{'f(a)':<20}{'f(b)':<20}{'f(c)':<20}{'|b - a|':<20}")

    for i in range(max_iter):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        f_a = func(a)
        f_b = func(b)
        f_c = func(c)
        abs_b_minus_a = abs(b - a)

        print(f"{i + 1:<10}{a:<20}{b:<20}{c:<20}{f_a:<20}{f_b:<20}{f_c:<20}{abs_b_minus_a:<20}")
        
        if abs(f_c) < tol:
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("Metode Regula Falsi tidak konvergen dalam jumlah iterasi yang ditentukan.")

def metode_newton_raphson(func, turunan_func, x0, tol=0.001, max_iter=100):
    """
    Metode Newton-Raphson digunakan untuk mencari akar persamaan.

    Parameters:
    - func (fungsi): Fungsi persamaan yang ingin diselesaikan.
    - turunan_func (fungsi): Turunan dari fungsi persamaan.
    - x0 (float): Nilai awal untuk iterasi.
    - tol (float): Toleransi galat yang diinginkan.
    - max_iter (int): Jumlah maksimum iterasi.

    Returns:
    - float: Estimasi akar persamaan.
    """
    x = x0
    print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<}".format("Iterasi", "xr", "f(xr)", "f'(xr)", "|xr+1 - xr|", "Kondisi Berhenti"))

    for i in range(max_iter):
        x_old = x
        f_x = func(x)
        f_prime_x = turunan_func(x)
        x = x - f_x / f_prime_x
        delta_x = abs(x - x_old)

        print("{:<10}{:<20}{:<20}{:<20}{:<20}".format(i + 1, x, f_x, f_prime_x, delta_x), end="")
        
        # Stopping criterion: Check if the change in x is smaller than tol
        if delta_x < tol:
            print("TRUE")
            return x
    
        print("FALSE")

    raise ValueError("Metode Newton-Raphson tidak konvergen dalam jumlah iterasi yang ditentukan.")

def metode_secant(func, x0, x1, tol=0.001, max_iter=100):
    """
    Metode Secant digunakan untuk mencari akar persamaan.

    Parameters:
    - func (fungsi): Fungsi persamaan yang ingin diselesaikan.
    - x0 (float): Nilai awal pertama.
    - x1 (float): Nilai awal kedua.
    - tol (float): Toleransi galat yang diinginkan.
    - max_iter (int): Jumlah maksimum iterasi.

    Returns:
    - float: Estimasi akar persamaan.
    """
    iterasi = 0
    x_old = x0

    print(f"{'Iterasi':<10}{'Xr':<20}{'f(Xr)':<20}{'|Xr+1 - Xr|':<20}{'Kondisi Berhenti'}")
    
    for i in range(max_iter):
        f_x0 = func(x0)
        f_x1 = func(x1)

        # Secant formula to update the root estimate
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        
        # Error calculation
        error = abs(x2 - x1)

        # Print iteration details
        print(f"{iterasi + 1:<10}{x2:<20}{func(x2):<20}{error:<20}", end="")

        # Stopping criterion: Check if the change in x is smaller than tol
        if error < tol:
            print("TRUE")
            return x2

        print("FALSE")

        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x2
        iterasi += 1
    
    raise ValueError("Metode Secant tidak konvergen dalam jumlah iterasi yang ditentukan.")

def solve_equation(method, input_values):
    try:
        if method == "Metode Bagi Dua":
            result = metode_bagi_dua(persamaan, *input_values)
        elif method == "Metode Regula Falsi":
            result = metode_regula_falsi(persamaan, *input_values)
        elif method == "Metode Newton-Raphson":
            result = metode_newton_raphson(persamaan, turunan_persamaan, *input_values)
        elif method == "Metode Secant":
            result = metode_secant(persamaan, *input_values)
        else:
            raise ValueError("Metode tidak valid.")
        
        messagebox.showinfo("Hasil", f"Hasil {method}: {result}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def create_input_fields(root, method, labels, input_values):
    for label_text in labels:
        Label(root, text=label_text, font=("Arial", 12, "bold")).pack(pady=5)
        entry = Entry(root, font=("Arial", 12))
        entry.pack(pady=5)
        input_values.append(entry)

    solve_method = lambda: solve_equation(method, [float(entry.get()) for entry in input_values])
    Button(root, text=f"Hitung {method}", command=solve_method, font=("Arial", 14, "bold"), bg="#2D9596", fg="white").pack(pady=10)

def create_gui():
    root = tk.Tk()
    root.title("Equation Solver")
    root.geometry("400x300")
    root.configure(bg="#9AD0C2")

    # Method selection
    Label(root, text="Pilih Metode", font=("Arial", 16,), bg="#ecf0f1").pack(pady=10)
    methods = ["Metode Bagi Dua", "Metode Regula Falsi", "Metode Newton-Raphson", "Metode Secant"]
    selected_method = tk.StringVar(root)
    selected_method.set(methods[0])

    method_dropdown = tk.OptionMenu(root, selected_method, *methods)
    method_dropdown.config(font=("Arial", 12), bg="#2ecc71", fg="white")
    method_dropdown.pack(pady=10)

    # Input fields for each method
    method_inputs = {
        "Metode Bagi Dua": ["Nilai Awal (a)", "Nilai Akhir (b)"],
        "Metode Regula Falsi": ["Nilai Awal (a)", "Nilai Akhir (b)"],
        "Metode Newton-Raphson": ["Nilai Awal (x0)"],
        "Metode Secant": ["Nilai Awal Pertama (x0)", "Nilai Awal Kedua (x1)"]
    }

    # Create input fields dynamically based on the selected method
    input_values = []
    create_input_fields(root, methods[0], method_inputs[methods[0]], input_values)

    def on_method_change(*args):
        # Clear previous input fields
        for widget in root.winfo_children():
            if isinstance(widget, Entry):
                widget.destroy()

        input_values.clear()

        # Create input fields for the selected method
        create_input_fields(root, selected_method.get(), method_inputs[selected_method.get()], input_values)

    # Bind method change event
    selected_method.trace_add("write", on_method_change)

    root.mainloop()

if __name__ == "__main__":
    create_gui()