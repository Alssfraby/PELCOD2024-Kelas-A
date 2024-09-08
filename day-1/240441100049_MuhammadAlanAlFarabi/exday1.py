#Biodata
nama="Muhammad Alan Al Farabi"
nim=240441100049
status="Mahasiswa"
ipk=4.00

print("Perkenalkan, Nama saya adalah", nama)
print("nim saya adalah ", nim)
print("saya adalah ", status)
print("impian saya adalah mendapat IPK", ipk)

#input string
nama_lengkap=str(input("nama saya adalah: "))

#input interger
nilai_mtk=int(input("nilai Matematika saya adalah: "))


#data
nilai_matematika=85
nilai_kimia=80
nilai_biologi=75
nilai_fisika=70

#penjumlahan dasar
a = nilai_matematika + nilai_biologi
b = nilai_biologi - nilai_fisika
c = nilai_fisika * nilai_kimia
d = nilai_matematika / nilai_fisika

print (f'Hasil penjumlahan dari matematika dan biologi adalah : {a} ') 
print (f'Hasil pengurangan dari biologi dan fisika adalah : {b} ') 
print (f'Hasil perkalian dari fisika dan kimia adalah : {c} ') 
print (f'Hasil pembagian dari matematika dan fisika adalah : {d} ') 

usia_masuk_kualiah = int(input("berapa usia anda saat masuk kuliah: "))
lama_kualiah = int(input("berapa lama  anda ingin kuliah (tahun): "))

usia_saat_ini = usia_masuk_kualiah + lama_kualiah
tahun_lulus = 2024 + lama_kualiah

print(f'saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'saya, {nama} akan lulus pada tahun {tahun_lulus}')
