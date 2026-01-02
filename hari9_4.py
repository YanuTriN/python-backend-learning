try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Salah input")
else:
    print("Input benar:", angka)
finally:
    print("Program selesai")