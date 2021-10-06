"""List adalah struktur data pada python 
   yang mampu menyimpan lebih dari satu data, seperti array,
   menyimpan banyak data dalam satu veriabel"""


#list kosong
Data =[]
print("")

#contoh list tipe data
a = ["buku", 21, True, 34.12]
print(a)
print("")

# mengakses list
Data = [1,4,9,16,25,36,49,64]
Subdata1 = Data[3]
Subdata2 = Data[-3]
print (Data)
print (Subdata2)
print (Subdata1)
print("")

# memotong list
Data2 = [100,200,300,400,500,600,700,800]
Subdata3 = Data2[2:4]
Subdata4 = Data2[:4]
print (Data2)
print (Subdata3)
print (Subdata4)
print("")

# menambah list
Data3 = Data + Data2
print(Data3)
print("")

# merubah nilai dari list
Data = [1,4,9,16,25,36,49,64]
Data[4] = 87
Data[0] = 2
print(Data)
print("")

# Mengcopy list ke variable baru
a = Data[:]
a[7] = 87
print(a)
print("")

# merubah content list dengan menggunakan metoda slicing
Data[3:5] = [11,12]
print(Data)
print("")

# List dalam list (nested list)
x = [Data,Data2]
print(x)
print("")

# mengakses list dalam multidimensional list (mengakses list dalam nested)
y = x[0][2]
z = x[1][6]
print(y,z)
print("")

#menghapus nilai
del Data2 [5]
print(Data2)
print("")



# methods untuk list
Data.append(30)
Data.insert(3, 29)
print(Data)
print("")

# Function yang bisa kita gunakan kepada list
panjang_list = len(Data)
print(panjang_list)


"""
fungsi...
len(list) 	Memberikan total panjang list.
max(list) 	Mengembalikan item dari list dengan nilai maks.
min(list) 	Mengembalikan item dari list dengan nilai min.
list(seq) 	Mengubah tuple menjadi list.

methode...
list.appen"d(obj)   	    Menambahkan objek obj ke list
list.count(obj)         	Jumlah pengembalian berapa kali obj terjadi dalam list
list.extend(seq)        	Tambahkan isi seq ke list
list.index(obj) 	        Mengembalikan indeks terendah dalam list yang muncul obj
list.insert(index, obj) 	Sisipkan objek obj ke dalam list di indeks offset
list.pop(obj = list[-1]) 	Menghapus dan mengembalikan objek atau obj terakhir dari list
list.remove(obj) 	        Removes object obj from list
list.reverse() 	            Membalik list objek di tempat
list.sort([func])       	Urutkan objek list, gunakan compare func jika diberikan
"""