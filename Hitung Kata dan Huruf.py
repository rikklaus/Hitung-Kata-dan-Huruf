print("Program Mencari Jumlah Huruf Dalam Kalimat")

kalimat = str(input('Masukkan kalimat: '))
kalimat_lower = kalimat.lower()
cari = str(input('Masukkan huruf yang ingin dicari: '))
cari_lower = cari.lower()
banyak_kata = len(kalimat_lower.split())
jumlah = kalimat_lower.count(cari_lower)
print(f"Jumlah kata pada kalimat adalah: {banyak_kata} kata dan jumlah huruf {cari} pada kalimat tersebut sebanyak: {jumlah}")