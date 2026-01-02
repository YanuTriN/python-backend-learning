anak = 1
remaja = 1
dewasa = 1

users = [
    {"nama" : "Andi", "umur" : "12"},
    {"nama" : "Dewi", "umur": "13"},
    {"nama" : "Bagus", "umur" : "33"}
]
def kategori_umur(umur):
    if umur < 13:
        return "Anak"
    elif umur <= 17:
        return "Remaja"
    else:
        return "Dewasa"
    
for user in users:
    if kategori_umur(int(user["umur"])) == "Anak":
        anak += 1
    elif kategori_umur(int(user["umur"])) == "Remaja":
        remaja += 1
    else:
        dewasa += 1

print ("Ringkasan :")
print ("Anak:" , anak)
print ("Remaja:" , remaja)
print ("Dewasa:" , dewasa)
