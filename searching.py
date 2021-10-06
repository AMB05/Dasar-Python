#Sequential Search
Data = [10, 4, 2, 3, 7, 1, 6, 8]
caridata = int(input("Masukkan nilai yang dicari: "))
ditemukan = False
for i in range(0, len(Data)): 
    print(Data[i])
    if Data[i] == caridata: 
        ditemukan = True
        break
if ditemukan:
    print('Data ditemukan!')
else:
    print('Data tidak ditemukan!')
print("")

#Linier Search
def linierSearch(Data,cari):
  posisi = 0
  ketemu = False
  while posisi<len(Data) and not ketemu:
    if cari == Data[posisi]:
      ketemu = True
    posisi+=1
  print('Angka ketemu di index = %i'%posisi)

Data = []
a = int(input('Masukan berapa panjang list yang ingin dibuat = '))
for i in range(a):
  x = int(input('Masukan angka ke %i untuk list = '%(i+1)))
  Data.append(x)
cari = int(input('Masukan angka yang ingin dicari = '))
linierSearch(Data,cari)
print("")

#Linier Search
def linearSearch(Data,list):
    ditemukan = False
    posisi = 0
    while posisi < len(list) and not ditemukan:
        if list[posisi] == Data:
            ditemukan = True
        posisi = posisi + 1
    return ditemukan
tas = ['buku','pinsil','pulpen','note book','laptop','handphone']
Data = input('apa yang ingin kamu cari didalam tas?')
temukanitem = linearSearch(Data,tas)
if temukanitem:
    print ('Ya, benda tersebut berada didalam tas')
else:
    print ('Oops, benda tersebut tidak berada didalam tas')
print("")

#Linear Search dengan for loop
Data = [114, 110, 77, 112, 65, 80, 80, 90, 113, 109, 110, 86, 108, 85, 87, 65,90, 95, 109]
caridata = 109 # elemen yang dicari
index = -1 # posisi elemen yang dicari
for i in range(len(Data)):
  if Data[i] == caridata:
    index = i
    break

if index == -1:
  print('Nilai ',caridata,'tidak ditemukan')
else:
  print('Nilai ',caridata,'ditemukan pada indeks',index)
print("")

#Linear search dengan sentinel
Data = [114, 110, 77, 112, 65, 80, 80, 90, 113, 109, 110, 86, 108, 85, 87, 65,90, 95, 109]
caridata = 109 # elemen yang dicari
jumlah = len(Data)
Data.append(caridata) # tambahkan elemen data pada akhir list sebagai sentinel
index = 0
while Data[index] != caridata:
   index+=1

if index < jumlah:
  print('Nilai',caridata,'ditemukan pada indeks',index)   
else:
  print('Nilai ',caridata,'tidak ditemukan')
print("")

#================================================================#

#binary search
Data = [1,3,4,6,7,8,10,13,14,18,19,21,24,3,7,40,45,71]
caridata = 7
print('Mencari nilai',caridata,'dengan binary search','pada list',Data)
ditemukan = False
batas_awal = 0
batas_akhir = len(Data) - 1
while not ditemukan and batas_awal <= batas_akhir:
  pos_cari = batas_awal + (batas_akhir-batas_awal)//2 #Rumus mengambil posisi tengah
  print('posisi pencarian: index',pos_cari,'dengan nilai',Data[pos_cari])  
  if Data[pos_cari] == caridata:
    ditemukan = True 
  elif Data[pos_cari] > caridata:
    batas_akhir = pos_cari-1 # geser 1 titik lebih kecil dari posisi sekarang
  else:
    batas_awal = pos_cari+1 # geser 1 titik lebih besar dari posisi sekarang

if ditemukan:
  print('Nilai',caridata,'ditemukan pada indeks',pos_cari)
else:
  print('Nilai',caridata,'tidak ditemukan')

#binary search
def binarySearch (data, posisi, x, cari): 
  if x >= posisi:
    mid = posisi + (x - posisi) // 2
    if data[mid] == cari: 
      return mid 
        
    elif data[mid] > cari: 
      return binarySearch(data, posisi, mid-1, cari) 
        
    else:
      return binarySearch(data, mid + 1, x, cari) 
  else:
    return -1  

data = [ 2, 3, 4, 10, 40 ] 
cari = int(input('Masukan Data yang akan dicari = '))
result = binarySearch(data, 0, len(data)-1, cari) 
if result != -1: 
    print ("Data Ditemukan!") 
else: 
    print ("Data Tidak Ditemukan!") 

#binary search
def binary_search(a,b):
	batas_awal = 0
	batas_akhir = len(a)-1
	ditemukan = False
	while( batas_awal<=batas_akhir and not ditemukan):
		mid = (batas_awal + batas_akhir)//2
		if a[mid] == b :
			ditemukan = True
		else:
			if b < a[mid]:
				batas_akhir = mid - 1
			else:
				batas_awal = mid + 1	
	return ditemukan
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))

#================================================================#

#binary interpolationSearch
def interpolationSearch(data, n, x): 
  bawah = 0
  hi = (n - 1) 
    while bawah <= hi and x >= data[lo] and x <= arr[hi]: 
        if bawah == hi: 
            if data[lo] == x:  
                return bawah; 
            return -1;    
        pos  = bawah + int(((float(hi - bawah) / 
            ( data[hi] - data[bawah])) * ( x - data[bawah])))   
        
        if data[pos] == x: 
            return pos 
        
        if data[pos] < x: 
            bawah = pos + 1; 
        
        else: 
            hi = pos - 1; 
    return -1

data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(data) 
x = int(input('Masukan Data yang akan dicari = ')) 
index = interpolationSearch(data, n, x) 
if index != -1: 
    print ("Data Ditemukan!") 
else: 
    print ("Data Tidak Ditemukan!")

#binary interpolationSearch
def Interpolation_Search (arr,target):
    start = 0
    end = len(arr)-1
    found = False

    while start <= end and found == False:
        if start == end:
            if arr[start] == target: 
                return "{} is at {} index".format(target,pos)
            return "not found"    

        pos = start + (((end-start)//(arr[end]-arr[start])) * (target-arr[start]))               

        if arr[pos] == target:      
            return "{} is at {} index".format(target,pos)  

        if arr[pos] < target:
            start = pos + 1;
        else:
            end = pos - 1;    

    return "Not Found"

arr = [10, 20, 40, 77, 86, 89, 91]
print(Interpolation_Search(arr, 86))