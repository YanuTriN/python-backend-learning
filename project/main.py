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

nama = input("Masukkan nama: ")
try:
    umur = int(input("Masukkan umur: "))
except ValueError:
    print("Umur harus angka")
    exit()

users.append({
    "nama": nama,
    "umur": umur
})
save_users(users)
tampilkan_users(users)