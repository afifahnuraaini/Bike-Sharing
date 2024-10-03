import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from scipy import stats

# Load data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Data preprocessing
hour_df.drop(['workingday'], axis=1, inplace=True)
day_df.drop(['workingday'], axis=1, inplace=True)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df.rename(columns={'yr': 'year', 'mnth': 'month', 'weekday': 'one_of_week',
                       'weathersit': 'weather_situation', 'windspeed': 'wind_speed',
                       'cnt': 'count_cr', 'hum': 'humidity'}, inplace=True)
hour_df.rename(columns={'yr': 'year', 'hr': 'hours', 'mnth': 'month', 'weekday': 'one_of_week',
                        'weathersit': 'weather_situation', 'windspeed': 'wind_speed',
                        'cnt': 'count_cr', 'hum': 'humidity'}, inplace=True)

# Function to categorize days
def get_category_days(one_of_week):
    return "weekend" if one_of_week in ["Saturday", "Sunday"] else "weekdays"

hour_df["category_days"] = hour_df["one_of_week"].apply(get_category_days)
day_df["category_days"] = day_df["one_of_week"].apply(get_category_days)

# Calculate average usage
workingday_data = day_df[day_df['category_days'] == 'weekdays']
weekend_data = day_df[day_df['category_days'] == 'weekend']
avg_workingday = workingday_data['count_cr'].mean()
avg_weekend = weekend_data['count_cr'].mean()

# Streamlit Dashboard
st.title("")

# Menghitung jumlah pelanggan per bulan
monthly_counts = day_df.groupby(day_df['dteday'].dt.to_period('M'))['count_cr'].sum().reset_index()
monthly_counts['dteday'] = monthly_counts['dteday'].dt.to_timestamp()

# Visualisasi jumlah pelanggan per bulan
st.subheader("Kinerja Perusahaan")
plt.figure(figsize=(23, 5))
plt.scatter(monthly_counts['dteday'], monthly_counts['count_cr'], c="#90CAF9", s=10, marker='o')
plt.plot(monthly_counts['dteday'], monthly_counts['count_cr'], color='b')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pelanggan')
plt.title('Grafik Jumlah Pelanggan per Bulan')
plt.xticks(rotation=45)  # Memutar label bulan agar lebih jelas
plt.grid(True)

# Menampilkan grafik di Streamlit
st.pyplot(plt)

st.write('Grafik menunjukkan fluktuasi jumlah pelanggan sepanjang tahun 2012 dengan tren kenaikan yang cukup konsisten hingga pertengahan tahun, diikuti oleh fluktuasi yang lebih tajam pada bulan-bulan selanjutnya. Dari awal tahun hingga pertengahan tahun, jumlah pelanggan meningkat signifikan dan mencapai puncaknya sekitar pertengahan tahun. Setelah itu, grafik memperlihatkan penurunan dengan berbagai fluktuasi hingga akhir tahun. Variasi jumlah pelanggan harian atau bulanan terlihat cukup jelas, menunjukkan adanya pengaruh musiman atau pola pembelian tertentu setiap bulan. Peningkatan tajam di pertengahan tahun mungkin terkait dengan momen atau acara tertentu yang mendongkrak aktivitas penjualan. Namun, menjelang akhir tahun, terjadi penurunan aktivitas pelanggan yang mungkin disebabkan oleh perubahan musiman, penurunan permintaan, atau faktor lain yang mempengaruhi perilaku pelanggan.')

# Hourly bike rental analysis
sum_order_items_df = hour_df.groupby("hours").count_cr.sum().reset_index()
st.subheader("Jumlah Penyewa Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x="hours", y="count_cr", data=sum_order_items_df, palette="Blues", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewa")
st.pyplot(fig)
st.write('Grafik menunjukkan pola penyewaan sepeda yang mencapai puncaknya pada sore hari, terutama pada pukul 16:00 dan 17:00, dengan puncak tertinggi terjadi pada pukul 17:00. Hal ini kemungkinan disebabkan oleh banyaknya pengguna yang memanfaatkan sepeda untuk perjalanan pulang kerja atau aktivitas sore lainnya. Sebaliknya, grafik juga memperlihatkan jam-jam dengan jumlah penyewaan sepeda paling sedikit, yaitu pada pukul 3:00 dan 4:00 dini hari. Rendahnya angka penyewaan pada waktu tersebut dapat dikaitkan dengan periode istirahat atau tidur, di mana aktivitas penyewaan sepeda sangat jarang. Secara keseluruhan, visualisasi ini menunjukkan bahwa penyewaan sepeda cenderung meningkat pada sore hari saat jam sibuk, dan menurun drastis pada dini hari ketika kebanyakan orang sedang beristirahat.')

# Pie chart for casual vs registered users
# Pie chart for casual vs registered users
total_casual = sum(day_df['casual'])
total_registered = sum(day_df['registered'])
data = [total_casual, total_registered]
labels = ['Casual', 'Registered']

# Membuat Pie Chart
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct='%1.1f%%', colors=["#D3D3D3", "#72BCD4"])
st.subheader("Distribusi Pengguna Sepeda")
st.pyplot(fig)

# Menulis deskripsi
st.write('Diagram lingkaran tersebut menunjukkan bahwa sebagian besar orang lebih memilih untuk mendaftar sebagai pengguna terdaftar dibandingkan dengan hanya melakukan penyewaan secara kasual. Pengguna terdaftar menyumbang 81,2% dari total, mengindikasikan bahwa mayoritas orang lebih memilih manfaat atau fitur yang didapat dengan menjadi pengguna terdaftar. Sementara itu, pengguna kasual hanya mewakili 18,8% dari total, menunjukkan bahwa sedikit orang yang memilih untuk menyewa tanpa mendaftar. Secara keseluruhan, visualisasi ini menunjukkan kecenderungan yang kuat untuk mendaftar, kemungkinan karena adanya keuntungan atau insentif tertentu yang diperoleh melalui pendaftaran.')

st.subheader("Kesimpulan")

st.write('Secara keseluruhan, kinerja perusahaan menunjukkan fluktuasi jumlah pelanggan dengan tren peningkatan pada awal hingga pertengahan tahun dan penurunan menjelang akhir tahun. Puncak penyewaan sepeda terjadi pada pukul 17:00, yang kemungkinan besar terkait dengan waktu pulang kerja, sementara penggunaan paling sedikit terjadi pada dini hari. Selain itu, mayoritas pengguna (81,2%) lebih memilih mendaftar sebagai pengguna terdaftar dibandingkan menyewa secara kasual, kemungkinan karena adanya manfaat atau fitur tambahan yang ditawarkan.')
