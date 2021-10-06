print("selamat datang di toko suka maju")
print("================================")
namabarang1 = str(input("masukan nama barang ="))
harga1 = int(input("masukan harga barang = Rp."))
namabarang2 = str(input("masukan nama barang ="))
harga2 = int(input("masukan harga barang = Rp."))

print("")
hargatotal = harga1 + harga2 
print("Total belanja kamu ialah = Rp.", hargatotal)
print("=======================================")

member = str(input("apakah kamu memiliki member ?"))
if member == "ya":
    member2 = str(input("apakah jenis member kamu ?"))
    if member2 == "platinum":
        print("")
        print("Identitas member kamu ialah : ", member2)
        print("kamu mendapat diskon 30%")
        print("")
        print("Harga Total Belanja kamu ialah = Rp.", hargatotal)
        hargadiskon = hargatotal * 30 / 100
        hargaakhir = hargatotal - hargadiskon
        print("harga total belanja kamu setelah diskon ialah = Rp.", hargaakhir)
    elif member2 == "gold":
        print("")
        print("Identitas member kamu ialah : ", member2)
        print("kamu mendapat diskon 20%")
        print("")
        print("Harga Total Belanja kamu ialah = Rp.", hargatotal)
        hargadiskon = hargatotal * 20 / 100
        hargaakhir = hargatotal - hargadiskon
        print("harga total belanja kamu setelah diskon ialah = Rp.", hargaakhir)
    elif member2 == "silver":
        print("")
        print("Identitas member kamu ialah : ", member2)
        print("kamu mendapat diskon 10%")
        print("")
        print("Harga Total Belanja kamu ialah = Rp.", hargatotal)
        hargadiskon = hargatotal * 10 / 100
        hargaakhir = hargatotal - hargadiskon
        print("harga total belanja kamu setelah diskon ialah = Rp.", hargaakhir)
    else :
        print("data yang kamu masukan salah")

elif member == "tidak":
    print ("anda mendapat gratis kupon parkir")
    print ("Total harga yang anda bayar ialah = Rp.", hargatotal)

else :
    print("data yang kamu masukan salah")
