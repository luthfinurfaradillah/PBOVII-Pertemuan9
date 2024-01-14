import mysql.connector

# Koneksi ke MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Cek koneksi
if db.is_connected():

    print("Database berhasil connect")

# Membuat objek cursor
cursor = db.cursor()

# Buat database jika belum ada
cursor.execute("CREATE DATABASE IF NOT EXISTS database_motor")

# Pilih database yang akan digunakan
cursor.execute("USE database_motor")

# Buat tabel jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS motor (
        merk VARCHAR(255),
        model VARCHAR(255),
        tahun INT,
        daya_baterai FLOAT
    )
""")

# Commit perubahan
db.commit()

class Motor:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

class MotorLaki(Motor):
    def __init__(self, merk, model, tahun, daya_baterai):
        super().__init__(merk, model, tahun)
        self.daya_baterai = daya_baterai

def input_data(db):
    cursor = db.cursor()

    merk = input("Masukan Merk Motor     : ")
    model = input("Masukan Model Motor   : ")
    tahun = int(input("Masukan Tahun Produksi : "))
    daya_baterai = float(input("Masukan Daya Baterai (kWh) : "))

    motor = MotorLaki(merk, model, tahun, daya_baterai)

    sql = "INSERT INTO motor (merk, model, tahun, daya_baterai) VALUES (%s, %s, %s, %s)"
    val = (motor.merk, motor.model, motor.tahun, motor.daya_baterai)
    cursor.execute(sql, val)
    db.commit()

    print("{} data berhasil ditambahkan.".format(cursor.rowcount))

def tampilkan_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM motor"
    cursor.execute(sql)
    fetch = cursor.fetchall()

    print(">>> DATA MOTOR LISTRIK <<<")
    for data in fetch:
        print("=====================")
        print("Merk         :", data[0])
        print("Model        :", data[1])
        print("Tahun        :", data[2])
        print("Daya Baterai :", data[3])

def ubah_data(db):
    merk = input("Masukan Merk motor yang akan diubah :")

    cursor = db.cursor()
    sql_select = "SELECT * FROM motor WHERE merk=%s"
    val_select = (merk,)
    cursor.execute(sql_select, val_select)
    fetch = cursor.fetchone()

    if not fetch:
        print("Data dengan Merk {} tidak ditemukan.".format(merk))
        return

    print("Data yang akan diubah:")
    print("=====================")
    print("Merk         :", fetch[0])
    print("Model        :", fetch[1])
    print("Tahun        :", fetch[2])
    print("Daya Baterai :", fetch[3])

    print("\n=== Ubah Data ===")
    print("1. Ubah Model")
    print("2. Ubah Tahun Produksi")
    print("3. Ubah Daya Baterai")
    print("0. Kembali ke Menu Utama")

    submenu_choice = input("Masukan Pilihan submenu : ")

    if submenu_choice == '1':
        model_baru = input("Masukan Model Motor Terbaru :")
        update_attribute(db, merk, "model", model_baru)
    elif submenu_choice == '2':
        tahun_baru = int(input("Masukan Tahun Produksi Terbaru :"))
        update_attribute(db, merk, "tahun", tahun_baru)
    elif submenu_choice == '3':
        daya_baru = float(input("Masukan Daya Baterai Terbaru (kWh) :"))
        update_attribute(db, merk, "daya_baterai", daya_baru)
    elif submenu_choice == '0':
        print("Kembali ke Menu Utama.")
    else:
        print("Pilihan tidak valid.")

def hapus_data(db):
    merk = input("Masukan Merk motor yang datanya ingin dihapus :")

    cursor = db.cursor()
    sql = "DELETE FROM motor WHERE merk=%s"
    val = (merk,)
    cursor.execute(sql, val)
    db.commit()

    print("Data Motor Laki Berhasil Dihapus")

def update_attribute(db, merk, attribute, new_value):
    cursor = db.cursor()
    sql_update = "UPDATE motor SET {}=%s WHERE merk=%s".format(attribute)
    val_update = (new_value, merk)
    cursor.execute(sql_update, val_update)
    db.commit()

    print("Data berhasil diubah.")

def menu(db):
    print("=== Pilihan Menu ===")
    print("1. Tambah Data Motor ")
    print("2. Tampilkan Data Motor ")
    print("3. Ubah Data Motor ")
    print("4. Hapus Data Motor ")
    print("0. Exit ")

    Menu = int(input("Masukan Pilihan menu : "))
    if Menu == 1:
        print("=== Menu Tambah Data Motor ===")
        input_data(db)
    elif Menu == 2:
        print("=== Menu Tampil Data Motor ===")
        tampilkan_data(db)
    elif Menu == 3:
        print("=== Menu Ubah Data Motor ===")
        ubah_data(db)
    elif Menu == 4:
        print("=== Menu Hapus Data Motor ===")
        hapus_data(db)
    elif Menu == 0:
        print("Terima Kasih Atas Kunjungan Anda")
        exit()
    else:
        print("Pilihan tidak valid.")

if __name__ == '__main__':
    while True:
        menu(db)
