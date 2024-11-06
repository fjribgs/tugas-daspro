# Nama  : Fajri Bagaskara Budi
# Kelas : 1B
# NIM   : 2403807

# Aira diminta guru Olahraganya untuk menghitung waktu teman-temannya mulai berlari dan selesai berlari. 
# Ia juga diminta untuk menghitung selisih waktu yang dia buat dan menuliskan hasilnya ke dalam format 
# Jam - Menit - Detik. Bantulah Aira untuk menyelesaikan masalah tersebut agar dapat dilakukan dengan cepat.

def selisihWaktu(*waktu):
    selisihJam   = (jam_selesai - jam_mulai)

    if selisihJam < 0:
        print("Error")
        return
    selisihMenit = (menit_selesai - menit_mulai)

    if selisihMenit < 0:
        selisihMenitMinus = 60 + selisihMenit

    selisihDetik = (detik_selesai - detik_mulai)
    
    if selisihDetik < 0:
        
        selisihDetikMinus = 60 + selisihDetik

    if selisihMenit >= 0 and selisihDetik >= 0:
        print(f"{selisihJam} jam - {selisihMenit} menit - {selisihDetik} detik")
    else:
        print(f"{selisihJam} jam - {selisihMenitMinus} menit - {selisihDetikMinus} detik")


jam_mulai           = int((input("Masukkan jam mulai disini: ")))
menit_mulai         = int((input("Masukkan menit mulai disini: ")))
detik_mulai         = int((input("Masukkan detik mulai disini: ")))

jam_selesai         = int((input("Masukkan jam selesai disini: ")))
menit_selesai       = int((input("Masukkan menit selesai disini: ")))
detik_selesai       = int((input("Masukkan detik selesai disini: ")))

selisihWaktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)