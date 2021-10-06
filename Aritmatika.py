# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)
print("")

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)
print("")

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)
print("")

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)
print("")

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)
print("")

# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)
print("")

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)
print("")

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen ** (pangkat)
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
print("")

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
print("")

# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)