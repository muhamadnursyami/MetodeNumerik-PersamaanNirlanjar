def persamaan(t):
    """
    Fungsi ini mendefinisikan persamaan yang ingin diselesaikan.
    """
    return 2 * t**3 + 5 * t**2 - 10 * t - 4

def turunan_persamaan(t):
    """
    Fungsi ini mendefinisikan turunan persamaan yang ingin diselesaikan.
    """
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
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(b - a) < tol or func(c) == 0:
            return c

        if func(c) * func(a) < 0:
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
    
    for i in range(max_iter):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if abs(func(c)) < tol:
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
    for i in range(max_iter):
        x_old = x
        x = x - func(x) / turunan_func(x)
        
        # Stopping criterion: Check if the change in x is smaller than tol
        if abs(x - x_old) < tol:
            return x
    
    raise ValueError("Metode Newton-Raphson tidak konvergen dalam jumlah iterasi yang ditentukan.")
    

# Input nilai awal dan akhir untuk Metode Bagi Dua
a_bagi_dua = float(input("Masukkan nilai awal (a) untuk Metode Bagi Dua: "))
b_bagi_dua = float(input("Masukkan nilai akhir (b) untuk Metode Bagi Dua: "))

# Solve menggunakan Metode Bagi Dua
try:
    hasil_bagi_dua = metode_bagi_dua(persamaan, a_bagi_dua, b_bagi_dua)
    print(f"Hasil Metode Bagi Dua: {hasil_bagi_dua}")
except ValueError as e:
    print(e)

# Input nilai awal dan akhir untuk Metode Regula Falsi
a_regula_falsi = float(input("Masukkan nilai awal (a) untuk Metode Regula Falsi: "))
b_regula_falsi = float(input("Masukkan nilai akhir (b) untuk Metode Regula Falsi: "))

# Solve menggunakan Metode Regula Falsi
try:
    hasil_regula_falsi = metode_regula_falsi(persamaan, a_regula_falsi, b_regula_falsi)
    print(f"Hasil Metode Regula Falsi: {hasil_regula_falsi}")
except ValueError as e:
    print(e)

# Input nilai awal untuk Metode Newton-Raphson
x0_newton_raphson = float(input("Masukkan nilai awal (x0) untuk Metode Newton-Raphson: "))

# Solve menggunakan Metode Newton-Raphson
try:
    hasil_newton_raphson = metode_newton_raphson(persamaan, turunan_persamaan, x0_newton_raphson)
    print(f"Hasil Metode Newton-Raphson: {hasil_newton_raphson}")
except ValueError as e:
    print(e)
