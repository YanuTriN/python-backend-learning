try:
    with open("data1.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan")