"""
    library python adalah suatu bentuk fungsi dari randaom() atau bilangan acak,
    yang dapat digunakan dalam berbagai macam kasus, dan biasanya untuk memecahkan 
    kasus Monte Carlo. 
    Randomisasi juga dapat digunakan untuk mengacak suatu tampilan produk, 
    atau digunakan saat proses pengacakan sebuah mesin cerdas (AI).
"""

#random.random()
""" random.random() akan menghasilkan angka yang memiliki tipe data float 
    yang dimulai dari 0,0 hingga 1,0 dan pada fungsi ini tidak perlu 
    menambahkan argumen.
"""
import random
print(random.random())
print("")

#random.randint()
""" menghasilkan angka acak dengan tipe data integer yang berada pada rentang yang 
    telah ditentukan.
"""
import random
data1 = random.randint(1,100)
data2 = random.randint(1,100)
print("data ke-1 : "+str(data1))
print("data ke-2 : "+str(data2))
print(random.randint(2,4))
print("")

#random.randrange()
"""
    memilih secara acak elemen yang berada pada rentang 
    yang telah dibuat menggunakan argumen start, stop, dan step.
"""
import random
data1 = random.randrange(1,10)
data2 = random.randrange(1,10,2)
data3 = random.randrange(0,101,10)
print("angka1: "+str(data1))
print("angka2: "+str(data2))
print("angka3: "+str(data3))
print(random.randrange(0, 3))
print("")

#random.choice()
"""
    menghasilkan secara acak elemen yang dipilih dari sekuensi yang 
    tidak kosong atau non-empty dan jika kosong maka IndexError.
"""
import random
data1 = random.choice('ALGORITMA')
data2 = random.choice([12,24,36,48,60,72,84,96])
print("hasil1: "+str(data1))
print("hasil2: "+str(data2))
print(random.choice('SAYA'))
print("")

#random.shuffle()
"""
    untuk mengubah urutan setiap elemen yang ada pada list, menjadi
    acak.
"""
import random
list1 = [12,24,36,48,60,72,84,96]
random.shuffle(list1)
print("hasil1: "+str(list1))

#https://docs.python.org/3/library/random.html