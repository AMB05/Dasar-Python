# fungsi adalah blok kode terorganisir dan dapat 
# digunakan kembali yang digunakan untuk melakukan 
# sebuah tindakan/action, fungsi menggunakan kata kunci def.
"""
def nama_fungsi ():
    statement(s)

return [expression]
"""

#bentuk fungsi (tanpa parameter dan tanpa nilai balik)
def Data():
    print ("Ini adalah fungsi dari Data") #statement / isi
#memanggil fungsi
Data()
print("")

def Data():
    a=10+9
    print(a)
Data()
print("")

"===================================================================="

#fungsi dengan parameter tanpa nilai balik
def Data(a,b):
    hasil = a+b
    print("hasil a + b =", hasil)
Data(2,3)
print("")

def Data(P,L,T):
    volume = P*L*T
    print("Volume Balok = ", volume)
Data(10,12,5)
print("")

"===================================================================="

#fungsi tanpa parameter dengan nilai balik
def Data():
    return print("ini menggunakan nilai balik")
Data()
print("")

def hitung():
    return 5*10
print("hasil = ",hitung())
print("")

"===================================================================="

#fungsi dengan parameter dengan nilai balik
def hitung(a,b):
    return a + b
print("hasil = ",hitung(8,12))
print("")

def luas_persegi_panjang(panjang, lebar):
	luas = panjang*lebar
	return luas
print(luas_persegi_panjang(9,8,))
print("")

def volume_balok(panjang, lebar, tinggi):
	return panjang*lebar*tinggi
print(volume_balok(3,4,5))
print("")
"===================================================================="

#variabel global
a=10
def Data():
   a=11
   return a
print(Data())
print("")
print(a)
print("")

a=100
def Data():
    global a
    a=110
    return a
print(Data())
print("")
print(a)
print("")

"===================================================================="

# fungsi rekursif adalah fungsi yang dapat memanggil dirinya 
# sendiri secara berulang-ulang hingga suatu kondisi yang 
# di definisikan terpenuhi atau bernilai benar (true). 

# Fungsi rekrusif juga bisa disebut perulangan rekursif 
# (karena fungsinya memang sama seperti looping) 
# perbedaannya adalah jika pada perulangan iteratif menggunakan 
# instruksi perulangan seperti for dan while, sementara pada 
# fungsi rekursif perulangan di lakukan pada fungsi itu sendiri.

#contoh pada pencarian faktorial
def faktorial(x):
  if x<=1: # base scenario
    return 1
  else:
    f = x * faktorial(x-1)
  return f
print(faktorial(5))
print("")
#gambaran
"""
    faktorial(5)
    5 * faktorial(4)
    5 * 4 * faktorial(3)
    5 * 4 * 3 * 2 * 1
    5 * 4 * 6
    5 * 24
    120
"""

#contoh pada pangkat
def pangkat(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat(x,y-1)
print(pangkat(5,2))
print("")

#contoh pada bilangan fibonacci
def fibonacci(n):
   if n == 0 or n == 1:
      return n
   else:
      return (fibonacci(n-1) + fibonacci(n-2))
print(fibonacci())
#gambaran
"""
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    1 n n n n 1

"""