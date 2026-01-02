users = [
    {"nama" : "Andi", "umur" : 0},
    {"nama" : "Rudi", "umur" : 19},
    {"nama" : "Dewi", "umur" : 34},
]

from logic import kategori_umur

for user in users:
    umur = int(user.get("umur", 0))
    kategori = kategori_umur(user["umur"])
    print(user["nama"], "-", user["umur"], "=>", kategori)