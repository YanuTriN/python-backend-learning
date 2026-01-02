users = [
    {"nama" : "Andi", "umur" : "14"},
    {"nama" : "Dewi", "umur" : "16"},
    {"nama" : "Bagus", "umur" : "33"},
]

with open("user.txt", "w") as file:
    for user in users:
        file.write(f"{user['nama']},{user['umur']}\n")