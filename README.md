Nama : Garuga Dewangga Putra Handikto  
NPM  : 2406437615
Kelas: PBP F
Hobi : Nonton Film
Jurusan : Ilmu Sistem Informasi Komputer


Pertanyaan Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawaban:
1. Inisialisasi proyek & app:
   - `django-admin startproject goalhub .`
   - `python manage.py startapp main`
   - Tambah `'main'` di `INSTALLED_APPS`.
2. Buat model `Product` di `main/models.py` sesuai spesifikasi.
3. `python manage.py makemigrations && python manage.py migrate`.
4. Daftarkan `Product` ke admin (`main/admin.py`).
5. Buat view `show_main` di `main/views.py` untuk render template.
6. Buat `main/urls.py`, lalu include ke `goalhub/urls.py`.
7. Buat template `main/templates/main.html`.
8. Jalankan server `python manage.py runserver` dan tes.
9. Commit & push ke GitHub, lalu deploy ke PWS.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawaban: 
### Bagan Alur Request–Response (Model-View-Template)

```mermaid
flowchart TD
    A[Client Browser] -->|HTTP Request /| B[Django URLs Router]
    B --> C[project/goalhub/urls.py]
    C -->|include main.urls| D[main/urls.py]
    D -->|path show_main| E[main/views.py]
    E -->|Query data optional| F[(models.py)]
    F -->|Return data| E
    E -->|render context| G[main.html Template]
    G -->|Generated HTML| H[HTTP Response]
    H --> A

- **urls.py (project)**: pintu masuk request, delegasi ke url app.
- **urls.py (app)**: mapping path spesifik -> fungsi view.
- **views.py**: logika; menyiapkan `context`; (opsional) akses `models.py`.
- **models.py**: definisi struktur data/database.
- **template (html)**: tampilan akhir yang dikirim balik ke client.

3. Jelaskan peran settings.py dalam proyek Django!

Jawaban:
- Menyimpan konfigurasi global proyek: `INSTALLED_APPS`, database, `MIDDLEWARE`, `TEMPLATES`, `STATIC`, `ALLOWED_HOSTS`, dll. Semua komponen Django membaca pengaturan dari sini.

4. Bagaimana cara kerja migrasi database di Django?

Jawaban: 
1. Ubah/definisikan model di `models.py`.
2. `makemigrations` membuat berkas migrasi (rencana perubahan skema).
3. `migrate` mengeksekusi migrasi ke database (membuat tabel, alter kolom, dsb).
4. Django melacak migrasi yang sudah/ belum dijalankan agar konsisten di semua environment.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Jawaban:
Menurut saya, karena:
- **Batteries-included**: admin, ORM, auth, template, form, middleware – lengkap.
- **Opinionated & terstruktur**: MVT jelas; cocok mengajarkan arsitektur web yang rapi.
- **Produktif & aman**: banyak proteksi built-in (CSRF, XSS, SQL injection).
- **Dokumentasi kuat & komunitas besar**: mudah belajar dan mendapatkan bantuan.

5. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Jawaban:
- Penjelasan step Git & struktur Django sudah membantu.
- Mungkin bisa ditambah cheat-sheet perintah Git dan ringkasan “arah file mana yang diubah” per step dibuat lebih jelas lagi.

Terima Kasih!
