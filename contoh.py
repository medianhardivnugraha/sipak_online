# Informasi kustomer
# Contoh untuk capstone
# - Nama
# - Umur
# - Kota
# - Koordinat Kota (Tempat tinggal)
# - Barang Favorit
# - Aktif/Tidak


custInformation = [
["Budi", 45, "Tangerang", (112.600, 98.00), ["Gitar", "Labubu"], True],
["Raharjo", 30, "Menteng Pusat", (115.700, 100.00), ["Pilates", "Candy Crush"], False],
["Sukijan", 65, "Angke", (100.000, 95.00), ["Burung", "Tanaman"], True]
]

column_name = ["Nama", "Umur", "Kota Domisili", "Koordinat Kota Domisili", "Barang Favorit", "Status Aktif"]

names = ['james', 'yatmi', 'rony the backstabber', 'dedi']
newList = []

for name in names:
    if name.lower() != 'dedi':
        newList.append(name)
    else:
        newList.append('feri')