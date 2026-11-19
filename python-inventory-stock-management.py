print("=== Sistem Pengurangan Stok Barang ===")

barang = [
    {"kode": "A01", "nama": "Mouse", "harga": 75000, "stok": 10},
    {"kode": "A02", "nama": "Keyboard", "harga": 150000, "stok": 8},
    {"kode": "A03", "nama": "Monitor", "harga": 1200000, "stok": 5}
]


def cari(kode):
    i = 0

    while i < len(barang):
        if barang[i]["kode"] == kode:
            return i
        i += 1

    return -1


def tampilkan():
    i = 0

    while i < len(barang):
        print(
            barang[i]["kode"],
            barang[i]["nama"],
            barang[i]["harga"],
            barang[i]["stok"]
        )
        i += 1


def kurangi_stok(kode, jumlah):
    i = cari(kode)

    if i == -1:
        print("Kode barang tidak ditemukan.")
        return

    if jumlah <= 0:
        print("Jumlah pengurangan harus lebih dari 0.")
        return

    if barang[i]["stok"] < jumlah:
        print("Stok barang tidak mencukupi.")
        return

    barang[i]["stok"] -= jumlah
    print("Stok berhasil dikurangi.")
    print("Sisa stok:", barang[i]["stok"])


while True:
    print("\n=== MENU BARANG ===")
    print("1. Tampilkan Barang")
    print("2. Kurangi Stok")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan()

    elif pilih == "2":
        kode = input("Masukkan kode barang: ")
        jumlah = int(input("Masukkan jumlah pengurangan: "))
        kurangi_stok(kode, jumlah)

    elif pilih == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
