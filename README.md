# 📦 Python Inventory Stock Management
### Sistem Pengurangan Stok Barang Berbasis Python

<p align="center">
  <b>Simple Inventory Management System Using Python</b>
</p>

---

## 📌 Deskripsi Proyek

**Python Inventory Stock Management** merupakan program sederhana berbasis Python yang dibuat untuk membantu mengelola dan mengontrol persediaan barang melalui sistem pengurangan stok.

Program ini memungkinkan pengguna untuk melihat daftar barang yang tersedia serta melakukan pengurangan stok berdasarkan kode barang dan jumlah yang diinginkan. Setiap proses pengurangan dilengkapi dengan validasi untuk memastikan kode barang ditemukan, jumlah pengurangan valid, dan stok mencukupi.

Proyek ini dikembangkan sebagai bentuk implementasi konsep dasar pemrograman Python, khususnya dalam pengolahan data menggunakan List dan Dictionary, penggunaan Function, perulangan, serta percabangan kondisi.

## ✨ Fitur Utama

Program ini memiliki beberapa fitur utama, yaitu:

- **📋 Menampilkan Data Barang**  
  Menampilkan seluruh daftar barang beserta kode, nama, harga, dan jumlah stok yang tersedia.

- **🔍 Pencarian Barang Berdasarkan Kode**  
  Mencari posisi data barang menggunakan kode unik yang telah ditentukan.

- **📉 Pengurangan Stok Barang**  
  Mengurangi jumlah stok barang berdasarkan kode barang dan jumlah pengurangan yang dimasukkan pengguna.

- **🛡️ Validasi Kode Barang**  
  Memastikan kode barang yang dimasukkan tersedia dalam daftar inventaris.

- **⚠️ Validasi Jumlah Pengurangan**  
  Mencegah pengurangan stok dengan jumlah nol atau nilai negatif.

- **📦 Validasi Ketersediaan Stok**  
  Memastikan jumlah barang yang akan dikurangi tidak melebihi stok yang tersedia.

- **🔄 Menu Interaktif**  
  Menyediakan menu berbasis terminal yang memungkinkan pengguna menjalankan program secara berulang hingga memilih keluar.

## 🛠️ Teknologi dan Konsep Pemrograman

Proyek ini menggunakan:

| Teknologi / Konsep | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| List | Menyimpan kumpulan data barang |
| Dictionary | Menyimpan atribut setiap barang |
| Function | Memisahkan program menjadi beberapa fungsi |
| While Loop | Melakukan pencarian dan perulangan menu |
| If-Else | Mengatur percabangan dan validasi kondisi |
| Return | Mengembalikan hasil pencarian |
| Operasi Aritmatika | Melakukan pengurangan jumlah stok |

## 📂 Struktur Data

Data barang disimpan menggunakan kombinasi List dan Dictionary.

Contoh data awal:

```python
barang = [
    {"kode": "A01", "nama": "Mouse", "harga": 75000, "stok": 10},
    {"kode": "A02", "nama": "Keyboard", "harga": 150000, "stok": 8},
    {"kode": "A03", "nama": "Monitor", "harga": 1200000, "stok": 5}
]
```

Setiap barang memiliki empat atribut utama:

- `kode` : Identitas unik barang.
- `nama` : Nama barang.
- `harga` : Harga satuan barang.
- `stok` : Jumlah persediaan barang.

## ⚙️ Fungsi Program

Program terdiri dari beberapa fungsi utama:

**1. `cari(kode)`**

Digunakan untuk mencari barang berdasarkan kode yang dimasukkan. Fungsi mengembalikan indeks barang apabila ditemukan dan `-1` apabila tidak ditemukan.

**2. `tampilkan()`**

Digunakan untuk menampilkan seluruh data barang yang tersimpan dalam List menggunakan perulangan While.

**3. `kurangi_stok(kode, jumlah)`**

Digunakan untuk memproses pengurangan stok barang. Fungsi ini melakukan beberapa pemeriksaan sebelum mengubah jumlah stok, yaitu:

- Memeriksa keberadaan kode barang.
- Memastikan jumlah pengurangan lebih dari nol.
- Memastikan stok mencukupi.
- Mengurangi stok apabila seluruh kondisi terpenuhi.

## 🚀 Cara Menjalankan Program

Pastikan Python sudah terinstal pada perangkat.

**1. Clone Repository**

```bash
git clone https://github.com/USERNAME/python-inventory-stock-management.git
```

**2. Masuk ke Folder Proyek**

```bash
cd python-inventory-stock-management
```

**3. Jalankan Program**

```bash
python main.py
```

*Catatan: Sesuaikan `main.py` dengan nama file Python yang digunakan.*

## 🖥️ Tampilan Menu Program

Ketika dijalankan, program akan menampilkan menu berikut:

```text
=== Sistem Pengurangan Stok Barang ===

=== MENU BARANG ===
1. Tampilkan Barang
2. Kurangi Stok
0. Keluar

Pilih menu:
```

Keterangan menu:

| Menu | Fungsi |
|---|---|
| 1 | Menampilkan seluruh data barang |
| 2 | Melakukan pengurangan stok barang |
| 0 | Mengakhiri program |

## 🧪 Contoh Validasi Program

Program memiliki beberapa kondisi untuk menjaga agar proses pengurangan stok berjalan dengan benar.

| Kondisi | Output |
|---|---|
| Kode barang tidak ditemukan | Kode barang tidak ditemukan. |
| Jumlah pengurangan 0 atau negatif | Jumlah pengurangan harus lebih dari 0. |
| Stok tidak mencukupi | Stok barang tidak mencukupi. |
| Semua kondisi terpenuhi | Stok berhasil dikurangi. |

## 🎯 Tujuan Pengembangan

Proyek ini dibuat untuk memahami dan menerapkan konsep dasar pemrograman Python dalam sebuah studi kasus pengelolaan inventaris barang.

Melalui proyek ini, diharapkan dapat meningkatkan pemahaman mengenai:

- Pengelolaan kumpulan data menggunakan List dan Dictionary.
- Penerapan Function untuk modularisasi program.
- Penggunaan While Loop dalam proses pencarian dan menu interaktif.
- Penerapan If-Else untuk validasi dan pengambilan keputusan.
- Pengolahan data serta manipulasi nilai dalam program.

## 👨‍💻 Identitas Pengembang

**Irga Mochamad Rafly**

- **NPM:** 267006111160
- **Kelas:** B
- **Program Studi:** Informatika
- **Fakultas:** Teknik
- **Universitas:** Universitas Siliwangi (UNSIL)

---

<p align="center">
  <b>Developed with Python 🐍</b><br>
  <i>Learning, Building, and Improving Through Code.</i>
</p>
