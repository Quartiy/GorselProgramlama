yazi = input("Lütfen cümle giriniz:")
arama = input("Lütfen aradığınız kelimeyi giriniz:")
a = yazi.find(arama)
if (a > 0):
	hedef = yazi[a - 1]
	hedef2 = yazi[a + len(arama)]
	print(hedef + arama + hedef2)
else:
	print("Aradığınız, kelime bulunamadı.!")
