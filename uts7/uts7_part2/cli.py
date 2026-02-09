import sys
from utils import clear_screen, daftar_parkir

def jalankan_cli():
    while True:
        clear_screen()
        print("1. Kendaraan Masuk")
        print("2. Kendaraan Keluar")
        print("3. Lihat Parkir")
        print("4. Keluar")
        
        pilihan = input("Pilihan : ")

        if pilihan == '1':
            plat = input("Plat  : ")
            jenis = input("Jenis : ")
            merk  = input("Merk  : ")
            
            kendaraan = {"plat": plat, "jenis": jenis, "merk": merk}
            daftar_parkir.append(kendaraan)
            print(f"\nBerhasil menambahkan kendaraan.")

        elif pilihan == '2':
            if len(daftar_parkir) == 0:
                print("Parkiran Kosong")
            else:
                cari_plat = input("Plat Kendaraan : ")
                
                ketemu = False
                for i in range(len(daftar_parkir)):
                    if daftar_parkir[i]["plat"] == cari_plat:
                        kendaraan_keluar = daftar_parkir.pop(i)
                        print(f"{cari_plat} {jenis} {merk}")
                        ketemu = True
                        break
                
                if not ketemu:
                    print("Kendaraan tidak ditemukan")

        elif pilihan == '3':
            if len(daftar_parkir) == 0:
                print("Parkiran Kosong")
            else:
                print("Daftar Parkir")
                for i, k in enumerate(daftar_parkir, 1):
                    print(f"{i}. {k['plat']}")

        elif pilihan == '4':
            sys.exit()

        input("\nKlik Enter untuk melanjutkan...")