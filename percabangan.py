#percabangan

# if..., 
# if... else, 
# if... elif... else






#pernyataan if...elif...else
#contoh kasus hasil nilai
print("pernyataan if...elif...else")
nilai = int(input("Inputkan nilaimu: "))

if nilai >= 90:
   grade = "A"
elif nilai >= 80:
   grade = "B+"
elif nilai >= 70:
   grade = "B"
elif nilai >= 60:
   grade = "C+"
elif nilai >= 50:
   grade = "C"
elif nilai >= 40:
   grade = "D"
else:
   grade = "E"

print("Grade: ", grade)





