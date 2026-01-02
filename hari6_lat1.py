users = [
    {"nama" : "andi", "umur" : "15"},
    {"nama" : "budi", "umur" : "22"}
]

def kategori(umur):
    if umur < 13:
        return "Anak"
    elif umur <= 17:
        return "Remaja"
    else:
        return "Dewasa"
    
for user in users:
    hasil = kategori(int(user["umur"]))

    print("Nama:", user["nama"])
    print("Umur:", user["umur"])
    print("Kategori:", hasil)
    print("=======")