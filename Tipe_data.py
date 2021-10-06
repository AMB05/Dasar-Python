#tipe data integer
a = 11
print("data : ", a)
print("~bertipe : ", type(a))
print("")

# tipe data float
b = 11.5
print("data : ", b)
print("~bertipe : ", type(b))
print("")

# tipe data string
aaaaaa = "nama saya adalah........"
print("data : ", aaaaaa)
print("~ bertipe : ", type(aaaaaa))
print("")

# tipe data boolean
d = False
e = True
print("data : ", d)
print("~ bertipe : ", type(d))
print("")
print("data : ", e)
print("~ bertipe : ", type(e))
print("")

# bilangan kompleks      Menyatakan pasangan angka real dan imajiner
f = complex(5,6)
g = complex(5j)
print("data : ", f)
print("~ bertipe : ", type(f))
print("data : ", g)
print("~ bertipe : ", type(g))
print("")


# tipe data double, char, dari bahasa C yang di import
from ctypes import c_double, c_char     #import data

h_double = c_double(10.5)
print("data : ", h_double)
print("~ bertipe : ", type(h_double))
print("")

