#contoh 1 model segita
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

#contoh 2
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

#contoh 3
c = ""
baris = 1
x = int(input("Masukkan angka :"))
# Looping Baris
while baris <= x:
	# Looping Kolom Spasi Kosong
	kolom = baris	
	while kolom > 1:
		c = c + "   "
		kolom = kolom - 1
		# Looping Kolom Bintang	
	kanan = 0
	while kanan <= (x - baris):
		c = c + " * "
		kanan = kanan + 1	
		
	c = c + "\n"
	baris = baris + 1
print (c)
print("")

#contoh 4
d = ""
x = int(input("Masukkan angka :"))
baris = x
# Looping Baris
while baris >= 0:
	# Looping Kolom Spasi Kosong
	kolom = baris
	while kolom > 0:
		d = d + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang	
	kanan = 1
	while kanan < (x - (baris-1)):
		d = d + " * "
		kanan = kanan + 1		
		
	d = d + "\n"
	baris = baris - 1
	
print (d)

#contoh5
e = ""
x = int(input("Masukkan angka :"))
baris = x
# Looping Baris
while baris >= 0:
	# Looping Kolom Spasi Kosong
	kolom = baris
	while kolom > 0:
		e = e + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 1
	while kiri < (x - (baris-1)):
		e = e + " * "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		e = e + " * "
		kanan = kanan + 1	

	e = e + "\n\n"
	baris = baris - 1
print (e)
print("")

#contoh 6
f = ""
baris = 1
x = int(input("Masukkan angka :"))
print ("\n")
# Looping Baris
while baris <= x:
	kolom = baris
	# Looping Kolom Spasi Kosong
	while kolom > 1:
		f = f + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 0
	while kiri <= (x - baris):
		f = f + " * "
		kiri = kiri + 1	
	# Looping Kolom Bintang Sisi Kanan
	kanan = kiri	
	while kanan > 1:
		f = f + " * "
		kanan = kanan - 1

	f = f + "\n\n"
	baris = baris + 1
print (f)
print("")

#contoh 7
g = ""
x = int(input("Masukkan angka :"))
baris = x
# Looping Baris
while baris >= 0:
	# Looping Kolom Spasi Kosong
	kolom = baris
	while kolom > 0:
		g = g + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang Sisi Kiri		
	kiri = 1
	while kiri < (x - (baris-1)):
		g = g + " * "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		g = g + " * "
		kanan = kanan + 1	

	g = g + "\n\n"
	baris = baris - 1
baris = 1	
# Looping Baris
while baris <= x:
	kolom = baris+1
	# Looping Kolom Spasi Kosong
	while kolom > 1:
		g= g + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 0
	while kiri < (x - baris):
		g = g + " * "
		kiri = kiri + 1	
	# Looping Kolom Bintang Sisi Kanan
	kanan = kiri	
	while kanan > 1:
		g = g + " * "
		kanan = kanan - 1

	g = g + "\n\n"
	baris = baris + 1
print (g)

#contoh 8
h = ""
baris = 1
x = int(input("Masukkan angka :"))
print ("\n")
# Looping Baris
while baris < x:
	# Looping Kolom Spasi Kosong
	kolom = baris
	while kolom > 1:
		h = h + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang Sisi Kiri
	kiri = 0
	while kiri <= (x - baris):
		h = h + " * "
		kiri = kiri + 1	
	# Looping Kolom Bintang Sisi Kanan
	kanan = kiri	
	while kanan > 1:
		h = h + " * "
		kanan = kanan - 1

	if (baris+1) <= x:
		h = h + "\n\n"
	baris = baris + 1

baris = x-1	
# Looping Baris
while baris >= 0:
	# Looping Kolom Spasi Kosong
	kolom = baris
	while kolom > 0:
		h = h + "   "
		kolom = kolom - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 1
	while kiri < (x - (baris-1)):
		h = h + " * "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		h = h + " * "
		kanan = kanan + 1	

	h = h + "\n\n"
	baris = baris - 1
print (h)