users = [
    {"nama": "Andi", "umur": "13"},
    {"nama": "Budi", "umur": "17"},
    {"nama": "Citra", "umur": "25"}
]

def kategori_umur(umur):
    if umur < 13:
        return "Anak"
    elif umur <= 17:
        return "Remaja"
    else:
        return "Dewasa"
    
for user in users:
    kategori = kategori_umur(int(user["umur"]))

    print ("Nama:", user["nama"])
    print ("Umur:", user["umur"])
    print ("Kategori:", kategori)
    print("----------")