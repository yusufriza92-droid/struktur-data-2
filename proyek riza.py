# Input nama
nama = input("Masukkan nama anda: ")

# Cek nama (misalnya nama yang dianggap benar: "riza")
if nama.lower() == "riza":
    print("Selamat datang", nama)
else:
    print("Program selesai")

# Input umur
umur = int(input("Masukkan umur anda: "))

# Percabangan umur
if umur >= 18:
    print("anda cukup umur")
elif umur > 0 and umur < 18:
    print("anda belum cukup umur")
elif umur <= 0:
    print("anda belum lahir")
    
# Tambahan kondisi
if umur > 60:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")