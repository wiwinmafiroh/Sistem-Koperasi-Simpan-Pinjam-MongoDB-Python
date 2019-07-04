import os
import pymongo
import msvcrt as m
import datetime
import itertools

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["koperasi"]
colnasabah = mydb["nasabah"]
colsimpanan = mydb["simpanan"]
colpinjaman = mydb["pinjaman"]

def wait():
    m.getch()
    
os.system('cls')

menu = True
while menu:
    print("""
Koperasi Simpan Pinjam
-----

    1. Tambah Nasabah
    2. Lihat Daftar Nasabah
    3. Rubah Data Nasabah
    4. Hapus Data Nasabah
    5. Buat Simpanan
    6. Buat Pinjaman
    7. Lihat Daftar Simpanan
    8. Lihat Daftar Pinjaman
    9. Pengambilan Simpanan
    10. Pengembalian Pinjaman
    """)
    menu = input("Pilih : ")

    if menu == "1":
        print("\nTambah Nasabah Baru\n")
        ktp = input("Nomor KTP: ")
        nama = input("Nama: ")
        gender = input("Jenis Kelamin: ")
        address = input("Alamat: ")
        data = {"ktp": ktp, "nama": nama, "gender": gender, "address": address}
        inputin = colnasabah.insert_one(data)
        if inputin is not None:
            print("\nBerhasil")
        else:
            print("\nGagal")
        wait()
        os.system('cls')
    elif menu == "2":
        print("\nDaftar Nasabah\n")
        nasabah = colnasabah.find({}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        for data in nasabah:
            print(data)
        wait()
        os.system('cls')
    elif menu == "3":
        print("\nRubah Data Nasabah\n")
        nasabah = colnasabah.find({}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        for data in nasabah:
            print(data)
        print("\n")
        ktp = input("Nomor KTP: ")
        datalama = colnasabah.find_one({"ktp": ktp}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        print(datalama,"\n")
        ktp = input("Nomor KTP: ")
        nama = input("Nama: ")
        gender = input("Jenis Kelamin: ")
        address = input("Alamat: ")
        databaru = {"$set": {"ktp": ktp, "nama": nama, "gender": gender, "address": address}}
        updetin = colnasabah.update_one(datalama, databaru);
        if updetin is not None:
            print("\nBerhasil")
        else:
            print("\nGagal")
        wait()
        os.system('cls')
    elif menu == "4":
        print("\nHapus Data Nasabah\n")
        nasabah = colnasabah.find({}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        for data in nasabah:
            print(data)
        print("\n")
        ktp = input("Nomor KTP: ")
        datanya = colnasabah.find_one({"ktp": ktp}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        print(datanya,"\n")
        yakin = input("Yakin ingin menghapus? [Y/N] ")
        if yakin == "Y":
            hapusin = colnasabah.delete_one(datanya);
            if hapusin is not None:
                print("\nBerhasil")
            else:
                print("\nGagal")
        else:
            print("\nGagal")
        wait()
        os.system('cls')
    elif menu == "5":
        print("\nBuat Simpanan\n")
        ktp = input("Nomor KTP: ")
        datanya = colnasabah.find_one({"ktp": ktp}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        if datanya is not None:
            print(datanya,"\n")
            jumlah = input("Jumlah Simpanan: ")
            data = {"ktp": ktp, "jml_simpanan": jumlah, "jml_pengambilan": "0", "tgl_simpan": datetime.datetime.now()}
            inputin = colsimpanan.insert_one(data)
            if inputin is not None:
                print("\nBerhasil")
            else:
                print("\nGagal")
            wait()
            os.system('cls')
        else:
            print("\nData tidak ditemukan")
            wait()
            os.system('cls')
    elif menu == "6":
        print("\nBuat Pinjaman\n")
        ktp = input("Nomor KTP: ")
        datanya = colnasabah.find_one({"ktp": ktp}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        if datanya is not None:
            print(datanya,"\n")
            jumlah = input("Jumlah Pinjaman: ")
            angsuran = input("Jumlah Angsuran: ")
            data = {"ktp": ktp, "jml_pinjaman": jumlah, "angsuran": "0", "tgl_pinjam": datetime.datetime.now()}
            inputin = colpinjaman.insert_one(data)
            if inputin is not None:
                print("\nBerhasil")
            else:
                print("\nGagal")
            wait()
            os.system('cls')
        else:
            print("\nData tidak ditemukan")
            wait()
            os.system('cls')
    elif menu == "7":
        sim = []
        kem = []
        print("\nDaftar Simpanan\n")
        ktp = input("Nomor KTP: ")
        simpanan = colsimpanan.find({"ktp": ktp}, {"_id": 0, "ktp": 1, "jml_simpanan": 1, "tgl_simpan": 1, "jml_pengambilan": 1})
        if simpanan is not None:
            for data in simpanan:
                print(data)
                kemb = data['jml_pengambilan']
                kem.append(kemb)
                simp = data['jml_simpanan']
                sim.append(simp)
            ke = list(map(int, kem))
            si = list(map(int, sim))
            print("\nTotal Simpanan : ")
            print(sum(si)-sum(ke))
            wait()
            os.system('cls')
        else:
            print("\nData tidak ditemukan")
            wait()
            os.system('cls')
    elif menu == "8":
        jml = []
        ang = []
        print("\nDaftar Pinjaman\n")
        ktp = input("Nomor KTP: ")
        pinjaman = colpinjaman.find({"ktp": ktp}, {"_id": 0, "ktp": 1, "jml_pinjaman": 1, "tgl_pinjam": 1, "angsuran": 1})
        if pinjaman is not None:
            for data in pinjaman:
                print(data)
                jmlh = data['jml_pinjaman']
                jml.append(jmlh)
                angs = data['angsuran']
                ang.append(angs)
            an = list(map(int, ang))
            jm = list(map(int, jml))
            print("\nTotal Pinjaman : ")
            print(sum(jm)-sum(an))
            wait()
            os.system('cls')
        else:
            print("\nData tidak ditemukan")
            wait()
            os.system('cls')
    elif menu == "9":
        print("\nPengambilan Simpanan\n")
        ktp = input("Nomor KTP: ")
        datanya = colnasabah.find_one({"ktp": ktp}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        if datanya is not None:
            print(datanya,"\n")
            ktp = input("Nomor KTP: ")
            jumlah = input("Jumlah Pengambilan: ")
            data = {"ktp": ktp, "jml_simpanan": "0", "jml_pengambilan": jumlah, "tgl_pengambilan": datetime.datetime.now()}
            inputin = colsimpanan.insert_one(data)
            if inputin is not None:
                print("\nBerhasil")
            else:
                print("\nGagal")
            wait()
            os.system('cls')
        else:
            print("\nData tidak ditemukan")
            wait()
            os.system('cls')
    elif menu == "10":
        print("\nPengembalian Pinjaman\n")
        ktp = input("Nomor KTP: ")
        datanya = colnasabah.find_one({"ktp": ktp}, {"_id": 0, "ktp": 1, "nama": 1, "gender": 1, "address": 1})
        if datanya is not None:
            print(datanya,"\n")
            ktp = input("Nomor KTP: ")
            jumlah = input("Jumlah Pengembalian: ")
            data = {"ktp": ktp, "jml_pinjaman": "0", "angsuran": jumlah, "tgl_pengembalian": datetime.datetime.now()}
            inputin = colpinjaman.insert_one(data)
            if inputin is not None:
                print("\nBerhasil")
            else:
                print("\nGagal")
            wait()
            os.system('cls')
        else:
            print("\nData tidak ditemukan")
            wait()
            os.system('cls')
    else:
        print("\nMenu tidak tersedia")
        wait()
        os.system('cls')
        menu = True
                
