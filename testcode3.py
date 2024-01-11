from sympy import symbols, diff, lambdify
import numpy as np

def persamaan(t):
    """
    Fungsi ini mendefinisikan persamaan yang ingin diselesaikan.
    """
    return 2 * t**3 + 5 * t**2 - 10 * t - 4

def turunan_pertama_persamaan(t):
    """
    Menghitung turunan pertama dari fungsi persamaan.
    """
    t_symb = symbols('t')
    persamaan_expr = 2 * t_symb**3 + 5 * t_symb**2 - 10 * t_symb - 4
    turunan_pertama = diff(persamaan_expr, t_symb)
    turunan_pertama_func = lambdify(t_symb, turunan_pertama, 'numpy')
    return turunan_pertama_func(t)

def turunan_kedua_persamaan(t):
    """
    Menghitung turunan kedua dari fungsi persamaan.
    """
    t_symb = symbols('t')
    persamaan_expr = 2 * t_symb**3 + 5 * t_symb**2 - 10 * t_symb - 4
    turunan_kedua = diff(persamaan_expr, t_symb, 2)
    turunan_kedua_func = lambdify(t_symb, turunan_kedua, 'numpy')
    return turunan_kedua_func(t)

def turunan_ketiga_persamaan(t):
    """
    Menghitung turunan ketiga dari fungsi persamaan.
    """
    t_symb = symbols('t')
    persamaan_expr = 2 * t_symb**3 + 5 * t_symb**2 - 10 * t_symb - 4
    turunan_ketiga = diff(persamaan_expr, t_symb, 3)
    turunan_ketiga_func = lambdify(t_symb, turunan_ketiga, 'numpy')
    return turunan_ketiga_func(t)

def fungsi_iterasi_titik_tetap(x):
    """
    Fungsi iterasi titik tetap yang akan digunakan dalam metode iterasi titik tetap.
    """
    # Menggunakan turunan pertama, kedua, dan ketiga sebagai komponen iterasi
    return x - turunan_pertama_persamaan(x) / turunan_kedua_persamaan(x) + turunan_ketiga_persamaan(x)

def metode_iterasi_titik_tetap(func, x0, tol=0.001, max_iter=100):
    """
    Metode Iterasi Titik Tetap digunakan untuk mencari akar persamaan.

    Parameters:
    - func (fungsi): Fungsi iterasi titik tetap.
    - x0 (float): Nilai awal untuk iterasi.
    - tol (float): Toleransi galat yang diinginkan.
    - max_iter (int): Jumlah maksimum iterasi.

    Returns:
    - float: Estimasi akar persamaan.
    """
    for i in range(max_iter):
        x = func(x0)

        # Stopping criterion: Check if the change in x is smaller than tol
        if abs(x - x0) < tol:
            return x

        x0 = x
    
    raise ValueError("Metode Iterasi Titik Tetap tidak konvergen dalam jumlah iterasi yang ditentukan.")

# Input nilai awal untuk Metode Iterasi Titik Tetap
x0_iterasi_titik_tetap = float(input("Masukkan nilai awal (x0) untuk Metode Iterasi Titik Tetap: "))

# Solve menggunakan Metode Iterasi Titik Tetap
try:
    hasil_iterasi_titik_tetap = metode_iterasi_titik_tetap(fungsi_iterasi_titik_tetap, x0_iterasi_titik_tetap)
    print(f"Hasil Metode Iterasi Titik Tetap: {hasil_iterasi_titik_tetap}")
except ValueError as e:
    print(e)
