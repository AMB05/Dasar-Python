"""Tuple adalah stuktur data yang digunakan untuk 
   menyimpan sekumpulan data. Tuple bersifat immutable
   artinya isi tuple tidak bisa kita ubah dan hapus, 
   tapi dapat kita isi dengan berbagai macam nilai dan objek."""

# Membuat tuple kosong
Data = ()

# List
Ganjil = [1,3,5,7,9]
# Tuple
Genap = (2,4,6,6,8,10)
print(type(Ganjil))
print(type(Genap))
print("")

# tuple single
Data = ('harga tiket murah',)
Data2 = "semua","lagi","diskon",
print(Data)
print(Data2)
print("")

#mengakses nilai tuple
Data = ('1', '2', '3', '4','5','6','7','8','9','10',)
print(Data[-2])
print(Data[0])
print(Data[7])
print("")

#slicing tuple
Data = ('1', '2', '3', '4','5','6','7','8','9','10',)
print(Data[0:2])
print(Data[:-4])
print(Data[2:2])
print("")

#mengambil nilai tuple
Data = ('1', '2', '3', '4','5','6','7','8','9','10',)
print("Jumlah Data : %d" % len(Data))

#len tuple
Data = ('1', '2', '3', '4','5','6','7','8','9','10',)
print(len(Data))
print("")

#nested tuple
Data3 = [Data, Data2]
print((1, 2, 3) + (4, 5, 6))
print(("punyaku",) * 3)
print(Data3)
print("")

#mengakses tuple pada nested
x = Data3[0][4]
y = Data3[1][1]
print(x)
print(y)
print("")

#packing dan unpacking
Data4 = 5181011076, 'Arriva', 'Teknik komputer', #packing
NPM, nama, prodi = Data4 #unpacking
print(NPM)
print(nama)
print(prodi)
print("")

#mengganti nilai tuple dan menconvert kelist
Data = ('1', '2', '3', '4','5','6','7','8','9','10',)
Data5 = list(Data)
Data5[1] = "angka ini yang di ganti"
Data = tuple(Data5)
print(Data5) 
print("")

# Membership tuple
Data = ('1', '2', '3', '4','5','6','7','8','9','10',)
# In operation
print('2' in Data)
print('11' in Data)
print('12' not in Data)# Not in operation