def kategori_umur(umur):
    if umur <= 0:
        return "Umur tidak valid"
    elif umur < 13:
        return "Anak"
    elif umur <= 17:
        return "Remaja"
    else:
        return "Dewasa"
    
try:
    umur = int(input("Masukkan umur anda: "))
    print(kategori_umur(umur))
except ValueError:
    print("Input berupa angka")