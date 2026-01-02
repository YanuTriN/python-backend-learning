user = {
    "nama" : "Hari",
    "umur" : "24",
    "dewasa" : True
}

print(user["nama"])
print(user["umur"])

user["pekerjaan"]= "Sales"

for key, value in user.items():
    print(key, ":", value)