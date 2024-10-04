# Proyek Analisis Data Bike-Sharing

Repositori ini berisi proyek analitik data yang saya kembangkan, dengan penerapan menggunakan Streamlit.

## Deskripsi

Projek ini akan menganalisis perkembangan kinerja perusahaan dalam beberapa tahun terakhir, mengidentifikasi puncak aktivitas penyewaan sepeda, serta membandingkan jumlah pengguna terdaftar dengan penyewa kasual. Temuan ini diharapkan memberikan gambaran perilaku konsumen dan kinerja perusahaan secara komprehensif.

## Struktur Direktori

.
├── Dashboard
│   ├── cleaned_day.csv
│   └── cleaned_hour.csv
│   └── dashboard.py
├── Data
│   ├── day.csv
|   └── hour.csv
├── preview
|   ├── capt 1.jpeg
|   ├── capt 1.jpeg
|   └── capt 1.jpeg
├── README.md
├── notebook.ipynb
└── requirements.txt

## Instalasi
## Setup Environment - Shell/Terminal
```bash
mkdir Submission
cd Submission
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit app
```bash
cd Dashboard
streamlit run dashboard.py
```

### 'notebook.ipynb'
1. Unduh proyek ini.
2. Buka IDE favorit Anda seperti Jupyter Notebook atau Google Colaboratory (di sini saya akan menggunakan Jupyter Notebook).
3. Buat Notebook Baru.
4. Unggah dan pilih file dengan ekstensi .ipynb.
5. Sambungkan ke runtime yang dihosting.
6. Terakhir, jalankan sel kode.

   
### 'dashboard/dashboard.py'
1. Unduh proyek ini.
2. Instal Streamlit di terminal atau command prompt menggunakan pip install streamlit jika Anda belum menginstalnya. Jika sudah, Anda bisa melanjutkan ke langkah berikutnya.
Instal pustaka yang diperlukan (Anda bisa melihat di requirements.txt, ada pustaka yang saya gunakan).
3. Harap dicatat, jangan pindahkan file CSV karena berfungsi sebagai sumber data. Simpan di dalam folder yang sama dengan dashboard.py.
4. Buka VSCode dan jalankan file tersebut dengan membuka terminal dan ketik streamlit run dashboard.py.
