Nama : Garuga Dewangga Putra Handikto  
NPM  : 2406437615
Kelas: PBP F
Hobi : Nonton Film
Jurusan : Sistem Informasi 


---

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
![Django MVT Flow Diagram](https://github.com/user-attachments/assets/79ce0e7c-3bd2-4cfd-9e9a-f6e0d7282b64)

Referensi: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Introduction#what_does_django_code_look_like)%20-%20[Visual%20Django%20Flow%20Chart](https://www.geeksforgeeks.org/django-project-mvt-structure/

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


---

# 📌 Tugas 3 Implementasi Form dan Data Delivery pada Django

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan agar aplikasi bisa bertukar data antar sistem atau client-server.  
Contohnya: front-end atau aplikasi pihak ketiga perlu mengakses informasi produk dari server.  

Dengan adanya data delivery (dalam format **JSON/XML**):
- Data bisa diakses tanpa harus membuka template HTML.
- Aplikasi jadi fleksibel, scalable, dan mudah diintegrasikan dengan sistem lain.

---

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
### JSON lebih baik karena:
- Struktur lebih sederhana & mudah dibaca manusia.
- Ukuran file lebih kecil → hemat bandwidth.
- Lebih cepat diproses (langsung kompatibel dengan JavaScript).

### XML masih relevan karena:
- Mendukung metadata & schema (lebih formal).
- Banyak dipakai di sistem legacy.

👉 Karena efisiensi & integrasi lebih gampang, **JSON lebih populer** di era API modern.

---

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
- `is_valid()` memvalidasi data input form sesuai aturan model  
  (misalnya panjang field, tipe data, required atau tidak).  
- Kalau `is_valid()` **True** → data aman disimpan ke database.  
- Kalau tidak valid → Django otomatis memberi pesan error.  

🔑 Penting untuk mencegah data tidak sesuai/korup masuk ke database.

---

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- `csrf_token` adalah mekanisme keamanan Django untuk mencegah **CSRF (Cross-Site Request Forgery)**.  
- Tanpa `csrf_token`, form bisa dipalsukan oleh penyerang. Contoh: user sedang login di website kamu, lalu membuka situs jahat. Situs itu bisa mengirim form request ke server kamu seolah-olah dari user tersebut.  
- Akibatnya, data penting bisa dimodifikasi (misalnya pembelian barang, perubahan password) tanpa sepengetahuan user.  

👉 Dengan `csrf_token`, setiap form punya token unik yang harus cocok dengan token di server. Jika token tidak valid → request ditolak.  

---

## 5. Step-by-Step Implementasi
1. Buat model `Product` di `models.py` dengan field:
   - `name`, `price`, `description`, `thumbnail`, `category`, `is_featured`
2. Jalankan:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
3. Buat form di forms.py menggunakan ModelForm.
4. Tambahkan views untuk:
   - show_main → menampilkan produk
   - show_xml & show_json → data delivery
   - show_xml_by_id & show_json_by_id → data delivery by ID
   - add_product → form input
   - product_detail → halaman detail produk
5. Atur URL routing di:
   - urls.py aplikasi (main/urls.py)
   - urls.py proyek (project/urls.py)
6. Buat template HTML:
   main.html, add_product.html, product_detail.html
7. Test data delivery di Postman:
   /xml/, /json/, /xml/<id>/, /json/<id>/
8. Push ke GitHub & deploy ke PWS agar bisa diakses online.

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Mungkin untuk setiap tutorial bisa lebih diperjelas lagi dengan kata kata yang mudah dipahami.

## 7. Dokumentasi Hasil Screenshot Postman
Hasil uji coba endpoint dengan Postman bisa diakses melalui link berikut:
   Google Drive: https://drive.google.com/drive/folders/1bEZnIlkXYcNHrU48cJjMt51m2YhHo8Co?usp=share_link


---

## Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

### 1. Apa itu Django `AuthenticationForm`? Kelebihan dan Kekurangannya
`AuthenticationForm` adalah form bawaan Django yang digunakan untuk proses login pengguna. Form ini otomatis menyediakan field **username** dan **password**, serta melakukan validasi terhadap data yang dimasukkan, termasuk mengecek apakah user valid dan password sesuai.

**Kelebihan:**
- Sudah built-in di Django, jadi tidak perlu membuat form login manual.
- Aman karena otomatis memanfaatkan sistem autentikasi Django.
- Mudah digunakan dan diintegrasikan dengan view.

**Kekurangan:**
- Kurang fleksibel jika ingin menambahkan field tambahan (misalnya login pakai email, captcha, dsb).
- Tampilan default sederhana, perlu dikustomisasi agar sesuai desain aplikasi.

---

### 2. Perbedaan Autentikasi dan Otorisasi + Implementasi Django
- **Autentikasi (Authentication):** proses verifikasi identitas pengguna. Contoh: login dengan username dan password.
- **Otorisasi (Authorization):** proses pengecekan hak akses setelah pengguna berhasil login. Contoh: hanya admin yang bisa mengakses halaman dashboard admin.

**Implementasi di Django:**
- **Autentikasi** dilakukan dengan `authenticate()`, `login()`, dan `AuthenticationForm`.
- **Otorisasi** dilakukan dengan sistem `permissions` dan `decorator` seperti `@login_required`, `@permission_required`, serta atribut `is_staff`, `is_superuser` pada user.

---

### 3. Kelebihan dan Kekurangan Session & Cookies
**Session:**
- *Kelebihan:* Data tersimpan di server, lebih aman; hanya ID session yang dikirim ke browser.
- *Kekurangan:* Membebani server jika data yang disimpan sangat banyak.

**Cookies:**
- *Kelebihan:* Disimpan di sisi client, mengurangi beban server.
- *Kekurangan:* Bisa dimodifikasi oleh user; ukuran terbatas; potensi risiko keamanan jika tidak dienkripsi.

---

### 4. Apakah Cookies Aman Secara Default? Bagaimana Django Menanganinya
- **Cookies tidak sepenuhnya aman secara default** karena bisa diakses atau dimodifikasi user. Risiko yang perlu diwaspadai antara lain:
  - **Session hijacking** (cookie dicuri oleh orang lain).
  - **XSS (Cross-Site Scripting)** untuk mencuri cookie.
  - **CSRF (Cross-Site Request Forgery)** untuk memanfaatkan session aktif.

**Django menangani keamanan cookies dengan:**
- Menggunakan `HttpOnly` agar cookie tidak bisa diakses via JavaScript.
- Mendukung `Secure` flag agar cookie hanya dikirim lewat HTTPS.
- Menyediakan proteksi CSRF otomatis dengan `{% csrf_token %}`.
- Menggunakan signing dan hashing untuk data penting.

---

### 5. Step-by-Step Implementasi Checklist
1. **Setup autentikasi dasar**  
   - Import `AuthenticationForm`, `login`, `logout` di `views.py`.  
   - Membuat fungsi `login_user`, `logout_user`, dan `register`.

2. **Membuat halaman login & register**  
   - Membuat template `login.html` dan `register.html` yang extend `base.html`.  
   - Menambahkan form bawaan Django (`AuthenticationForm`, `UserCreationForm`).

3. **Mengatur URL routing**  
   - Menambahkan path untuk `login`, `logout`, dan `register` di `urls.py`.

4. **Menambahkan proteksi login**  
   - Menggunakan `@login_required` pada view tertentu (misalnya `show_main`, `add_product`, `product_detail`).

5. **Menyimpan informasi session**  
   - Menambahkan cookie `last_login` setelah user berhasil login.  
   - Menampilkan `last_login` di halaman utama.

6. **Logout dan hapus session**  
   - Menghapus session dan `last_login` cookie saat logout.

Dengan langkah-langkah ini, aplikasi mendukung autentikasi pengguna, menyimpan state dengan session dan cookies, serta aman sesuai best practice Django.

---
