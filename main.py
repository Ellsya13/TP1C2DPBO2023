#Saya Ellsya Nabella Nur'allifa 2009037 mengerjakan TP1 dalam mata kuliah
#Design Pemrograman Berorientasi Objek untuk keberkahan-Nya, maka saya tidak melakukan
#kecurangan seperti yang telah dispesifikasikan. Aamiin*/

# Membuat kelas manusia
class Manusia:

    # Untuk atribut
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    
    def __str__(self):
        return f"{self.nama} ({self.jenis_kelamin})"
    

# Membuat kelas mahasiswa
class Mahasiswa(Manusia):

    # Untuk atribut
    def __init__(self, nama, jenis_kelamin, nim, buku_pelajaran, laptop):
        super().__init__(nama, jenis_kelamin)
        self.nim = nim
        self.buku_pelajaran = buku_pelajaran
        self.laptop = laptop

    # Untuk metode
    def makan(self):
        print(f"{self.nama} sedang makan") # jika melakukan aktivitas makan
    
    def minum(self):
        print(f"{self.nama} sedang minum") # jika melakukan akivitas minum
    
    def tidur(self):
        print(f"{self.nama} sedang tidur") # jika melakukan aktivitas tidur

    def belajar(self):
        print(f"{self.nama} sedang belajar") # jika melakukan aktivitas belajar
    
    
    def __str__(self):
        return f"Mahasiswa: {super().__str__()} (NIM: {self.nim})"
    

# Membuat kelas dosen
class Dosen(Manusia):

    # Untuk atribut
    def __init__(self, nama, jenis_kelamin, nip, spidol, papan_tulis, laptop):
        super().__init__(nama, jenis_kelamin)
        self.nip = nip
        self.spidol = spidol
        self.papan_tulis = papan_tulis
        self.laptop = laptop
    
    # Untuk metode
    def mengajar(self):
        print(f"{self.nama} sedang mengajar") # jika sedang mengajar
    
    def memberikan_nilai(self, mahasiswa, nilai):
        print(f"{self.nama} memberikan nilai {nilai} kepada {mahasiswa.nama}") # jika sedang memberikan nilai
    
    def __str__(self):
        return f"Dosen: {super().__str__()} (NIP: {self.nip})"
    

# Membuat kelas anggota klub
class AnggotaKlub(Manusia):

    # Untuk atribut
    def __init__(self, nama, jenis_kelamin, klub):
        super().__init__(nama, jenis_kelamin)
        self.klub = klub
    
    # Untuk metode
    def merencanakan_program(self):
        print(f"{self.nama} sedang merencanakan program untuk {self.klub}") # jika merencanakan program
    
    def __str__(self):
        return f"Anggota Klub: {super().__str__()} ({self.klub})"


# Membuat objek-objek

# Keterangan setiap individu sesuai atribut yang ada di kelas AnggotaKlub
pahri = AnggotaKlub("Pahri", "Laki-laki", "BEM") 
angga = AnggotaKlub("Angga", "Laki-laki", "Klub Inggris") 
getsbi = AnggotaKlub("Getsbi", "Laki-laki", "Klub Inggris") 

# Keterangan setiap individu sesuai atribut yang ada di kelas Mahasiswa
mila = Mahasiswa("Mila", "Perempuan", "123456", ["Matematika", "Fisika", "Kimia"], "Asus") 
resyad = Mahasiswa("Resyad", "Laki-laki", "789012", ["Sejarah", "Ekonomi", "Sosiologi"], "Acerk") 

# Keterangan setiap individu sesuai atribut yang ada di kelas Dosen
bu_rose = Dosen("Ibu Rose", "Perempuan", "987654", "Hitam", ["Black Board", "White Board"], "Lenovo") 


# Memanggil metode
pahri.merencanakan_program()
angga.merencanakan_program()
getsbi.merencanakan_program()
mila.belajar()
resyad.tidur()
bu_rose.mengajar()



