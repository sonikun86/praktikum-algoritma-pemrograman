jmlpisanggoreng = int(input("banyaknya pisang goreng yang akan di hitung: \n"))
hargasatuan = int(input("harga perbiji: \n"))
print("daftar harga pisang goreng")

# Inisialisasi variabel i
i = 1
while i <= jmlpisanggoreng:
    print(f"{i} pisang goreng: \t rp {i * hargasatuan}")
    i += 1  # Menambah nilai i agar loop berhenti setelah jumlah pisang goreng yang diminta
