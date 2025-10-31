print("==================")
print("\tBiodata\tSiswa")
print("==================")
print("Nama     :\tGathan\nNIS      :\t123456789\nJURUSAN  :\tRPL\nUmur     :\t16\nhobi     :\tmain hp")
print ("=================")




data = None
print(data)
nama = "Gathan"
if nama is None:
    print("Nama belum diisi.")
else:
    print("Nama kamu adalah:",nama)


list_1= [2,4,8,16]
print(list_1[0])

list_2= ["grayson","jason","tim","damian"]
print(list_2[2])

list_3 = [24,False,"Hello Python"]
print(list_3[1])

buah = ["apel","jeruk"]
buah.append("mangga")
print(buah)

buah = ["apel,'jeruk"]
buah.extend(["mangga","pisang"])
print(buah)

angka = [1,2,3]
angka.insert(4,3)
print(angka)

buah = ["apel", "jeruk", "mangga","semangka","pepaya"]
buah.pop(4)  
print(buah)

angka = [5,2,9,1]
angka.sort()
print(angka)

buah = ["apel","jeruk","mangga"]
buah.remove("jeruk")
print(buah)

angka = [5,2,9,1]
angka.sort(reverse=True)
print(angka)

data = [1,2,3]
data.clear()
print(data)

nama = ["Gathan", "Aulia", "Ghofur"]
print(nama.index("Gathan"))

warna = ["merah", "kuning", "hijau"]
warna.reverse()
print(warna) 

angka = [1, 2, 2, 3, 2, 2, 2, 2, 2]
print(angka.count(2))


