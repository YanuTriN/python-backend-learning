try:
    umur = int(input("Masukkan umur: "))
    print("Umur anda:", umur)

except ValueError:
    print("Input harus berupa angka")