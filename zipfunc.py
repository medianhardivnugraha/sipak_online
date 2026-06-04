from tabulate import tabulate

data1 = range(1,6)
data2 = ['a','b','c','d']
data3 = (1,3,5,7,9,11)
data4 = 'mnopqrs'
data5 = 50
data6 = {"angka1": 2, "angka2":1}
data7 = True

print("Hasil zip data2 & data3:", list(zip(data2, data3)))
print("Hasil zip data1, data2 & data6 value only:", list(zip(data1, data2, data6.values())))

for i in data6:
    print(i)
print()
dataNama = ['Andi', 'Budi', 'Ceci', 'Dedi']
dataUmur = [24, 27, 35, 55]

print('Example 1')
# Example 1
for nama, umur in zip(dataNama, dataUmur):
    print("Nama: {}\nUmur: {}".format(nama, umur))
    print("------------")

print('Example 2')
# Example 2

# range(5) = 0, 1, 2, 3, 4 # start 0, stop 5, step 1
# range(10,0,-2) = 10, 8, 6, 4, 2 # start 10, stop 0, step -2
for i, j in zip(range(5), range(10,0,-2)):
    print("i = {} & j = {}".format(i, j))

print()
# versi List in Dictionary (2D data)

studentList = {
    "dataNama": ['Andi', 'Budi', 'Ceci', 'Dedi'],
    "dataUmur": [24, 27, 35, 55]
}


print("List Nama Siswa Sekolah Dasar Negeri Jombang Mojokerto (Jomok)")
print(tabulate(studentList, headers="keys", tablefmt="grid"))