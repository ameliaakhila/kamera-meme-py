# 🤖 Detektor Pose Meme

Program Python untuk mendeteksi pose tangan tertentu dan (memohon) menggunakan webcam secara *real-time*, yang kemudian memicu pemutaran video meme beserta suaranya.

---

## 📋 Syaratnya
Sebelum memulai, pastikan komputer kamu sudah instal:
*   **Python** (Disarankan versi 3.10)
*   **Git** (Opsional)

---

## 🚀 Step-by-Step Instalasi & Jalanin Projectnya

### 1. Unduh / Clone Repo Project Ini
Buka terminal/Command Prompt, lalu arahkan ke folder project kamu:
```bash
cd path/ke/folder/project-meme
```

### 2. Buat dan Aktifkan Virtual Environment (Opsional)
```bash
python -m venv .venv
```
Aktifkan environment:
*   **Windows (CMD/PowerShell):**
    ```bash
    .venv\Scripts\activate
    ```

### 3. Install Semua Library Yang Aku Gunain
Caranya cuma jalanin satu perintah ini untuk menginstal seluruh kebutuhan dari file `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Siapkan Aset Media
Pastiin semua file-file ini berada di dalam **folder project** yang sama:
*   `cek-kamera.py` (Script program utama)
*   `meme.mp4` (Kamu bisa ubah pake video lain)
*   `meme_audio.mp3` (Kalo mau ada suaranya kamu harus kasih suara vidaonya juga)

### 5. Jalanin Programnya & Tips Penting
```bash
python cek-kamera.py
```
*   `PENTING:` Saat kamera menyala, mundur sedikit sampai bahu dan lengan kamu terlihat jelas di layar. Jika terlalu dekat, sensor tidak akan bekerja.
Rapatkan kedua telapak tangan di depan dada (pose memohon) dan TAHAN .
*   Kalo jarak tangan udah sesuai, **video meme bersuara akan langsung berputar**.
*   Tekan tombol **`q`** pada keyboard kalo mau keluar dari program.

## Worth a whirl, peeps :)