# ===============================================
# REVIEW MATERI PYTHON FUNCTION
# ===============================================

# Fungsi adalah blok kode yang dapat digunakan ulang
# Fungsi didefinisikan menggunakan kata kunci `def`

# ===============================================
# 1. FUNGSI TANPA PARAMETER
# ===============================================
def sapa():
    """Fungsi ini menyapa pengguna."""
    print("Halo, selamat datang!")

sapa()               # Print terminal: Halo, selamat datang!
print(sapa())        # None; Tidak menghasilkan output

# ===============================================
# 2. FUNGSI DENGAN PARAMETER
# ===============================================
def sapa_pengguna(nama):
    """Fungsi dengan parameter."""
    print(f"Halo {nama}, senang bertemu denganmu!")

sapa_pengguna("Wahyu")          # Print terminal: Halo Wahyu, senang bertemu denganmu!
print(sapa_pengguna("Wahyu"))   # None; Tidak menghasilkan output
sapa_pengguna(input("Masukkan nama anda: "))

# ===============================================
# 3. RETURN VALUE
# ===============================================
def hitung_luas_persegi(sisi):
    """Mengembalikan nilai luas persegi."""
    return sisi * sisi

luas = hitung_luas_persegi(5) # Output: 25 -> luas
print("Luas persegi:", luas)  # Print terminal: Luas persegi: 25

# ===============================================
# 4. DEFAULT ARGUMENT
# ===============================================
def greet(nama="Pengguna"):
    print(f"Halo {nama}!")

greet()               # Output: Halo Pengguna!
greet("Andi")          # Output: Halo Andi!

# ===============================================
# 5. KEYWORD ARGUMENTS
# ===============================================
def biodata(nama, usia):
    print(f"Nama: {nama}, Usia: {usia} tahun")

biodata(usia=25, nama="Rani")  # urutan tidak masalah karena menggunakan keyword

# ===============================================
# 6. FUNGSI SEBAGAI OBJEK
# ===============================================
def tambah(x, y):
    return x + y

operasiValue = tambah(1, 2) # operasi = 3
print('Tipe data operasiValue: ', type(operasiValue))

operasiFunction = tambah    # operasi = function tambah
print('Tipe data operasiFunction: ', type(operasiFunction))
print(operasiFunction(3, 4))  # Output: 7

# ===============================================
# 7. NESTED FUNCTION DAN SCOPE
# ===============================================
def luar():
    pesan = "Hai dari fungsi luar"

    def dalam():
        print(pesan)

    dalam()

luar()  # Output: Hai dari fungsi luar

# ===============================================
# 8. LAMBDA FUNCTION
# ===============================================
kali = lambda a, b: a * b
print(type(kali))
print(kali(3, 5))  # Output: 15

# ===============================================
# 9. PRAKTIK SEDERHANA
# ===============================================
# Buat fungsi untuk menentukan bilangan ganjil/genap
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

print(cek_ganjil_genap(10))  # Output: Genap
print(cek_ganjil_genap(7))   # Output: Ganjil

# ===============================================
# 10. JENIS-JENIS FUNGSI
# ===============================================

# --- Callback Function ---
# Fungsi yang dikirim sebagai argumen ke fungsi lain dan dipanggil kembali di dalamnya

def panggil_callback(callback):
    print("Memanggil fungsi callback:")
    callback()

def contoh_callback():
    print("Saya adalah callback!")

panggil_callback(contoh_callback)  # Output: Saya adalah callback!

# --- Calling other Function
# Fungsi yang memanggil fungsi lain melalui blok kode di bawahnya

def printHasilHitung(hasilHitung, fungsiHitung):
    print(f'Hasil {fungsiHitung} adalah {hasilHitung}')

def tambahAngka(a,b):
    hasil = a + b
    printHasilHitung(hasil, 'tambah')
    return hasil

def kurangAngka(a,b):
    printHasilHitung(a - b, 'kurang')
    return a - b

def kaliAngka(a,b):
    printHasilHitung(a * b, 'kali')
    return a * b

def bagiAngka(a,b):
    printHasilHitung(a / b, 'bagi')
    return a / b

# Boleh ganti dengan fungsi lain (tambah, kurang, kali, bagi)
tambahAngka(2,4)

# --- Recursive Function ---
# Fungsi yang memanggil dirinya sendiri

def countdown(counter):
    print(counter)
    counter -= 1 # compound statement

    if(counter >= 0): # stop condition
        countdown(counter)

countdown(3)

def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1) # 5 * faktorial(5-1)
                                    # 5 * 4 * faktorial(4-1)
                                    # 5 * 4 * 3 * faktorial(3-1)
                                    # 5 * 4 * 3 * 2 * faktorial(2-1)
                                    # 5 * 4 * 3 * 2 * 1

print(faktorial(5))  # Output: 120

# --- Built-in Function ---
# Fungsi bawaan dari Python, seperti len(), print(), type(), dll.

print("Fungsi print untuk menampilkan objek apapun ke terminal")
print(12)
print(len("Python"))  # Output: 6
print(type(123))      # Output: <class 'int'>

# --- Anonymous Function (lambda) ---
# Sudah dibahas di bagian 8

# ===============================================
# AKHIR DARI REVIEW FUNCTION
# ===============================================
# Catatan:
# - Gunakan fungsi untuk memecah masalah menjadi bagian kecil
# - Dokumentasikan fungsi dengan docstring (googling)
# - Gunakan return untuk mengembalikan hasil jika diperlukan
# - Kenali jenis-jenis fungsi dan penggunaannya

# Contoh Docstring
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
 
    return

# Cara 1 menampilkan dokumentasi
print("Using __doc__:")
print(my_function.__doc__)

# Cara 2 menampilkan dokumentasi
print("Using help:")
help(my_function)

# print(8/0)
# print('Hello, world!'[5::-1])
x = 5
if x >= 5:
    print("This morning is sunny")
elif x > 4:
    print("This morning it was cloudy")
else:
		print("None")

for i in range(5):
    if i == 3:
        pass  # Placeholder, no action
    print(i)

number = 0

# for i in range(5):
# 	for j in range(3):
# 		number += 1
          
a = 'x' or None
print(a) # 3

lee, kim, tim = "x", None, ()
print(not lee if lee or kim else tim) # False
print(not lee)