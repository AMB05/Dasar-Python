#perulangan while
"""start;
while condition:
  # kode program yang akan diulang
  increment
"""

#contoh 1 while-do
i = 1
while i <= 5:
  print("semoga weekend beneran libur")
  i+=1
print("")

#contoh 2
i = 0
while i < 5:
  print(i)
  i += 1
print("")

#contoh 3 ascending
i = 0
while (i < 5):
    print("i = " , i)
    i = i + 1
print("lanjut...")
print("")

#contoh 4
n = int(input("Masukkan banyak pengulangan: "))
i = 1
while i <= n:
   print("ini lagi diulang yang ke-", i)
   i+=1
print("")

#contoh 5 descending
i = 5
while i >= 1:
   print(i)
   i = i - 1 
print("")

#contoh 6 
i = int(input("masukan nilai i :"))
n = int(input("masukan banyak perulangan : "))
while i >= n:
   print(i)
   i = i - 1 
print("")

#contoh 7
n = 'ya'
i = 0
while(n == 'ya'):
    i += 1
    n = str(input("Apakah Ingin Ulang ? "))
print ("Total perulagan: ", i) 
print("")
#atau
#do-while
n = 'ya'
i = 0
while(n == 'ya'):
    i += 1
    n = str(input("Ulang lagi tidak? "))
    if (n == 'tidak'):
        break
print ("Total perulagan: ", i)
print("")

#contoh 8 nested loop bersarang
i = 2
while(i < 20):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : 
      print(i, " adalah bilangan prima")
    i = i + 1
print("")

#contoh 9
i = 0
n = 1
#Perulangan WHILE
while (i < 10) :
     print("Perulangan Ke ", i)
     while(n < 3) :
         print(" Perulangan ke ", i , " , ",n)
         n +=1
     #diluar perulangan n
     n = 1
     i +=1
#diluar_perulangan var_nilai
print("i = ",int(i)," = 10. Bernilai False")
print("");

#contoh 10 model segita
a = ""
baris = 1
x = int(input("Masukkan angka :"))
# Looping Baris
while baris <= x:
	kolom = baris
  # Looping Kolom
	while kolom > 0:
		a = a + " * "
		kolom = kolom - 1
		
	a = a + "\n"
	baris = baris + 1
print (a)
print("")

#contoh 11
b = ""
baris = int(input("Masukkan angka :"))
#Looping Baris
while baris >= 0:
	kolom = baris
  # Looping Kolom
	while kolom > 0:
		b = b + " * "
		kolom = kolom - 1
		
	b = b + "\n"
	baris = baris - 1
print (b)
print("")

#contoh 12
x = "SemogaLongWeekend"
while x:
  print( x, " ")
  x = x[1:] 

#contoh 13
