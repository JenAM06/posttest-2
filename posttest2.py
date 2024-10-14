from prettytable import PrettyTable
# Data
data_admin = {
    'nama': 'jen',
    'pass': 'kece123'
    }

pelamar = {
    'jojo': {'password': 'jojo123'},
    'jeje': {'password': 'jeje123'},
}

tingkat_pendidikan = {
    'SMA': 1, 
    'S1': 2, 
    'S2': 3
}

#buat tabel
tabel = PrettyTable()
tabel.field_names = ["nomor", "Jobdesk", "Umur", "Pengalaman(tahun)", "Pendidikan"]

#fungsi menambahkan barang ke daftar
def tabel_loker(nomor, jobdesk, umur, pengalaman, pendidikan):
    tabel.add_row([nomor, jobdesk, umur, pengalaman, pendidikan])

#database job
tabel_loker("1","Programmer", 22, 2, 'S1')
tabel_loker("2", "Desainer Grafis", 20, 1, 'SMA')
tabel_loker("3", "Manajer Proyek",25, 5, 'S2')
tabel_loker("4", "Customer Service", 18, 0, 'SMA')

#Fungsi keluar
def keluar():
    print("===================")
    print("Keluar dari program")
    print("====Terima Kasih===")
    exit()

#Fungsi Read
def tampil_loker():
    print(tabel)

#Fungsi Create
def tambah_loker():
    while True:
        jobdesk = str(input("Masukkan jobdesk: "))
        umur = int(input("Masukkan umur mininum: "))
        pengalaman = int(input("Masukkan minimal tahun pengalaman kerja: "))
        pendidikan = input("Masukkan minimal pendidikan(SMA/S1/S2): ")
        tabel_loker(str(len(tabel.rows) + 1), jobdesk, umur, pengalaman, pendidikan)
        print("Loker berhasil ditambahkan!")
        tampil_loker()
        pilih = input("Apakah ingin menambah loker lagi? (y/n): ")
        if pilih == 'n':
            break

#Fungsi Update  
def ubah_loker():
    while True:
        tampil_loker()
        nomor = int(input("Masukkan Nomor Loker yang ingin dirubah: "))
        
        if 0 < nomor <= len(tabel.rows):
            print("Apa yang ingin diubah?")
            print("1. Jobdesk")
            print("2. Umur")
            print("3. Pengalaman")
            print("4. Pendidikan")
            pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

            #Nilai saat ini untuk setiap variabel
            loker_row = tabel.rows[nomor - 1]
            jobdesk = loker_row[1]
            umur = loker_row[2]
            pengalaman = loker_row[3]
            pendidikan = loker_row[4]

            if pilihan == 1:
                jobdesk = input("Masukkan jobdesk baru: ")
                tabel.rows[nomor - 1][1] = jobdesk
            elif pilihan == 2:
                umur = int(input("Masukkan umur minimum baru: "))
                tabel.rows[nomor - 1][2] = umur 
            elif pilihan == 3:
                pengalaman = int(input("Masukkan pengalaman(tahun) baru: "))
                tabel.rows[nomor - 1][3] = pengalaman 
            elif pilihan == 4:
                pendidikan = input("Masukkan minimal pendidikan baru (SMA/S1/S2): ")
                tabel.rows[nomor - 1][4] = pendidikan 
            else:
                print("Pilihan tidak valid.")
                continue
            tabel.rows[nomor - 1] = [nomor, jobdesk, umur, pengalaman, pendidikan]
            print("Loker berhasil dirubah!")
            tampil_loker()
            pilih = input("Apakah ingin merubah loker lagi? (y/n): ")
            if pilih == 'n':
                break 
        else:
            print("Nomor Loker tidak valid.")

#fungsi  Delete
def hapus_loker():
    while True:
        tampil_loker()
        nomor = input("Masukan nomor loker yang ingin dihapus : ")

        for row in tabel._rows:
            if row[0] == nomor:
                tabel.del_row(tabel.rows.index(row))
        print(f"Nomor loker {nomor} telah dihapus")
        tampil_loker()
        pilihan = input("Apakah Ingin menghapus loker lagi? (y/n): ")
        if pilihan == "n":
            break


#login admin
def login_admin():
    while True:
        username = input("\nMasukkan username admin anda: ").lower()
        password = input("Masukkan password anda: ")
        if username == data_admin['nama'] and password == data_admin['pass']:
            print("===================")
            print("Login berhasil!\nSelamat datang admin Jen!")
            print("===================")
            while True:
                print("\n====Menu Admin====")
                print("1. Tambah loker")
                print("2. Tampilkan loker")
                print("3. Ubah syarat loker")
                print("4. Hapus loker")
                print("5. Logout")
                pilih = int(input("Masukkan pilihan anda: "))
                if pilih == 1:
                    tambah_loker()
                elif pilih == 2:
                    tampil_loker()
                elif pilih == 3:
                    ubah_loker()
                elif pilih == 4:
                    hapus_loker()
                elif pilih == 5:
                    print("Logout berhasil")
                    menu_utama()
                    break
                else:
                    print("Pilihan tidak tersedia. Silahkan pilih lagi")
        else:
            print("username atau password salah")

#Memilih jobdesk
def daftar_job():
    tampil_loker()
    print("==================================")
    print("Masukkan data anda terlebih dahulu")
    print("==================================")
    umur = int(input("\nMasukkan umur anda: "))
    pengalaman = int(input("Masukkan pengalaman kerja Anda (tahun): "))
    pendidikan = input("Masukkan tingkat pendidikan Anda (SMA/S1/S2): ") 
    if len(tabel.rows) > 0:
        while True:
            nomor = int(input("Masukkan Nomor Loker yang ingin Anda lamar: "))
            if 0 < nomor <= len(tabel.rows):
                syarat = tabel.rows[nomor - 1] 
                if (umur >= syarat[2] and 
                    pengalaman >= syarat[3] and
                    tingkat_pendidikan[pendidikan] >= tingkat_pendidikan[syarat[4]]):
                    print(f"Selamat anda lulus seleksi, anda akan dihubungi untuk tes seleksi wawancara posisi '{syarat[1]}'!")
                    keluar()
                    break
                else:
                    print(f"Maaf, Anda tidak memenuhi syarat untuk posisi '{syarat[1]}'.")
                    pilih = input("Apakah ingin memilih loker lagi? (y/n): ")
                    if pilih == 'n':
                        break
            else:
                print("Nomor Loker tidak valid.")
    else:
        print("Tidak ada loker tersedia saat ini. Silahkan coba lagi tahun depan")
        keluar()

#Login pelamar
def login_pelamar():
    while True:
        username = str(input("Masukkan username anda: ")).lower()
        password = input("Masukkan password anda: ")
        if username in pelamar and pelamar[username]['password'] == password:
            print("\nLogin Berhasil!\nSelamat datang calon penopang perusahaan!")
            daftar_job()
            break
        else:
            print("Username atau password salah")


#Menu
def menu_utama():
    while True:
        print("===========================")
        print("Selamat Datang di PT. Misti")
        print("========Menu Utama=========")
        print("1. Login sebagai admin")
        print("2. Login sebagai pelamar")
        print("3. Keluar")
        pilih = input("Masukkan pilihan: ")

        if pilih == '1':
            login_admin()
        elif pilih == '2':
            login_pelamar()
        elif pilih == '3':
            keluar()
        else:
            print("\nPilihan tidak tersedia, kembali ke menu utama\n")

#Mulai program
if __name__== "__main__":
    menu_utama()