print("Fitur Pengisian Rencana Studi") #print judul
nim = input("Masukkan NIM: ") #input nim
if nim [5:7] == "20": #jika index [5:7] adalah 20 maka termasuk mahasiswa tahun pertama  
    tahun = "tahun pertama"
    max_sks = 20 #jumlah maksimal sks mahasiswa tahun pertama
elif nim[5:7] == "19":#jika index [5:7] adalah 19 maka termasuk mahasiswa tahun kedua 
    tahun = "tahun kedua"
    max_sks = 22 #jumlah maksimal sks mahasiswa tahun kedua
elif nim [5:7] == "18":#jika index [5:7] adalah 18 maka termasuk mahasiswa tahun ketiga 
    tahun = "tahun ketiga"
    max_sks = 24#jumlah maksimal sks mahasiswa tahun ketiga
elif nim [5:7] == "17":#jika index [5:7] adalah 17 maka termasuk mahasiswa tahun keempat 
    tahun = "tahun keempat"
    max_sks = 26#jumlah maksimal sks mahasiswa tahun keempat
else: #jika nim tidak menampilkan tahun masuk mahasiswa berarti nim tidak valid
    print("nim tidak valid")

print("Anda mahasiswa " + tahun + ". Anda bisa mengambil paling banyak " + str(max_sks) + " SKS.") #print untuk mncetak hasil 

jumlah_sks = 0 # set jumlah sks = 0
while True: #memakai perulangan while
    print("Jumlah SKS yang diambil: ", jumlah_sks) #cetak jumlah sks yang diambil
    matkul = input("Masukkan nama mata kuliah yang diambil atau X untuk selesai: ") #mahasiswa dapat menginpt nama mata kuliah 
    if (matkul == "X"):#jika matkul sama dengan X
        print("Pengisian Rencana Studi selesai.") #Maka akan mencetak pengisisan encana studi selesai
        break #Untuk memberhentikan program
    else: #jika kondisi lain maka 
        sks = int (input("Masukkan beban SKS mata kuliah tersebut: ")) #input beban sks dengan menggunakan integer
        jumlah_sks = jumlah_sks + sks #jumlah sks ditambah dengan sks
        if (jumlah_sks == max_sks): # untuk mengecek jumlah sks< jika iya maka pengisian KRS selesai
            print("Pengisian Rencana Studi Selesai.") #untuk mencetak 
        elif (jumlah_sks > max_sks):#untuk mengecek apakah jumlah sks lebih besar dari max sks
            print("Jumlah SKS melebihi SKS maksimal. Pengisian Rencana Studi selesai.") #jika iya pengisian melebihi, maka program aka berhenti
            break #tidak diulang kembali
        else: # untuk akhiran semuanya berhasil mengambil matkul, nanti dipanggil matkul dan bobotnya juga dipanggil
            print("Berhasil mengambil mata kuliah", matkul, "dengan bobot", sks, "SKS. \n")
            


