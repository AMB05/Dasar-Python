import sys

data =[]
data2=[]

hasil2 = 0
ulang = int(input("Berapa Banyak Program Ingin Berjalan ? " ))
for i in range (0,ulang) :
    print()
    print("Data ke : ", i+1 )
    a=str(input("Input Nama Pelanggan           : "))
    b=int(input("Input Jumlah Baris Program     : "))
    c=int(input("Input Jumlah Halaman Program   : "))
    tanya= str(input("Apakah Ingin menggunakan DataBase ? "))
    if tanya == "ya":
        
        total=b*5000 + c*50000 + 200000
        data.insert(0,a)
        data.insert(1,b)
        data.insert(2,c)
        data.insert(3,total)
        
        print ("Nama Pelanggan          = ", data[0])
        print ("Jumlah Baris Program    = ", data[1])
        print ("Jumlah Halaman Program  = ", data[2])
        print ("Total Biaya             = ", data[3])
    elif tanya == "T":
        
        total2=b*5000 + c*50000
        data2.insert(0,a)
        data2.insert(1,b)
        data2.insert(2,c)
        data2.insert(3,total2)
        print ("Nama Pelanggan          = ", data2[0])
        print ("Jumlah Baris Program    = ", data2[1])
        print ("Jumlah Halaman Program  = ", data2[2])
        print ("Total Biaya             = ", data2[3])

print(data)
print(data2)
data.extend(data2)
print ('Extend : ', data)


def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
 
c=[data]
print("===============================")
print("Sebelum Bubble Sort")
print(c)
print("Setelah Bubble Sort")
bubbleSort(c)
print(c)
print("")