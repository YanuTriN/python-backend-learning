import json
from logic import kategori_umur

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=2)

def tampilkan_users(users):
    for user in users:
        print(
            user["nama"],
            "-",
            user["umur"],
            "=>",
            kategori_umur(user["umur"])
        )

users = load_users()

nama_cari = input("Masukkan nama yang akan diupdate: ")
ditemukan = False

for user in users:
    if user["nama"].lower() == nama_cari.lower():
        try:
            umur_baru = int(input("Masukkan umur baru: "))
            user["umur"] = umur_baru
            ditemukan = True
            break
        except ValueError:
            print("Umur harus angka")
            exit()

if ditemukan:
    save_users(users)
    print("Data berhasil diupdate\n")
else:
    print("Daata tidak ditemukan\n")

tampilkan_users(users)