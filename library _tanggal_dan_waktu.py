#datetime 
"""
Tanggal dalam Python bukanlah tipe datanya sendiri, 
tetapi kita dapat mengimpor modul bernama datetime 
untuk bekerja dengan tanggal sebagai objek tanggal.
"""

#menentukan tanggal sekarang
import datetime
tanggal = datetime.date.today() 
print(tanggal)
print("")

#menentukan tanggal dan waktu sekarang
import datetime
sekarang = datetime.datetime.now() 
print(sekarang)
print("")

#mengisi variabel dengan tanggal tertentu
from datetime import date
tgl = date(2020, 6, 25) # tahun, bulan, tanggal
print(tgl)
print("")

#mengakses tahun, bulan, tanggal dari sebuah date object
from datetime import date
hari_ini = date.today() 
print("Tahun ini        :", hari_ini.year)
print("Bulan ini        :", hari_ini.month)
print("Tanggal hari ini :", hari_ini.day)
print("")

#mengakses jam, menit, detik, dan microsecond dari sebuah time object
from datetime import time
a = time(5, 15, 5, 728172)
print("jam          =", a.hour)
print("menit        =", a.minute)
print("detik        =", a.second)
print("microsecond  =", a.microsecond)
print("")

#mengisi variabel dengan nilai waktu tertentu
from datetime import time
a = time(20, 31, 7) 
print(a)
b = time(hour = 8, second = 56) 
print(b)
c = time(1, 11, 27, 991727) 
print(c)
print("")

#menghitung selisih antara dua tanggal
from datetime import date
tgl1 = date(year = 2000, month = 7, day = 10)
tgl2 = date.today()
selisih = tgl2 - tgl1
print('Saya Hidup di Dunia ini Selama ', selisih.days, ' hari')
print("")

#Format tanggal dan waktu dengan strftime
from datetime import datetime
saat_ini = datetime.now()
jam = saat_ini.strftime('%H:%M:%S')
print('Jam              :', jam)
tgl = saat_ini.strftime('%d/%m/%Y') # format dd/mm/YY
print('Tanggal          :', tgl)
tgl_jam = saat_ini.strftime("%d/%m/%Y, %H:%M:%S") # format dd/mm/YY H:M:S 
print('tanggal dan jam  : ', tgl_jam)
print("")


"""
Time tuple

Index 	Field 	            Value
0   	4-digit year 	    2008
1   	Bulan       	    1 sampai 12
2 	    Hari 	            1 sampai 31
3 	    Jam 	            0 sampai 23
4 	    Menit 	            0 sampai 59
5 	    Detik 	            0 sampai 61
6   	Hari dalam Minggu 	0 sampai 6 (0 adalah Senin)
7   	Hari dalam Bulan 	1 sampai 366
8   	Daylight savings 	-1, 0, 1, -1 means library determines DST

Index 	Atribut 	    Value
0 	    tm_year 	    2008
1 	    tm_mon 	        1 sampai 12
2 	    tm_mday 	    1 sampai 31
3 	    tm_hour 	    0 sampai 23
4 	    tm_min 	        0 sampai 59
5 	    tm_sec 	        0 sampai 61
6 	    tm_wday 	    0 sampai 6 (0 adalah Senin)
7 	    tm_yday 	    1 sampai 366
8 	    tm_isdst 	    -1, 0, 1, -1 means library determines DST
"""

"""
Fungsi DateTime

time.altzone 	                                Diimbangi zona waktu DST lokal, dalam detik di sebelah barat UTC, jika seseorang didefinisikan. Ini negatif jika zona waktu DST lokal berada di sebelah timur UTC (seperti di Eropa Barat, termasuk Inggris). Gunakan saja ini jika siang hari tidak nol.
time.asctime([tupletime]) 	                    Menerima time-tupel dan mengembalikan string 24-karakter yang dapat dibaca seperti ‘Tue Dec 11 18:07:14 2008’.
time.clock() 	                                Mengembalikan waktu CPU saat ini sebagai jumlah floating-point detik. Untuk mengukur biaya komputasi dari berbagai pendekatan, nilai time.clock lebih bermanfaat daripada time.time ().
time.ctime([secs])      	                    Seperti asctime (localtime (detik)) dan tanpa argumen seperti asctime ()
time.gmtime([secs]) 	                        Menerima instan yang diungkapkan dalam hitungan detik sejak zaman dan mengembalikan waktu tuple t dengan waktu UTC. Catatan: t.tm_isdst selalu 0
time.localtime([secs]) 	                        Menerima instan yang dinyatakan dalam hitungan detik sejak zaman dan mengembalikan waktu tuple t dengan waktu setempat (t.tm_isdst adalah 0 atau 1, tergantung pada apakah DST berlaku seketika oleh peraturan lokal).
time.mktime(tupletime) 	                        Menerima instan dinyatakan sebagai time-tuple di waktu setempat dan mengembalikan nilai floating-point dengan instan yang dinyatakan dalam hitungan detik sejak zaman.
time.sleep(secs) 	                            Menangguhkan panggilan untuk beberapa detik.
time.strftime(fmt[,tupletime]) 	                Menerima instan dinyatakan sebagai tupel waktu di waktu lokal dan mengembalikan sebuah string yang mewakili instan seperti yang ditentukan oleh string fmt.
time.strptime(str,fmt=’%a %b %d %H:%M:%S %Y’) 	Parses str sesuai dengan format string fmt dan mengembalikan format instant-tuple.
time.time() 	                                Mengembalikan waktu saat ini secara instan, jumlah detik mengambang beberapa detik sejak zaman itu.
time.tzset() 	                                Mengatur ulang aturan konversi waktu yang digunakan oleh rutinitas perpustakaan. Variabel lingkungan TZ menentukan bagaimana hal ini dilakukan.
"""

"""
Atribut Time

time.timezone 	Atribut time.timezone adalah offset dalam detik zona waktu lokal (tanpa DST) dari UTC (> 0 di Amerika; <= 0 di sebagian besar Eropa, Asia, Afrika).
time.tzname 	Atribut time.tzname adalah sepasang string yang bergantung pada lokal, yang merupakan nama zona waktu lokal tanpa dan dengan DST.
"""

"""
Atribut Calander

calendar.calendar(year,w=2,l=1,c=6) 	Mengembalikan string multiline dengan kalender untuk tahun tahun yang diformat menjadi tiga kolom yang dipisahkan oleh ruang c. W adalah lebar karakter setiap tanggal; Setiap baris memiliki panjang 21 * w + 18 + 2 * c. L adalah jumlah baris untuk setiap minggu.
calendar.firstweekday( ) 	            Mengembalikan pengaturan saat ini untuk hari kerja yang dimulai setiap minggu. Secara default, saat kalender pertama kali diimpor, ini adalah 0, yang berarti Senin.
calendar.isleap(year) 	                Pengembalian True jika tahun adalah tahun kabisat; Jika tidak, False
calendar.leapdays(y1,y2) 	            Mengembalikan jumlah lompatan hari dalam tahun-tahun dalam rentang (y1, y2).
calendar.month(year,month,w=2,l=1)  	Mengembalikan string multiline dengan kalender untuk bulan bulan tahun, satu baris per minggu ditambah dua baris header. W adalah lebar karakter setiap tanggal; Setiap baris memiliki panjang 7 * w + 6. L adalah jumlah baris untuk setiap minggu.
calendar.monthcalendar(year,month)  	Mengembalikan daftar daftar int. Setiap sublist menunjukkan seminggu. Hari di luar bulan bulan tahun diatur ke 0; Hari dalam bulan ditetapkan ke hari ke bulan, 1 dan ke atas.
calendar.monthrange(year,month) 	    Mengembalikan dua bilangan bulat. Yang pertama adalah kode hari kerja untuk hari pertama bulan bulan di tahun; Yang kedua adalah jumlah hari dalam sebulan. Kode hari kerja adalah 0 (Senin) sampai 6 (Minggu); Angka bulan adalah 1 sampai 12.
calendar.prcal(year,w=2,l=1,c=6) 	    Seperti kalender cetak.calendar (tahun, w, l, c).
calendar.prmonth(year,month,w=2,l=1) 	Seperti kalender cetak. Bulan (tahun, bulan, w, l).
calendar.setfirstweekday(weekday)   	Mengatur hari pertama setiap minggu sampai hari kerja kode hari kerja. Kode hari kerja adalah 0 (Senin) sampai 6 (Minggu).
calendar.timegm(tupletime) 	            Kebalikan dari time.gmtime: menerima waktu instan dalam bentuk tupel waktu dan mengembalikan detik yang sama seperti jumlah floating-point dalam hitungan detik sejak zaman.
calendar.weekday(year,month,day) 	    Mengembalikan kode hari kerja untuk tanggal yang ditentukan. Kode hari kerja adalah 0 (Senin) sampai 6 (Minggu); Bulan adalah 1 (Januari) sampai 12 (Desember).
"""
# referensi https://www.w3schools.com/python/python_datetime.asp
# https://docs.python.org/3/library/datetime.html