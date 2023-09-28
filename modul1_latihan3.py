#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Sistem Penilaian Akhir Mahasiswa


# In[ ]:


#Tambahkan fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir


# In[ ]:


#Tambahkan fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa):
    temp_data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts = nilai["uts"]
        uas = nilai["uas"]
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        temp_data_nilai_akhir[nama] = nilai_akhir
    return temp_data_nilai_akhir


# In[ ]:


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa: ")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama : {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


# In[ ]:


def main():
    data_mahasiswa = {
        #Data mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk dictionary)
        "Zidan": {"uts": 90, "uas": 85}, "Andaru": {"uts": 100, "uas": 90}, "Faiz": {"uts": 80, "uas": 75}
    }
    
    data_nilai_akhir = hitung_nilai_akhir_semua_mahasiswa(data_mahasiswa)
    
    tampilkan_nilai_akhir(data_nilai_akhir)
    
if __name__ == "__main__":
    main()

