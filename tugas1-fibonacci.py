# Nama  : Fajri Bagaskara Budi
# NIM   : 2403807
# Kelas : 1B

# Deret Fibonacci dengan menggunakan fungsi n

def fibonacci(n):
  if n <= 0:
    return [0]
  elif n == 1:
    return [1]
  else:
    list_angka = [1, 1]
    for i in range(n-2):
      angka_selanjutnya = list_angka[-1] + list_angka[-2]
      list_angka.append(angka_selanjutnya)
    return list_angka

n = int(input("Masukkan jumlah angka fibonacci disini: "))
angkafibonacci = fibonacci(n)
print("Fibonacci sequence:", angkafibonacci)