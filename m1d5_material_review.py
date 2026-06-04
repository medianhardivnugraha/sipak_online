# === REVIEW MATERI DICTIONARY DAN SET ===
# File ini berisi materi ringkasan tentang dictionary dan set dalam Python,
# dilengkapi dengan dokumentasi dan contoh kode praktikal.

# =====================================================
# 1. DICTIONARY
# =====================================================
# Dictionary adalah struktur data yang menyimpan pasangan key-value.
# Dapat digunakan untuk menyimpan data terstruktur seperti data siswa, buku, dll.

print("=== 1. DICTIONARY ===")

x = [1,2,3]

# --- 1.1 Membuat dan Mengakses Data ---
siswa = {
    # string, int, float, tuple -> key
    "nama": "Andi",
    "umur": 17,
    "kelas": "12 IPA 1",
}

kumpulan_siswa = {
    'nama1':"Andi",
    'nama1':"Budi",
    'nama1':"Ceci",
    'nama1':"KDM",
    'nama1':"Eki"
}

print(kumpulan_siswa)

siswa = dict(nama="Andi", umur=17, kelas="12 IPA 1")
print("1.1 Dictionary Awal:", siswa)

print("Akses nama:", siswa["nama"])
print("Akses umur (dengan get):", siswa.get("umur"))

# Akses item yang tidak ada dalam dictionary
# print("Akses kota: ", siswa['kota']) # error
print("Akses kota: ", siswa.get("kota", "key tidak ada"))

print(siswa.keys())

print("Semua key:", list(siswa.keys())) # index
print("Semua value:", list(siswa.values())) # isi
print("Semua item:", list(siswa.items())) # pasangan key-value

# --- 1.2 Menambahkan atau Memperbarui Data ---
print("\n--- 1.2 Menambahkan / Memperbarui ---")
siswa["hobi"] = "Futsal"  # Menambah key baru
siswa["umur"] = 18        # Memperbarui umur
print("Setelah update:", siswa)

# update()
siswa.update({"nama": "Budi", "umur": 19})
print("Setelah update:", siswa)
# siswa["nama"] = "Caca"
# siswa["umur"] = 20

# --- 1.3 Menghapus Data ---
print("\n--- 1.3 Menghapus ---")
del siswa["kelas"]
print("Setelah menghapus 'kelas':", siswa)

umur_dihapus = siswa.pop("umur")
print("Setelah pop 'umur':", siswa)
print("Nilai umur yang dihapus:", umur_dihapus)

terakhir = siswa.popitem()
print("Setelah popitem:", siswa)
print("Item terakhir yang dihapus:", terakhir)

# --- 1.4 Metode Lain ---
print("\n--- 1.4 Metode Lain ---")
# Clear & Copy
backup = siswa.copy()
siswa.clear()
print("Setelah clear:", siswa)
print("Backup siswa:", backup)

# Fromkeys
print("Dictionary dari fromkeys:")
kunci = ["nama", "umur", "jurusan"]
data_kosong = dict.fromkeys(kunci, "belum diisi")
print(data_kosong)


# --- 1.5 Looping Dictionary ---
print("\n--- 1.5 Looping Dictionary ---")
# ngambil key aja dari objek dictionary utuh
for key in backup:
    print(key)

# ngambil key dan value terpisah dari objek tuple pasangan key-value
for key, value in backup.items():
    print(f"{key} → {value}")

# ngambil pasangan key dan value dari objek tuple pasangan key-value
for item in backup.items():
    print(item)

# ngambil value aja dari objek list of values
for values in backup.values():
    print(values)

# =====================================================
# 2. SET
# =====================================================
# Set adalah kumpulan data unik (tidak ada duplikat).
# Set tidak memiliki urutan (unordered) dan tidak bisa diakses dengan indeks.

print("\n=== 2. SET ===")

# --- 2.1 Membuat dan Mengakses Set ---
# int, float, string -> value
angka = {1, 2, 3, 4, 4, 5}
print("2.1 Isi Set (tanpa duplikat):", angka)

# --- 2.2 Menambahkan dan Menghapus ---
print("\n--- 2.2 Menambah / Menghapus ---")
angka.add(6)
print("Setelah tambah 6:", angka)

angka.discard(3)
print("Setelah hapus 3:", angka)

# angka.remove(10) # Error
# print("Setelah hapus 10: ", angka)

angka.discard(10)
print("Setelah hapus 10: ", angka)

# --- 2.3 Operasi Set (dengan method) ---
print("\n--- 2.3 Operasi Set ---")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

print("Union:", A.union(B))                     # Gabungan
print("Intersection:", A.intersection(B))       # Irisan
print("Difference (A - B):", A.difference(B))   # Selisih A dengan B
print("Difference (B - A):", B.difference(A))   # Selisih B dengan A
print("Symmetric Difference:", A.symmetric_difference(B))  # XOR
print("Symmetric Difference:", B.symmetric_difference(A))  # XOR
# AND, OR, NOT
# XOR (CROSS OR), NOR (NOT OR), NAND (NOT AND), XNOR (CROSS NOT OR)


# --- 2.4 Subset dan Superset ---
print("\n--- 2.4 Subset dan Superset ---")
C = {1, 2}
D = {1, 2, 3, 4, 5}
E = {3, 4, 5}

print("C:", C)
print("D:", D)
print("E:", E)
print("C adalah subset dari D:", C.issubset(D))
print("D adalah superset dari C:", D.issuperset(C))
print("C adalah subset dari A:", C.issubset(A))
print("E adalah subset dari D:", E.issubset(D))
print("D adalah superset dari E:", D.issuperset(E))
print("C adalah disjoint dari E:", C.isdisjoint(E))

# --- 2.5 Looping Set ---
print("\n--- 2.5 Looping Set ---")
for item in B:
    print("Angka:", item)