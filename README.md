# Proyek Analisis Data Bike-Sharing

Repositori ini berisi proyek analitik data yang saya kembangkan, dengan penerapan menggunakan Streamlit.

## Deskripsi

Projek ini akan menganalisis perkembangan kinerja perusahaan dalam beberapa tahun terakhir, mengidentifikasi puncak aktivitas penyewaan sepeda, serta membandingkan jumlah pengguna terdaftar dengan penyewa kasual. Temuan ini diharapkan memberikan gambaran perilaku konsumen dan kinerja perusahaan secara komprehensif.

## Struktur Direktori

- `/data`: Folder ini berisi data yang digunakan dalam proyek, dalam format `.csv`.
- `/dashboard`: Folder ini menyimpan `main.py` yang digunakan untuk membangun dashboard hasil analisis.
- `notebook.ipynb`: File ini digunakan untuk melakukan analisis data secara mendetail.

## Instalasi

Pastikan Anda memiliki lingkungan Python yang sesuai beserta pustaka-pustaka yang dibutuhkan. Anda dapat menginstal pustaka-pustaka tersebut dengan menjalankan perintah berikut:

```bash
cd submission
pip install -r requirements.txt

cd dashboard
streamlit run dashboard.py
