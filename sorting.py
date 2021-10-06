#bentuk umum
x = ['e','a','u','i','o']
y = 'Python'
print(sorted(x))
print(sorted(y))
print(sorted(x, reverse=True))
print("")

def data(z):
    return z[1]
random = [(2,2), (3,4), (4,1), (1,3)]
print("Sebelum di Sorting")
print(random)
sortedlist = sorted(random, key=data)
print('Setelah di Sorting:', sortedlist)
print("")


#Buble Short
def tukar(data1,i,j): 
    data1[i],data1[j]=data1[j],data1[i]
def bubblesort(data):
    ubah = True
    sesi = len(data) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while sesi > 1 and ubah:
        ubah = False
        j = 1
        while j < sesi:
            if data[j]<data[j-1]:
                ubah = True
                tukar(data,j,j-1) 
            j+=1
        print(data)
        #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
        if not ubah:
            print("hasil akhir = %s" %str(data))
        sesi-=1
print("===============================")
print("Sebelum Bubble Sort")
a=[4,13,67,35,21,77,89,67]
print(a)
print("Setelah Bubble Sort")
bubblesort(a)
print("")

#Buble Short
def tukar(data2,i,j):
    data2[i],data2[j]=data2[j],data2[i]
def BubbleSort(data):
    ubah = True
    x = len(data)-1
    while x >= 0 and ubah:
        ubah = False
        for i in range(x,0,-1):
            if data[i]<data[i-1]:
                tukar(data,i,i-1)
                ubah = True
        if not ubah:
            return data
        x-=1
print("===============================")
print("Sebelum Bubble Sort")
b=[35,33,12,45,65,90,100,87,21,101]
print(b)
print("Setelah Bubble Sort")
BubbleSort(b)
print(b)
print("")

#Buble Short
def bubbleSort(x):
    for passnum in range(len(x)-1,0,-1):
        for i in range(passnum):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
 
c = [23,7,32,99,4,15,11,20]
print("===============================")
print("Sebelum Bubble Sort")
print(c)
print("Setelah Bubble Sort")
bubbleSort(c)
print(c)
print("")

#Selection Sort
def tukar(data3,i,j):
   data3[i],data3[j]=data3[j],data3[i]
def Selection(data):
   perubahan = True
   sesi = 0 #digunakan untuk membuat sesi pencarian
   while sesi < len(data)-1 and perubahan:
       perubahan = False
       dataterendah = sesi
       datalanjutan = dataterendah + 1
       while datalanjutan < len(data):
           if data[dataterendah] > data[datalanjutan]:
               dataterendah = datalanjutan
           datalanjutan += 1
       if dataterendah != sesi:
           tukar(data,dataterendah,sesi)
           perubahan = True
       print(data)  
       #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
       if not perubahan:
           print("hasil akhir = %s" %str(data))
       sesi += 1
print("===============================")
print('Sebelum Selection Sort')
d = [54,26,13,93,17,77,44,31]
print(d)
print("Setelah Selection Sort")
Selection(d)
print("")

#Selection Sort
def selectionSort(data4):
     for slot in range(len(data4)-1):
       position=slot
       for location in range(len(data4)-1,slot,-1):
           if data4[location]<data4[position]:
               position = location

       temp = data4[slot]
       data4[slot] = data4[position]
       data4[position] = temp
e = [54,26,93,17,77,31,44,55,20]
print("===============================")
print("Sebelum Selection Sort")
print(e)
print("Setelah Selection Sort")
selectionSort(e)
print(e)
print("")

#Selection Sort
def SelectionSort(x):
   for isi in range(len(x)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if x[lokasi]>x[Max]:
               Max = lokasi
 
       temp = x[isi]
       x[isi] = x[Max]
       x[Max] = temp
 
f = [23,7,32,99,4,15,11,20]
print("===============================")
print("Sebelum Selection Sort")
print(f)
print("Setelah Selection Sort")
SelectionSort(f)
print(f)
print("")

#Insertion Sort
def insertionSort(data5):
    for index in range(1, len(data5)):
        x = data5[index]
        y = index - 1
        while y >=0 and data5[y] > x:
            data5[y + 1] = data5[y]
            y -= 1
        data5[y + 1] = x

index = 0
print("=====================================")
panjangList = int(input("Input panjang list yang diinginkan = "))
data5 = []
for i in range(1,panjangList+1):
    angka = int(input("Masukan angka yang ke %i untuk List = " %i))
    data5.append(angka)

print ("Sebelum di insertion sort =" )
print (data5)
insertionSort(data5)
print ("Setelah di insertion sort =" )
print (data5)
print("")

#Insertion Sort
def insertion_sort(data6):
    for i in range(1, len(data6)):
        x = data6[i]
        j = i-1
        while j >=0 and x < data6[j] :
                data6[j+1] = data6[j]
                j -= 1
        data6[j+1] = x
 
g = [12, 11, 13, 5, 6]
insertion_sort(g)
print("===============================")
print ("hasil : ")
for i in range(len(g)):
    print ("%d" %g[i])
print("")

#Insertion Sort
def InsertionSort(data7):
   for index in range(1,len(data7)):
    x = data7[index]
    posisi = index
    while posisi>0 and data7[posisi-1]>x:
        data7[posisi]=data7[posisi-1]
        posisi = posisi-1
    data7[posisi]=x
 
h = [23,7,32,99,4,15,11,20]
print("===============================")
print("Sebelum Insertion Sort")
print(h)
print("Setelah Selection Sort")
InsertionSort(h)
print(h)
print("")

#Quick Sort
def quickSort(alist):
  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
  if first<last:
    splitpoint = partition(alist,first,last)
    quickSortHelper(alist,first,splitpoint-1)
    quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False
  while not done:
    while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
      leftmark = leftmark + 1
    while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
      rightmark = rightmark -1
    if rightmark < leftmark:
      done = True
    else:
      temp = alist[leftmark]
      alist[leftmark] = alist[rightmark]
      alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
print("===============================")
print("Sebelum Quick Sort")
print(alist)
print("Setelah Quick Sort")
quickSort(alist)
print(alist) 
print("")

#Quick Sort
def partition(l, bwh, atas):
  pivot = l[bwh]
  pos_batas = bwh+1
  for j in range(bwh+1,atas):
    if l[j] < pivot:
      l[pos_batas],l[j]=l[j],l[pos_batas]
      pos_batas += 1
  l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
  return pos_batas

def quicksort(l, bwh, atas):
  if atas <= bwh:
    return
  q = partition(l, bwh, atas)
  quicksort(l, bwh, q-1)
  quicksort(l, q, atas)
  return l
angka = [34,21,45,32,12,31,19,23,54,31,25,27]
print("===============================")
print('Sebelum sort:',angka)
quicksort(angka,0,len(angka))
print('Setelah sort:',angka)

#Merge Short
def merge_sort(list_bilangan):
  jumlah_bilangan =  len(list_bilangan)
  if jumlah_bilangan > 1:
    posisi_tengah = len(list_bilangan)//2
    potongan_kiri = list_bilangan[:posisi_tengah]
    potongan_kanan = list_bilangan[posisi_tengah:]
    
    merge_sort(potongan_kiri)
    merge_sort(potongan_kanan)

    jumlah_bilangan_kiri = len(potongan_kiri)
    jumlah_bilangan_kanan = len(potongan_kanan)
    c_all,c_kiri,c_kanan = 0,0,0 # pencacah/counter
    print('Sebelum merge:',list_bilangan)  
    print('Potongan sebelum merge:',potongan_kiri,':',potongan_kanan)
    while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
      if c_kiri == jumlah_bilangan_kiri: # elemen di potongan kiri habis
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      elif c_kanan == jumlah_bilangan_kanan: # elemen di potongan kanan habis
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      elif potongan_kiri[c_kiri] <= potongan_kanan[c_kanan]: # nilai elemen di potongan kiri lebih kecil
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      else: # nilai elemen di potongan kanan lebih besar
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      c_all = c_all + 1
    print('Setelah merge:', list_bilangan)
    print()
          
angka = [6,5,3,1,8,7,2,4]
print('Sebelum sort:',angka)
print("")
merge_sort(angka)
print('Setelah sort:',angka)
print("")

#Merge Short
def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2

		L = arr[:mid]

		R = arr[mid:]

		mergeSort(L)

		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Sebelum Short", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sesudah Short ", end="\n")
	printList(arr)


#Radix Short
def countingSort(arr, exp1): 

	n = len(arr) 

	output = [0] * (n) 

	count = [0] * (10) 

	for i in range(0, n): 
		index = (arr[i] / exp1) 
		count[int(index % 10)] += 1

	for i in range(1, 10): 
		count[i] += count[i - 1] 

	i = n - 1
	while i >= 0: 
		index = (arr[i] / exp1) 
		output[count[int(index % 10)] - 1] = arr[i] 
		count[int(index % 10)] -= 1
		i -= 1

	i = 0
	for i in range(0, len(arr)): 
		arr[i] = output[i] 

def radixSort(arr): 

	max1 = max(arr) 

	exp = 1
	while max1 / exp > 0: 
		countingSort(arr, exp) 
		exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66] 
radixSort(arr) 
for i in range(len(arr)): 
	print(arr[i]) 

