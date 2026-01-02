try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print(hasil)
except ValueError:
    print("Harus berupa angka")
except ZeroDivisionError:
    print("Tidak boleh nol")