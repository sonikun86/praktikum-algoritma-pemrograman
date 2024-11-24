print("selamat datang di kalkulator deret pintar!\n\n")
jumlahbilangan = int(input("masukan banyaknya bilangan kemudian ENTER: \n"))
totalbilangan = 0
reratabilangan = 0
print("deretbilangan:", end='')

# Menggunakan while untuk menggantikan for
i = 1
while i <= jumlahbilangan:
    if i == jumlahbilangan:
        print(f"{i} \n", end='')
    else:
        print(f"{i} +", end='')
        totalbilangan += i
    i += 1  # Menambah nilai i agar perulangan berhenti saat mencapai jumlahbilangan

print(f"total seluruh bilangan jika di jumlahkan: {totalbilangan}")
reratabilangan = totalbilangan / jumlahbilangan
print(f"rata-ratanya adalah {reratabilangan}")
