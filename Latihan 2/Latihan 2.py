namaFile = input("Masukkan nama file : ")

try:
    file = open (namaFile, "r") 
    file = open (namaFile, "a") 
    tambahan = input("Data yang mau ditambahkan: ")
    file.write(tambahan)
    tambah = input("Mau lagi (y/n): ")
    while tambah == 'y':
        tambahan = input("Data yang mau ditambahkan: ")
        file.write(tambahan)
        tambah = input('Mau lagi (y/n): ')
    file.close()
    
except FileNotFoundError:
	print("File tidak ditemukan")
