def main():
    harga_produk = []  # List untuk menyimpan harga-harga produk
    
    print("Masukkan harga produk satu per satu. Ketik 'stop' untuk menghentikan input.")
    
    while True:
        try:
            harga_input = input("Masukkan harga produk: ")
            
            # Jika admin mengetik 'stop', keluar dari loop
            if harga_input.lower() == 'stop':
                break
            
            # Mencoba mengonversi input menjadi angka (float)
            harga = float(harga_input)
            
            # Menambahkan harga yang valid ke dalam daftar harga_produk
            harga_produk.append(harga)
        
        except ValueError:
            # Menangani kesalahan jika input bukan angka
            print("Input tidak valid. Harap masukkan harga dalam angka.")
    
    # Mengecek apakah ada harga yang valid dimasukkan
    if harga_produk:
        harga_tertinggi = max(harga_produk)
        harga_terendah = min(harga_produk)
        
        print(f"Harga produk tertinggi: {harga_tertinggi}")
        print(f"Harga produk terendah: {harga_terendah}")
    else:
        print("Tidak ada harga produk yang dimasukkan.")

# Menjalankan program
if __name__ == "__main__":
    main()
