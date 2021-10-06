"""Dictionary adalah stuktur data yang bentuknya seperti kamus,
   Ada kata kunci kemudian ada juga nilaninya,
   Kata kuncinya sendiri harus unik, dan nilai boleh diisi denga apa saja
   atau bebas"""
#bentuk dictionary
# Membuat dictionary kosong
a= {}
b = {1: 'sepatu', 2: 'tas'} # dictionary dengan kunci integer
c = {'warna': 'merah', 1: [2,3,5]}# dictionary dengan kunci campuran
d = dict({'a':'sepatu', 'b':'bola'})# membuat dictionary menggunakan fungsi dict()
print(a)
print(b)
print(c)
print(d)
print("")

Data = {'Nama': 'Birri',
        'NPM': 5181011076, 
        'prodi': 'TK'}
print ("Data['Nama']: ", Data['Nama'])
print ("Data['NPM'] : ", Data['NPM'])
print ("Data['Prodi]: ", Data['prodi'])
print("")

#mengubah nilai
Data['Nama'] = "Arriva"
print(Data)
print("")

#menambah nilai
Data['status'] = "otw kaya"
print(Data)
print("")

#mengambil nilai
print(Data.get('status'))
print("")

#nested dict
dict = {'Nama': 'Birri',
        'NPM': 5181011076, 
        'prodi': 'TK',
        'sosial_media' : 
            {
                'instagram' : 'arriva_riva05',
                'status' : 'otw kaya'
            }
        }
print ("dict['Nama']  : ", dict['Nama'])
print ("dict['NPM']   : ", dict['NPM'])
print ("dict['Prodi'] : ", dict['prodi'])
print ("dict['Sosmed']: ", dict['sosial_media']['instagram'])
print ("dict['Status']: ", dict['sosial_media']['status'])
print("")

#mengambil panjang nilai
print("panjang data : %d" %len(dict))
print("")



"""
#fungsi copy
Data = {'Nama': 'Birri',
        'NPM': 5181011076, 
        'prodi': 'TK'}
print ("Data['Nama']: ", Data['Nama'])
print ("Data['NPM'] : ", Data['NPM'])
print ("Data['Prodi]: ", Data['prodi'])
print("")
Data2 = Data.copy()
print(Data2)
print("")


fungsi...
cmp(dict1, dict2) 	Membandingkan unsur keduanya.
len(dict) 	        Memberikan panjang total Dictionary. Ini sama dengan jumlah item dalam Dictionary.
str(dict)       	Menghasilkan representasi string yang dapat dicetak dari Dictionary
type(variable)  	Mengembalikan tipe variabel yang lulus. Jika variabel yang dilewatkan adalah Dictionary, maka akan mengembalikan tipe Dictionary.
clear()     	        Menghapus semua anggota dictionary
copy() 	                Mengembalikan shallow copy dari dictionary
fromkeys(seq[, v]) 	Mengembalikan dictionary baru dengan kunci-kuncinya dari seq, dan nilainya sama dengan v (defaultnya None)
get(key[,d])    	Mengembalikan nilai dari key. Bila key tidak tersedia, kembalikan d (defaultnya None)
items() 	        Mengembalikan view baru (berisi semua pasangan key,value dari dictionary
keys() 	                 Mengembalikan view baru (berisi semua kunci pada dictionary)
pop(key[,d]) 	        Menghapus anggota yang memiliki kunci key dan mengembalikan nilai d jika kunci tidak ada dalam dictionary. Bila d tidak dibuat, dan key tidak ditemukan, akan menghasilkan KeyError
popitem()       	Menghapus anggota secara acak. Menghasilkan KeyError jika dictionary kosong
setdefault(key[,d])     Bila key ada dalam dictionary, kembalikan nilainya. Bila tidak, sisipkan key dengan nilai d dan kembalikan d (defaulnya None)
update([other]) 	Mengupdate dictionary dengan menambahkan anggota dari dictionary lain other, timpa (overwrite) bila ada kunci yang sama
values() 	        Mengembalikan view baru (berisi semua value pada dictionary)

methode...
dict.clear()     	            Menghapus semua elemen Dictionary
dict.copy()                 	    Mengembalikan salinan Dictionary
dict.fromkeys()     	            Buat Dictionary baru dengan kunci dari seq dan nilai yang disetel ke nilai.
dict.get(key, default=None) 	    For key, nilai pengembalian atau default jika tombol tidak ada dalam Dictionary
dict.has_key(key)                   Mengembalikan true jika key dalam Dictionary, false sebaliknya
dict.items() 	                    Mengembalikan daftar dari pasangan tuple dictionary (key, value)
dict.keys() 	                    Mengembalikan daftar key dictionary
dict.setdefault(key, default=None)  Mirip dengan get (), tapi akan mengatur dict [key] = default jika kunci belum ada di dict
dict.update(dict2) 	            Menambahkan pasangan kunci kata kunci dict2 ke dict
dict.values() 	                    Mengembalikan daftar nilai dictionary
"""