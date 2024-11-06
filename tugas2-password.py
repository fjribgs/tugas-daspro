# Nama  : Fajri Bagaskara Budi
# NIM   : 2403807
# Kelas : 1B

# Pak Dedi merupakan seorang Kepala Laboratorium Komputer di SMAN 2 Harapan. 
# Dia ingin membuat sebuah menu login yang dapat memberi kesempatan user untuk 
# memasukkan password kembali ketika dia salah sebanyak3 kali. Ketika user terus 
# memasukkan password yang salah, maka user tersebutakan keluar dari menu login tersebut. 
# Pak budi juga menambahkan bahwapassword ini harus sudah ada dalam sistem yang di buat, 
# sehingga sistem ituhanya mengecek password saja tanpa memperdulikan username.

for x in range(1, 4, 1):
    def akunValid(a, b, c):
        if percobaan == 0:
            print("Kesempatan log-in habis.")
            return True
        
        if password != "Latihan":
            print(f"Password salah! Sisa kesempatan anda {percobaan} kali lagi")
            return True
        
    username    = input("Masukkan username disini: ")
    password    = input("Masukkan password disini: ")
    percobaan   = 3 - x

    if password == "Latihan":
        print("Selamat Datang!")
        break
    
    akunValid(username, password, percobaan)