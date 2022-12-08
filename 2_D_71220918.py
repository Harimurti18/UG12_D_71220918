print("~~~~ Tabel Matematika Nich ~~~~")
print("Pilihlah Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
n = int(input("Msukan model matematika yang diinginkan 1/2 : "))
if n == 1:
    a = int(input("Menampilkan tabel matematika dari angka: "))
    for i in range(1, 11):
        hasil = a * i
        print(a, "x", i, "=", hasil)
elif n == 2:
    a = int(input("Menampilkan tabel matematika dari angka: "))
    for i in range(50, 66):
        hasil = i / a
        print(i, ":", a, "=", hasil)
else:
    c = int(input("Menampilkan tabel matematika dengan angka:"))
    print("Pilihan tidak tersedia, jangan ngasal!")