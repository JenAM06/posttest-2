# Praktikum PosTest 2

# Profil Diri

Nama : Jen Agresia Misti

NIM : 2409116007
Kelas : A
Tema : Sistem loker PT. Misti

# Flowchart

![CRUD minpro 2-Page-1 drawio](https://github.com/user-attachments/assets/55e51984-60b8-4942-829b-f8dd0157e912)


# Menu Login

![Screenshot 2024-10-14 214704](https://github.com/user-attachments/assets/fff24cf9-5b4f-4828-94a6-e6923dc5d1c2)

Tampilan program yang dilihat user saat memilih role admin atau pelamar

# <sub>Penjelasan Menu mode Login</sub>

  1. Admin,
     bisa melakukan sistem CRUD(Create,Read,Update,Delete) pada database loker.
  2. Pelamar,
     hanya bisa memasukkan data umur, pengalaman bekerja, dan pendidikan, lalu memilih jobdesk yang diinginkan.
  3. Keluar,
     opsi untuk User yang ingin keluar dari program
     **Jika user memilih opsi 3:**
     
     ![Screenshot 2024-10-14 220502](https://github.com/user-attachments/assets/8eae37bf-e7fb-475f-b6d9-c1eab2a4d8a5)

      User akan otomatis keluar dari program

**Jika user menginputkan angka mode selain 1, 2, dan 3**

![Screenshot 2024-10-14 220946](https://github.com/user-attachments/assets/625487fe-27ef-40e1-abfc-d5a3783c8425)

jika user menginputkan angka selain 1, 2, dan 3, maka otomatis akan kembali ke Menu Mode Login

# <sub>Login Admin</sub>

User akan menginputkan username dan password yang sudah diatur untuk akun admin
* **tampilan program jika user memilih opsi 1 lalu menginputkan username dan password yang benar:** 

![Screenshot 2024-10-14 221402](https://github.com/user-attachments/assets/5b8a3cf9-d1c4-4e9e-b4df-cd8fb5f4b250)

User akan masuk pada fitur admin setelah login.

* **tampilan program jika user salah menginputkan username dan password yang benar:**

![Screenshot 2024-10-14 222012](https://github.com/user-attachments/assets/02d50f99-9292-4818-843c-c885e0d97a8e)

program akan terus mengulang sampai username dan password yang diinput benar.

# <sub>Login Pelamar</sub>
User akan menginputkan username dan password yang sudah diatur untuk akun pelamar

* **tampilan program jika user memilih opsi 2 lalu menginputkan username dan password:**

![Screenshot 2024-10-14 223941](https://github.com/user-attachments/assets/9ae7fe11-b2df-4a2d-bc42-25492212903e)

User akan masuk pada fitur pelamar setelah login.

* **tampilan program jika user salah menginputkan username dan password:**

![Screenshot 2024-10-14 224324](https://github.com/user-attachments/assets/ff33db2a-6178-4013-8f67-a58017d32ccf)

program akan terus mengulang sampai username dan password yang diinput benar.

# Mode Admin

![Screenshot 2024-10-14 224823](https://github.com/user-attachments/assets/c1a704a1-2167-4790-8603-70ab58e2bcfc)

pada mode admin, user akan diberikan 5 Fitur seperti gambar diatas dan user diminta untuk menginputkan fitur sesuai dengan angka fitur yang disediakan.

# <sub>Penjelasan Fitur Admin</sub>

1. Tambah loker

![Screenshot 2024-10-14 225148](https://github.com/user-attachments/assets/7cd3d82d-c343-4945-afab-62176bf83ae7)

untuk masuk ke fitur "Tambah loker" inputkan angka 1

![Screenshot 2024-10-14 225558](https://github.com/user-attachments/assets/46fa18d8-60f5-4248-b5c9-8373c59b67cc)

Admin akan menginputkan jobdesk, umur, pengalaman bekerja, dan pendidikan untuk ditambahkan ke tabel loker. setelah menambahakan admin akan ditanya kembali apakah ingin menambah loker lagi dengan sistem looping (y/n)

sebelum "Tambah loker":

![Screenshot 2024-10-14 225717](https://github.com/user-attachments/assets/c9a1618a-3fbb-4d07-a035-49aa4c8d1293)

* **Jika Admin menginputkan "y"**

![Screenshot 2024-10-14 230638](https://github.com/user-attachments/assets/5bcaab6b-abe9-45a4-9a0a-10f46f60df68)

 * **Jika Admin menginputkan "n"**

![Screenshot 2024-10-14 230858](https://github.com/user-attachments/assets/e5175c93-e3b6-4033-9ca6-3a201e21a57b)

jika admin input "n" maka admin akan kembali ke Fitur menu Admin.

2. Lihat loker

![Screenshot 2024-10-14 230858](https://github.com/user-attachments/assets/bc466559-a7ec-47d3-a55d-d93ba3dcb282)

Fitur untuk melihat daftar loker yang ada, baik setelah ditambahkan atau ada yang dihapus lokernya. disaat Barang sudah muncul dalam output otomatis akan looping kembali ke fitur.   

3. Ubah syarat loker(update)
   
![Screenshot 2024-10-14 234455](https://github.com/user-attachments/assets/a69a7fee-c62a-4dd5-966c-ccd3424a7554)

pilih nomor loker yang dirubah dan data yang ingin diganti

![Screenshot 2024-10-14 235025](https://github.com/user-attachments/assets/7fd4a731-98a7-45de-93d1-7da1c375abae)

Gambar diatas adalah loker yang sudah dirubah datanya.

* **Jika admin menginputkan data yang tidak valid**

![Screenshot 2024-10-14 235410](https://github.com/user-attachments/assets/de498fb4-a198-4685-bf69-c868e26f678d)

![Screenshot 2024-10-14 235436](https://github.com/user-attachments/assets/869ac6e8-3be6-42a9-92ac-c84a17a90b22)

jika admin menginputkan Nilai yang tidak Valid, program akan melakukan perulangan sampai admin menginputkan data yang benar.

4. Hapus loker (delete)

  ![Screenshot 2024-10-15 001705](https://github.com/user-attachments/assets/92885625-6cdd-43b2-a2a5-378544ec5c70)

  setelah menghapus nomor loker, kita bisa memilih kembali ingin menghapus lagi atau ke menu admin.

5. Log out (kembali ke menu utama)

   ![Screenshot 2024-10-15 002054](https://github.com/user-attachments/assets/600a0687-aff3-4103-afb1-69027551abe7)

# <sub> jika di menu fitur Admin input angka yang bukan dari range 1-5 </sub>

![Screenshot 2024-10-15 002505](https://github.com/user-attachments/assets/ca904718-cb2c-46c5-8f4c-02b833d17b51)

akan terus melakukan perulangan sampai user menginputkan opsi yang tersedia

# Menu Pelamar

![Screenshot 2024-10-15 002814](https://github.com/user-attachments/assets/7b42d169-15fa-462a-af9e-6ff04e8b50f2)

setelah login sebagai pelamar, user akan diminta untuk menginputkan data yang diperlukan lalu memilih jobdesk yang diinginkan. Jika memenuhi kualifikasi perusahaan, maka pelamar lulus tahap syarat wawancara.

* **Jika pelamar tidak lulus**

![Screenshot 2024-10-15 003637](https://github.com/user-attachments/assets/177b72ab-f822-48e9-bf7b-e28ff243ce8d)

jika pelamar tidak lulus di salah satu loker, pelamar akan di beri pilihan untuk memilih nomor loer lagi.

* **Memilih ulang nomor loker**

![Screenshot 2024-10-15 003905](https://github.com/user-attachments/assets/6f5393a5-6b51-43f0-bb0c-2cf826e01fd6)

* **Jika input nomor loker salah**

![Screenshot 2024-10-15 004117](https://github.com/user-attachments/assets/ca9304d7-09c0-4899-a0cb-06dbf2bbbdf7)

* **Jika tidak ada loker (tabel kosong)**
