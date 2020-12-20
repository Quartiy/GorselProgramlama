import re



mail = input("Email adresinizi giriniz: ")

if re.match(r"[^@]+@[^@]+\.[^@]+", mail):
    print("bu bir mail adresi")
else:
    print("bu bir mail adresi değil.")
