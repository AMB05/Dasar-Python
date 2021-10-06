




def data(data1):
    for index in range(1, len(data1)):
        x = data1[index]
        y = index - 1
        while y >=0 and data1[y] > x:
            data1[y + 1] = data1[y]
            y -= 1
        data1[y + 1] = x
index = 0
print("=====================================")
data_ = int(input("Input banyak data = "))
data1 = []
for i in range(1,data_+1):
    angka = int(input("Masukan nilai yang ke %i = " %i))
    data1.append(angka)
print ("Data ialah = ")
print (data1)
data(data1)
print(data1)

data2=[data1]

caridata = int(input("Masukkan nilai yang dicari: "))
ditemukan = True
for i in range(0, len(data2)): 
    print(data2[i])
    if data2[i] == caridata: 
        ditemukan = False
        break
if ditemukan:
    print('Data ditemukan!')
else:
    print('Data tidak ditemukan!')
print("")
