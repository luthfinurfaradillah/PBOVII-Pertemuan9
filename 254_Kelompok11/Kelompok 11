class Animal:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.jumlah_kaki = jumlah_kaki

    def biodata(self):
        return f"Nama: {self.nama}, Sifat: {self.sifat}, Ukuran: {self.ukuran}, Jumlah Kaki: {self.jumlah_kaki}"

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def biodata(self):
        return super().biodata() + f", Bisa Jalan: {self.bisa_jalan}, Jenis Mamalia: {self.jenis_mamalia}"

class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def biodata(self):
        return super().biodata() + f", Bisa Terbang: {self.bisa_terbang}, Jenis Aves: {self.jenis_aves}"

class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def biodata(self):
        return super().biodata() + f", Jenis Ayam: {self.jenis_ayam}, Bisa Diadu: {self.bisa_diadu}"
    
class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_merpati):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_merpati = jenis_merpati
    
    def biodata(self):
        return super().biodata() + f", Jenis Merpati: {self.jenis_merpati}"

singa = Mamalia("Singa", "Aggresif", "Besar", 4, True, "Berber")
kuda = Mamalia("Kuda", "Penurut", "Besar", 4, True, "Cleveland Bay")
gajah = Mamalia("Gajah", "Sensitif", "Sangat Besar", 4, True, "African Forest")
burung_merpati = Aves("Burung Merpati", "Setia", "Sedang", 2, True, "Zamrud Stephan")
burung_camar = Aves("Burung Camar", "Pemangsa", "Kecil", 2, True, "Andean")
ayam_hutan = Ayam("Unggas Ayam", "Waspada", "Sedang", 2, True, "Gallus", "Hutan hijau", True)
merpati = Merpati("Merpati", "Ramah", "Sedang", 2, True, "Goura", "Victoria")

print(singa.biodata())
print(kuda.biodata())
print(gajah.biodata())
print(burung_merpati.biodata())
print(burung_camar.biodata())
print(ayam_hutan.biodata())
print(merpati.biodata())
