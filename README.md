# 🧠 AI Prediksi Down Syndrome Menggunakan Neural Network

Aplikasi ini merupakan sistem berbasis **Streamlit** yang memanfaatkan model **Artificial Neural Network (ANN)** untuk memprediksi potensi seseorang mengidap **Down Syndrome** berdasarkan data medis numerik. Sistem ini dirancang sebagai alat bantu deteksi dini yang cepat, interaktif, dan dapat digunakan oleh tenaga kesehatan maupun masyarakat umum.

---

## 📌 Fitur Utama

- 🔍 **Prediksi Down Syndrome** berdasarkan input numerik.
- 📊 **Evaluasi model** mencakup akurasi, confusion matrix, dan classification report.
- 🧾 **Riwayat prediksi** ditampilkan dan dapat diunduh dalam format Excel.
- ✍️ **Input manual** untuk prediksi kasus baru.
- 🩺 **Saran penanganan** otomatis ditampilkan jika prediksi positif.
- ⚡ **Model ANN** dengan arsitektur `(50, 25)` dan maksimal 500 iterasi.

2. Siapkan lingkungan Python
Disarankan menggunakan virtual environment:

bash
Salin
Edit
python -m venv venv
source venv/bin/activate   # atau venv\Scripts\activate di Windows
3. Instal dependensi
bash
Salin
Edit
pip install -r requirements.txt
4. Jalankan aplikasi
bash
Salin
Edit
streamlit run app.py
📁 Struktur Folder
bash
Salin
Edit
.
├── data/
│   └── down_syndrom.csv       # Dataset input
├── app.py                     # File utama Streamlit
├── requirements.txt           # Dependensi Python
└── README.md
📈 Model Machine Learning
Model ANN dibangun menggunakan MLPClassifier dari sklearn dengan preprocessing StandardScaler. Dataset dibagi menjadi data latih dan uji, lalu model dilatih untuk klasifikasi biner (mengidap / tidak mengidap Down Syndrome).

📤 Output
Hasil evaluasi model ditampilkan langsung di aplikasi.

Data prediksi manual disimpan dalam bentuk tabel.

File .xlsx berisi dataset dan riwayat prediksi dapat diunduh.

⚠️ Catatan Penting
Aplikasi ini bukan alat diagnosis medis resmi, melainkan alat bantu prediksi berbasis data. Hasil prediksi harus dikonsultasikan kepada dokter atau ahli genetika klinis untuk tindakan lebih lanjut.

📚 Lisensi
MIT License

👤 Pengembang
Dikembangkan oleh [Kelompok 7], sebagai bagian dari proyek pembelajaran AI dan deteksi dini kesehatan masyarakat.
- Refangga Lintar Prayoga 1204220137
-
- 



---

Jika kamu butuh versi dalam Bahasa Indonesia penuh atau dalam format siap GitHub Pages (misalnya dengan badge atau GIF demo), saya bisa bantu juga!





---

## 🚀 Cara Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/username/down-syndrome-ann.git
cd down-syndrome-ann

