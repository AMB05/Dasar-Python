# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("")
print("suhu adalah",celcius, "Celcius")
print("")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")
print("")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")
print("")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, "Kelvin")


print("\n===PROGRAM KONVERSI TEMPERATUR===\n")
def hasil (celcius) :
   reamur = (4/5) * celcius
   fahrenheit = ((9/5) * celcius) + 32
   kelvin = celcius + 273
   print("=======================================================\n")
   print("suhu                      = ",celcius, "Derajat Celcius")
   print("suhu dalam reamur         = ",reamur, "Derajat Reamur")
   print("suhu dalam fahrenheit     = ",fahrenheit, "Derajat Fahrenheit")
   print("suhu dalam kelvin         = ",kelvin, "Derajat Kelvin")
   print("=======================================================\n")

a=float(input("Masukan Suhu Celcius : "))
hasil(a)