#01
#data integer
a=3
print(type(a))
#data float
a=3.5
print(type(a))
#data string
name="wiwut"
print(type(name))
#data list
angka=[1,2,3,4,5]
print(type(angka))

#02
belanjaan=["beras","minyak","telur"]
belanjaan.append("gula")
print("daftar belanjaan saya:")
print(belanjaan)

# 03
harga_belanjaan = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

print("harga belanjaan saya:")
print(harga_belanjaan)

total = sum(harga_belanjaan.values())
print("total belanjaan saya: Rp", total)

#04
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling
panjang=int(input("Masukkan panjang: "))
lebar=int(input("Masukkan lebar: "))

luas, keliling = hitung_persegi_panjang(panjang, lebar)

print("Luas persegi panjang:", luas)    
print("Keliling persegi panjang:"), keliling
      
#05
usia = int(input("Masukkan usia Anda: "))
if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")