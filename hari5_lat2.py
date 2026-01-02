def kategori_umur(umur):
    if umur < 13:
        return "Anak"
    elif umur <=17:
        return "Remaja"
    else:
        return "Dewasa"
    
umur = int(input("Masukkan umur: "))
hasil = kategori_umur(umur)

print("Anda termasuk:", hasil)