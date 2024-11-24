# Fungsi untuk mengonversi nilai huruf ke angka
def nilai_ke_angka(nilai):
    if nilai == 'A':
        return 4
    elif nilai == 'B':
        return 3
    elif nilai == 'C':
        return 2
    elif nilai == 'D':
        return 1
    else:
        return 0  # Untuk nilai E atau yang tidak valid

# Program utama
def hitung_ips():
    # Input jumlah mata kuliah
    jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    
    total_nilai = 0  # Untuk menyimpan total bobot nilai
    total_sks = 0  # Untuk menyimpan total SKS

    # Perulangan untuk setiap mata kuliah
    for i in range(1, jumlah_mk + 1):
        print(f"\nMata Kuliah ke-{i}:")
        sks = int(input("Masukkan jumlah SKS: "))
        nilai = input("Masukkan nilai (A, B, C, D): ").upper()
        
        # Cek apakah nilai yang dimasukkan valid
        while nilai not in ['A', 'B', 'C', 'D']:
            print("Nilai tidak valid, masukkan A, B, C, atau D.")
            nilai = input("Masukkan nilai (A, B, C, D): ").upper()

        # Mengonversi nilai ke angka
        nilai_angka = nilai_ke_angka(nilai)

        # Menambahkan total bobot nilai dan total SKS
        total_nilai += nilai_angka * sks
        total_sks += sks

    # Menghitung IPS
    if total_sks == 0:
        print("Jumlah SKS tidak boleh 0.")
    else:
        ips = total_nilai / total_sks
        print(f"\nIndeks Prestasi Semester (IPS) Anda: {ips:.2f}")

# Menjalankan program
hitung_ips()
