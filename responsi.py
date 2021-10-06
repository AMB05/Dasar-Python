#                   Program Kasir
Nama     = []
Nim      = []

beras = 75000
gula  = 23000
minyak= 25000
sabun = 15000
teh   = 10000
tepung= 50000

berass = []
gulaa = []
minyakk = []
sabunn = []
tehh = []
tepungg = []

print("---** Program Kasir Toko Sembako **---")
print("")
print("")
ulang = int(input("Masukan Berapa Kali Program Akan Mengulang ? = "))
for Value in range(0, ulang) :
    print("")
    print("Data ke-", Value+1, ":")
    Nim.append(input("Nim   = "))
    Nama.append(input("Nama = "))
    print("")

    print("Nama Barang")
    print("--------------------------")
    print("Beras = Rp.", beras)
    print("Gula  = Rp.", gula)
    print("Minyak= Rp.", minyak)
    print("Sabun = Rp.", sabun)
    print("Teh   = Rp.", teh)
    print("Tepung= Rp.", tepung)
    print("")
    print("")
    
    print("Masukan Yang dibeli :")
    print("---------------------------------")
    berass.append(int(input("Beras      = ")))
    gulaa.append(int(input("Gula        = ")))
    minyakk.append(int(input("Minyak    = ")))
    sabunn.append(int(input("Sabun      = ")))
    tehh.append(int(input("Teh          = ")))
    tepungg.append(int(input("Tepung    = ")))

    hasil = (berass[Value]+gulaa[Value]+minyakk[Value]+sabunn[Value]+tehh[Value]+tepungg[Value])
    
    print("")
    print("Total Belanja Anda = Rp.", hasil)
    if hasil >= 100000 :
        gift = ("Anda Mendapat Kupon Gratis Parkir")
        print (gift)
        print("")
        tanya_member=str(input("Apakah Anda Memilki Member ? "))
        if tanya_member == "ya" or "YA" or "Ya" or "yA" or "y" or "Y" :
            member = str(input("Member Apa Yang Anda Miliki?"))
            if member == "silver" or "Silever" or "SILVER" :
                print("Anda Mendapat Diskon 10%")
                diskon = hasil - (hasil * 10 / 100)
                print("")
            elif member == "gold" or "Gold" or "GOLD" :
                print("Anda Mendapat Diskon 20%")
                diskon = hasil - (hasil * 20 / 100)
                print("")
            elif member == "platinum" or "Platinum" or "PLATINUM" :
                print("Anda Mendapat Diskon 30%")
                diskon = hasil - (hasil * 25 / 100)
                print("")
            else :
                print("Anda Salah Input")
                print("")
                
            print("")
            print("Nama = ", Nama)
            print("Nim  = ", Nim)
            print("-------------------------")
            print("Gift yang didapat    = ", gift)
            print("Member Yang dimiliki = ", member)
            print("Total Belanja Kamu   = Rp.", hasil , "(Sebelum Diskon)")
            print("Total Belanja Kamu   = Rp.", diskon ,"(Setelah Diskon)")
            print("------------------------------------------------------")
            print("Terimakasih Telah Belanja, ")
            print("")

    elif hasil >=200000 and hasil <=300000 :
        gift = ("Anda Mendapat Kupon Belanja RP.50000")
        print(gift)
        print
        tanya_member=str(input("Apakah Anda Memilki Member ? "))
        if tanya_member == "ya" or "YA" or "Ya" or "yA" :
            member = str(input("Member Apa Yang Anda Miliki?"))
            if member == "silver" or "Silever" or "SILVER" :
                print("Anda Mendapat Diskon 10%")
                diskon = hasil - (hasil * 10 / 100)
                print("")
            elif member == "gold" or "Gold" or "GOLD" :
                print("Anda Mendapat Diskon 20%")
                diskon = hasil - (hasil * 20 / 100)
                print("")
            elif member == "platinum" or "Platinum" or "PLATINUM" :
                print("Anda Mendapat Diskon 30%")
                diskon = hasil - (hasil * 25 / 100)
                print("")
            else :
                print("Anda Salah Input")
                print("")

            print("")
            print("Nama = ", Nama)
            print("Nim  = ", Nim)
            print("-------------------------")
            print("Gift yang didapat    = ", gift)
            print("Member Yang dimiliki = ", member)
            print("Total Belanja Kamu   = Rp.", hasil , "(Sebelum Diskon)")
            print("Total Belanja Kamu   = Rp.", diskon ,"(Setelah Diskon)")
            print("----------------------------------------------------")
            print("Terimakasih Telah Belanja, ")
            print("")

    elif hasil >300000 :
        gift = ("Anda Mendapat Kupon Undian Sepeda")
        print (gift)
        print("")
        tanya_member=str(input("Apakah Anda Memilki Member ? "))
        if tanya_member == "ya" or "YA" or "Ya" or "yA" :
            member = str(input("Member Apa Yang Anda Miliki?"))
            if member == "silver" or "Silever" or "SILVER" :
                print("Anda Mendapat Diskon 10%")
                diskon = hasil - (hasil * 10 / 100)
                print("")
            elif member == "gold" or "Gold" or "GOLD" :
                print("Anda Mendapat Diskon 20%")
                diskon = hasil - (hasil * 20 / 100)
                print("")
            elif member == "platinum" or "Platinum" or "PLATINUM" :
                print("Anda Mendapat Diskon 30%")
                diskon = hasil - (hasil * 25 / 100)
                print("")
            else :
                print("Anda Salah Input")
                print("")

            print("")
            print("Nama = ", Nama)
            print("Nim  = ", Nim)
            print("-------------------------")
            print("Gift yang didapat    = ", gift)
            print("Member Yang dimiliki = ", member)
            print("Total Belanja Kamu   = Rp.", hasil , "(Sebelum Diskon)")
            print("Total Belanja Kamu   = Rp.", diskon ,"(Setelah Diskon)")
            print("---------------------------------------------------")
            print("Terimakasih Telah Belanja, ")





    

    

        



    

