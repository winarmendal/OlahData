# Impor modul yang dibutuhkan
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import statistics as st

# Membuat list kosong untuk menyimpan data
nama = [] # List untuk menyimpan nama siswa
nilai = [] # List untuk menyimpan nilai uas siswa

# Meminta input jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Membuat perulangan for untuk menginput data
for i in range(jumlah_siswa):
    # Meminta input nama siswa
    nama_siswa = input(f"Masukkan nama siswa ke-{i+1}: ")
    # Menambahkan nama siswa ke list nama
    nama.append(nama_siswa)
    # Meminta input nilai uas siswa
    nilai_uas = int(input(f"Masukkan nilai uas siswa ke-{i+1}: "))
    # Menambahkan nilai uas siswa ke list nilai
    nilai.append(nilai_uas)

# Menampilkan data yang telah diinput
print(f"Data {jumlah_siswa} siswa yang telah diinput:")
# Menggabungkan list nama dan list nilai menjadi satu list
data = list(zip(nama, nilai))
# Menampilkan data dengan fungsi tabulate, pilih format tabel dan header yang diinginkan
print(tabulate(data, headers=['Nama', 'Nilai'], tablefmt='simple'))

mean = np.mean(nilai) # Menghitung rata-rata nilai
median = np.median(nilai) # Menghitung nilai tengah
mode = st.mode(nilai) # Menghitung nilai yang paling sering muncul
std = np.std(nilai) # Menghitung simpangan baku
range = np.ptp(nilai) # Menghitung rentang nilai

print(f"Rata-rata nilai UAS siswa adalah {mean}")
print(f"Nilai tengah dari nilai UAS siswa adalah {median}")
print(f"Nilai yang paling sering muncul adalah {mode}")
print(f"Simpangan baku dari nilai UAS siswa adalah {std}")
print(f"Rentang dari nilai UAS siswa adalah {range}")

# Membuat grafik batang dari data
plt.bar(nama, nilai)

# Memberikan judul grafik
plt.title("Grafik Nilai UAS Siswa")

# Memberikan label sumbu x dan y
plt.xlabel("Nama Siswa")
plt.ylabel("Nilai UAS")

# Menampilkan grafik
plt.show()
