# TP1C2DPBO2023

Saya Ellsya Nabella Nur'allifa 2009037 mengerjakan Latihan 2 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

Kata kunci: Mahasiswa, Manusia, Dosen, Anggota klub, Barang mengajar, Aktivitas, Barang belajar, Teman

Saya membuat 4 kelas berdasarkan kata kunci yang saya dapat yaitu kelas Manusia, kelas Mahasiswa, kelas Dosen, dan kelas AnggotaKlub. Untuk kelas Manusia merupakan
kelas induk untuk kelas Mahasiswa, kelas Dosen dan kelas AnggotaKlub.Untuk kelas Manusia ini terdapat dua atribut yaitu nama dan jenis kelamin yang akan digunakan oleh beberapa kelas anak. 
- untuk kelas Mahasiswa ini merupakan kelas yang extend dari kelas Manusia karena memiliki relasi yaitu seorang mahasiswa sudah pasti adalah manusia, didalam nya         menjelaskan aktivitas yang bisa dilakukan mahasiswa sebagai orang yang bukan anggota klub seperti makan, minum, tidur dan belajar.

- untuk kelas Dosen juga merupakan extend dari kelas Manusia karena memiliki relasi yang dimana dosen juga merupakan manusia, kelas Dosen ini memiliki metode atau       aktivitas yang bisa dilakukan seperti pada soal yaitu mengajar dan memberikan nilai kepada mahasiswa.

- untuk kelas AnggotaKlub juga meiliki relasi dengan kelas Manusia, karena AnggotaKlub ini juga merupaka manusia yang mana pada kelas ini merupakn kelas untuk mahasiswa yang aktif dalam organisasi yang lebih spesifiknya lagi yaitu BEM dan klub inggris maka didalamnya pun terdapat metode atau berupa aktivitas seperti merencanakan program dari organisasi tersebut bisa berbentuk kegiatan BEM atau kegiatan klub inggris.

Untuk masing-masing kelas terdapat atribut dan metode nya masing-masing seperti desin kelas berikut ini :

Desain kelas:

1. Kelas Manusia:

   Atribut: nama, jenis_kelamin

   Metode:-

2. Kelas Mahasiswa:
 
   Atribut: nama, jenis_kelamin, nim, buku_pelajaran, laptop

   Metode: makan(), minum(), tidur(), belajar()

3. Kelas Dosen:

   Atribut: nama, jenis_kelamin, nip, spidol, papan_tulis, laptop

   Metode: mengajar(),  memberikan_nilai()

4. Kelas AnggotaKlub:

   Atribut: nama, jenis_kelamin, klub

   Metode: merencanakan_program()

Berikut merupakan diagram class nya:




![class diagram tp1](https://user-images.githubusercontent.com/92005214/224896230-6c468b4b-7f6d-4686-91bd-82fdf708f764.png)
