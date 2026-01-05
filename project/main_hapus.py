import json
from logic import kategori_umur

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=2)

def hapus_user(nama):
    users = load_users()
    user_baru = [u for u in users if u["nama"].lower() != nama.lower()]

    if len(users) == len(user_baru):
        print("User tidak ditemukan")
    else:
        save_users(user_baru)
        print("User berhasil dihapus")

def tampilkan_users(users):
    for user in users:
        print(
            user["nama"],
            "-",
            user["umur"],
            "=>",
            kategori_umur(user["umur"])
        )

nama = input("Masukkan nama user yang akan dihapus: ")
hapus_user(nama)