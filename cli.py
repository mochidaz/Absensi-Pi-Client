from database import Database


print("Selamat datang!")

db = Database()

while True:
    print("Apa yang ingin anda lakukan?")
    inp = int(input("""
1. Input data siswa
2. Delete data siswa
3. Lihat data siswa
4. Lihat data SEMUA siswa
5. Lihat data kehadiran
6. Exit

>> """))
    if inp == 1:
        nama = input("Masukkan nama: ")
        kelas = input("Masukkan kelas: ")
        umur = int(input("Masukkan umur: "))
        nis = input("Masukkan nis: ")
        foto = input("Masukkan lokasi foto: ")
        db.Insert((nama, kelas, umur, nis, foto))
        print(f"Siswa {nama} dengan NIS {nis} berhasil ditambahkan")
    elif inp == 2:
        nis = input("Masukkan NIS siswa yang akan dihapus: ")
        conf = input(f"Apa anda yakin akan menghapus siswa {db.Nama(nis)} dengan nis {nis}? (Y/n)")
        if conf.lower() == "y":
            db.Delete(nis)
            print(f"Siswa dengan NIS {nis} telah dihapus")
        else:
            print("Dibatalkan...")

    elif inp == 3:
        nis = input("Masukkan nis: ")
        print(db.getAll(nis))
    
    elif inp == 4:
        db.showAll()

    elif inp == 5:
        pass

    elif inp == 6:
        print("Selamat tinggal...")
        exit()

