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


# Tugas 5 Desain Web menggunakan HTML, CSS dan Framework CSS

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas CSS selector adalah:
1. **Inline style** (ditulis langsung pada elemen, misalnya `<p style="color:red">`) memiliki prioritas tertinggi.  
2. **ID selector** (`#id`) lebih tinggi dibanding class.  
3. **Class, attribute, dan pseudo-class selector** (`.class`, `[attr]`, `:hover`).  
4. **Element selector** (`div`, `p`, `h1`) memiliki prioritas paling rendah.  
Jika dua selector punya tingkat prioritas sama, maka yang **ditulis terakhir di CSS** yang akan dipakai (*last rule wins*).

---

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
- **Alasan penting**: Responsive design memastikan tampilan website tetap nyaman digunakan di berbagai perangkat (desktop, tablet, smartphone) tanpa harus membuat versi terpisah. Ini meningkatkan pengalaman pengguna (UX) dan mempermudah aksesibilitas.  

- **Contoh sudah menerapkan**:  
  - **Nike.com** atau **Shopee** → tampilan produk otomatis menyesuaikan layar, tombol navigasi berubah jadi hamburger menu di mobile.  
- **Contoh belum menerapkan**:  
  - Website lama yang hanya mendukung desktop → diakses lewat HP tampilannya mengecil, harus diperbesar secara manual, dan sulit digunakan.  

---

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- **Margin**: ruang di luar elemen, digunakan untuk memberi jarak antar elemen.  
  ```css
  .box { margin: 20px; }
* Border: garis di sekeliling elemen.
   .box { border: 2px solid black; }
* Padding: ruang di dalam elemen, antara konten dan border.
   .box { padding: 15px; }

## 4. Jelaskan konsep flexbox dan grid layout beserta kegunaannya!
* Flexbox: digunakan untuk mengatur layout satu dimensi (baris atau kolom). Cocok untuk navbar, daftar tombol, atau elemen yang perlu alignment fleksibel.

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

* Grid layout: digunakan untuk mengatur layout dua dimensi (baris dan kolom). Cocok untuk galeri, dashboard, atau daftar produk.

.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

Flexbox dipakai untuk layout sederhana, Grid untuk layout kompleks dengan baris dan kolom.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
a. Membuat fitur edit & delete produk
* Menambahkan fungsi edit_product dan delete_product di views.py.
* Menambahkan route di urls.py.
* Menampilkan tombol Edit & Delete hanya untuk produk milik user yang login.
b. Styling login & register
* Membuat form login dan register dengan tampilan card modern.
* Menggunakan Tailwind CSS untuk styling input, tombol, dan pesan error.
c. Styling add/edit & detail product
* Form tambah dan edit produk dibuat dengan desain konsisten.
* Detail produk menampilkan gambar, nama, harga, deskripsi, dan tombol aksi.
d. Styling daftar produk
* Jika produk kosong → tampilkan ilustrasi dan teks “Belum ada produk”.
* Jika ada produk → ditampilkan dengan card grid responsif (1 kolom di mobile, 2–4 kolom di desktop).
e. Responsive navbar
* Navbar desktop menampilkan logo dan menu horizontal.
* Navbar mobile menampilkan hamburger menu yang bisa diklik untuk membuka navigasi.

# Tugas 6: Javascript dan AJAX

## Pertanyaan dan Jawaban

### 1. Apa perbedaan antara synchronous request dan asynchronous request?

**Synchronous Request** adalah permintaan yang bersifat blocking, di mana browser akan menunggu hingga server memberikan respons sebelum melanjutkan eksekusi kode berikutnya. Selama proses ini, pengguna tidak dapat berinteraksi dengan halaman web karena halaman akan "freeze" atau tidak responsif.

**Asynchronous Request** adalah permintaan yang bersifat non-blocking, di mana browser tidak perlu menunggu respons dari server untuk melanjutkan eksekusi kode. Pengguna tetap dapat berinteraksi dengan halaman web sementara permintaan diproses di background. Ketika respons diterima, callback function atau promise akan dijalankan untuk menangani data tersebut.

**Perbedaan utama:**
- **Blocking vs Non-blocking**: Synchronous memblokir eksekusi kode, sedangkan asynchronous tidak
- **User Experience**: Synchronous dapat membuat halaman tidak responsif, asynchronous tetap responsif
- **Performance**: Asynchronous lebih efisien karena dapat menangani multiple request secara bersamaan
- **Kompleksitas**: Synchronous lebih mudah dipahami secara linear, asynchronous memerlukan pemahaman tentang callback, promises, atau async/await

### 2. Bagaimana AJAX bekerja di Django (alur request–response)?

AJAX (Asynchronous JavaScript and XML) di Django bekerja dengan alur sebagai berikut:

1. **Client-side (JavaScript)**:
   - User melakukan interaksi (click button, submit form, dll)
   - JavaScript menangkap event tersebut
   - JavaScript membuat XMLHttpRequest atau menggunakan Fetch API untuk mengirim request ke server
   - Request dikirim ke URL endpoint Django tertentu dengan method HTTP (GET, POST, PUT, DELETE)

2. **Server-side (Django)**:
   - Django routing (urls.py) menerima request dan mengarahkan ke view yang sesuai
   - View function/class memproses request (validasi data, operasi database, logika bisnis)
   - View mengembalikan response dalam format JSON (biasanya menggunakan `JsonResponse`)
   - Response dikirim kembali ke client

3. **Client-side (JavaScript) - Response Handling**:
   - JavaScript menerima response dari server
   - Data di-parse (jika JSON)
   - DOM dimanipulasi untuk menampilkan data/perubahan tanpa reload halaman
   - Update UI sesuai dengan data yang diterima (tampilkan toast, refresh list, close modal, dll)

**Contoh alur CRUD Product:**
User click "Tambah Product" → Modal form muncul → User isi form → Submit
→ JavaScript kirim POST request dengan data form → Django view proses data 
→ Simpan ke database → Return JsonResponse → JavaScript terima response 
→ Update tampilan product list → Tampilkan toast sukses

### 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

**Keuntungan AJAX:**

1. **User Experience Lebih Baik**:
   - Tidak perlu reload seluruh halaman
   - Interaksi lebih smooth dan responsif
   - Halaman tetap interaktif selama request diproses
   - Dapat menampilkan loading state untuk feedback visual

2. **Performance Lebih Efisien**:
   - Hanya data yang diperlukan yang ditransfer (JSON), bukan seluruh HTML
   - Mengurangi bandwidth usage
   - Server load lebih ringan karena tidak perlu render template HTML lengkap
   - Faster response time

3. **Fleksibilitas Tinggi**:
   - Dapat update bagian tertentu dari halaman secara independen
   - Mudah implementasi fitur real-time (dengan polling atau websocket)
   - Dapat menggabungkan data dari multiple endpoints
   - Better separation of concerns (backend fokus ke data, frontend fokus ke presentasi)

4. **Modern Web Development**:
   - Memungkinkan pembuatan Single Page Application (SPA)
   - Lebih mudah untuk membuat Progressive Web App (PWA)
   - Mendukung mobile-first development
   - Dapat di-cache untuk offline capability

**Kekurangan render biasa Django:**
- Setiap interaksi memerlukan full page reload
- Transfer data lebih besar (HTML lengkap)
- User experience kurang smooth
- Tidak cocok untuk aplikasi yang membutuhkan interaksi real-time

### 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

**Langkah-langkah keamanan yang harus diterapkan:**

1. **CSRF Protection**:
   - Gunakan CSRF token pada setiap AJAX request yang mengubah data (POST, PUT, DELETE)
   - Include CSRF token di header request: `'X-CSRFToken': csrftoken`
   - Django akan memvalidasi token untuk mencegah Cross-Site Request Forgery

2. **HTTPS/SSL**:
   - Gunakan HTTPS untuk enkripsi data saat transmisi
   - Mencegah man-in-the-middle attacks
   - Kredensial login tidak dikirim dalam plain text

3. **Input Validation dan Sanitization**:
   - Validasi semua input di server-side (tidak hanya client-side)
   - Gunakan Django Forms atau Serializers untuk validasi
   - Sanitize input untuk mencegah XSS (Cross-Site Scripting)
   - Gunakan Django's built-in escape functions

4. **Authentication & Authorization**:
   - Gunakan `@login_required` decorator untuk protected endpoints
   - Validasi user permissions sebelum mengizinkan operasi
   - Gunakan Django's authentication system yang sudah teruji
   - Implement proper session management

5. **Rate Limiting**:
   - Batasi jumlah request login/register dari satu IP
   - Mencegah brute force attacks
   - Gunakan packages seperti `django-ratelimit`

6. **Password Security**:
   - Gunakan Django's built-in password hashing (PBKDF2)
   - Enforce strong password policy
   - Tidak pernah store password dalam plain text
   - Implement password strength validator

7. **Error Handling**:
   - Jangan expose sensitive information di error messages
   - Generic error messages untuk login failures
   - Log security events untuk monitoring

8. **Content Security Policy (CSP)**:
   - Set proper CSP headers untuk mencegah XSS
   - Batasi sumber JavaScript yang dapat dieksekusi

**Contoh implementasi CSRF pada AJAX:**
```javascript
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

fetch(url, {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
})

### 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

**Dampak Positif AJAX terhadap UX:**

1. **Responsiveness**:
   - Halaman tetap responsif saat memproses request
   - User dapat melanjutkan interaksi dengan bagian lain dari halaman
   - Mengurangi frustasi dari waiting time
   - Memberikan feedback instan melalui loading indicators

2. **Seamless Interaction**:
   - Tidak ada "flash" atau "blank page" saat reload
   - Transisi antar state lebih smooth
   - Navigasi terasa lebih natural dan fluid
   - Pengalaman yang mirip dengan native application

3. **Faster Perceived Performance**:
   - Meskipun actual load time mungkin sama, perceived performance lebih cepat
   - User melihat perubahan incremental, bukan menunggu full page load
   - Dapat menampilkan skeleton loading untuk perceived speed
   - Progressive rendering membuat konten muncul lebih cepat

4. **Better Feedback**:
   - Dapat menampilkan toast notifications untuk setiap aksi
   - Loading states yang jelas (spinner, progress bar, skeleton)
   - Error handling yang lebih user-friendly
   - Success/failure feedback yang immediate

5. **Data Efficiency**:
   - Hemat bandwidth karena hanya transfer data yang diperlukan
   - Penting untuk mobile users dengan limited data
   - Faster loading terutama pada koneksi lambat
   - Dapat implement progressive loading

6. **Context Preservation**:
   - User tidak kehilangan context (scroll position, form state)
   - Tidak perlu re-navigate setelah action
   - Multi-step forms lebih smooth
   - Maintain application state lebih mudah

7. **Modern Features**:
   - Memungkinkan real-time updates (notifications, live search)
   - Infinite scrolling untuk better content discovery
   - Auto-save functionality
   - Collaborative features (multiple users)

**Potensi Dampak Negatif (jika tidak diimplementasi dengan baik):**

- **Kompleksitas**: User bisa bingung jika tidak ada feedback yang jelas
- **Accessibility**: Perlu extra effort untuk screen reader compatibility
- **Browser History**: Back button bisa tidak berfungsi seperti expected
- **SEO**: Content yang loaded via AJAX mungkin tidak ter-index dengan baik
- **Error Handling**: Error bisa kurang obvious tanpa visual feedback yang jelas

**Best Practices untuk UX:**

- Selalu tampilkan loading indicator saat request diproses
- Berikan feedback visual untuk setiap user action (toast, animation)
- Handle error dengan graceful degradation
- Implement proper empty states
- Maintain accessibility standards (ARIA labels, keyboard navigation)
- Consider offline functionality dengan service workers
- Test pada berbagai kondisi network (slow 3G, offline)