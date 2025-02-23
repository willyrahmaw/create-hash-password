# Password Encryption

## Deskripsi
Program ini digunakan untuk mengenkripsi dan mendekripsi password menggunakan metode encoding kustom berbasis daftar kata tertentu.

## Fitur
- Menggunakan daftar kata dasar untuk membentuk encoding unik.
- Mengenkripsi password dengan sistem pengkodean yang tidak umum.
- Dapat mendekripsi kembali password yang telah dienkripsi.

## Cara Penggunaan
1. Jalankan skrip Python:
   ```bash
   python script.py
   ```
2. Pilih opsi:
   - `1` untuk mengenkripsi password.
   - `2` untuk mendekripsi password.
3. Masukkan password atau teks terenkripsi.
4. Program akan menampilkan hasil enkripsi atau dekripsi.

## Persyaratan
- Python 3.x

## Catatan
- Encoding menggunakan daftar kata default `['willy', 'rahma', 'wijaya', 'rw', 'wr']`.
- Setiap karakter akan dipetakan ke kombinasi unik dari kata dasar dan angka.
- Jika karakter tidak dikenali dalam encoding, akan menggunakan placeholder `XXXXX`.
- Dekripsi hanya akan berhasil jika menggunakan encoding yang sama saat enkripsi.

## Contoh Penggunaan
### Enkripsi
**Input:**
```
willy
```
**Output:**
```
wijaya915wr wr131rahma willy430wr willy430wr wr938rahma
```

### Dekripsi
**Input:**
```
wijaya915wr wr131rahma willy430wr willy430wr wr938rahma
```
**Output:**
```
willy
```

