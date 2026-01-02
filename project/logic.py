def kategori_umur(umur):
    if umur <= 0:
        return "Umut tidak valid"
    elif umur < 13:
        return "Anak"
    elif umur <=17:
        return "Remaja"
    else:
        return "Dewasa"