import os

# Bagian tambahan: Membuat requirements.txt kalau belum ada
if not os.path.exists('requirements.txt'):
    requirements = [
        "streamlit",
        "numpy",
        "pandas",
        "matplotlib"
    ]
    with open('requirements.txt', 'w') as f:
        for package in requirements:
            f.write(package + '\n')
    print("✅ File requirements.txt berhasil dibuat!")

# --- Mulai coding asli kamu ---
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menghitung persamaan regresi linier dan koefisien korelasi
def calculate_regression_equation(X, Y, var_name_x='x', var_name_y='y'):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    sum_x_squared = np.sum(X**2)
    sum_y_squared = np.sum(Y**2)

    # Menghitung koefisien regresi
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    # Menghitung koefisien korelasi
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

    equation = f'{var_name_y} = {a:.2f} + {b:.2f}{var_name_x}'
    regression_info = {'equation': equation, 'intercept': a, 'slope': b, 'r_value': r}
    return regression_info

# Halaman aplikasi Streamlit
def main():
    st.title('✨ Penentuan Konsentrasi Dari Persamaan Regresi Deret Standar ✨')
    st.write('Penentuan konsentrasi dari persamaan regresi deret standar yang dapat memudahkan analisis tanpa perlu menghitung secara manual. ENJOY FOR ACCESS 🧪👩‍🔬')
    st.markdown(" **SCROLL FOR MORE!!!")

    # CSS untuk gradasi warna pastel colorful dan animasi
    background_color_start = "#FFB6C1"  # Light Pink
    background_color_end = "#B0E0E6"    # Powder Blue
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, {background_color_start}, {background_color_end}) !important;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }}
        h1 {{
            text-align: center;
            color: #8B4513;
            animation: floating 3s ease-in-out infinite;
        }}
        @keyframes floating {{
            0% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0); }}
        }}
        </style>
    """, unsafe_allow_html=True)

    # Gambar
    img_url = "https://i.imgur.com/NuOnLxQ.jpeg"  # Link direct gambar
    st.markdown(f"""
        <style>
        .floating-image {{
            width: 60%;
            display: block;
            margin-left: auto;
            margin-right: auto;
            animation: float 4s ease-in-out infinite;
            border-radius: 20px;
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
        }}
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-15px); }}
            100% {{ transform: translateY(0px); }}
        }}
        </style>
        <img src="{img_url}" class="floating-image">
    """, unsafe_allow_html=True)

    # Perkenalan Kelompok
    st.header("👥 Kelompok 11 (E2-PMIP)")
    st.write("""
    1. Kayla Nurrahma Siswoyo (2420606)  
    2. Nahda Rensa Subari (2420632)  
    3. Rizka Rahmawati Shavendira (2420656)  
    4. Ummu Nabiilah (2420676)
    """)

    # Kalkulator Regresi
    st.header("📈 Kalkulator Regresi Linear")
    st.write("Masukkan data di bawah ini:")

    # Default data
    default_data = pd.DataFrame({
        'X': [0.0, 0.0, 0.0, 0.0],
        'Y': [0.0, 0.0, 0.0, 0.0]
    })

    # Input data tabel
    data_df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

    var_name_x = st.text_input('Nama variabel X:', 'x')
    var_name_y = st.text_input('Nama variabel Y:', 'y')

    if not data_df.empty and 'X' in data_df.columns and 'Y' in data_df.columns:
        try:
            X = data_df['X'].astype(float).to_numpy()
            Y = data_df['Y'].astype(float).to_numpy()

            # Menghitung persamaan regresi linier dan koefisien korelasi
            regression_info = calculate_regression_equation(X, Y, var_name_x, var_name_y)

            # Output Hasil Regresi
            st.markdown("## Hasil dari persamaan regresi yang dihitung adalah:")
            st.markdown(f"### 📌 {regression_info['equation']}")

            st.write(f"*Slope (b)*: {regression_info['slope']:.2f}")
            st.write(f"*Intercept (a)*: {regression_info['intercept']:.2f}")
            st.write(f"*Koefisien Korelasi (r)*: {regression_info['r_value']:.4f}")

            # Menampilkan grafik regresi
            fig, ax = plt.subplots()
            ax.scatter(X, Y, color='blue', label='Data')
            ax.plot(X, regression_info['intercept'] + regression_info['slope'] * X, color='red', label='Regresi')
            ax.set_xlabel(var_name_x)
            ax.set_ylabel(var_name_y)
            ax.set_title('Grafik Regresi Linear')
            ax.legend()
            st.pyplot(fig)

            # Input untuk menghitung X berdasarkan Y
            st.header("📊 Hitung Nilai X Berdasarkan Y")
            y_input = st.number_input(f'Masukkan nilai {var_name_y} yang ingin dihitung X-nya:', value=0.0)

            if y_input is not None:
                # Menghitung nilai X berdasarkan Y menggunakan persamaan regresi
                b = regression_info['slope']
                a = regression_info['intercept']
                if b != 0:
                    X_calculated = (y_input - a) / b
                    st.write(f"Nilai X untuk Y = {y_input} adalah: {X_calculated:.2f}")
                else:
                    st.write("Tidak dapat menghitung X karena slope (b) adalah 0.")

        except Exception as e:
            st.error(f"Terjadi kesalahan dalam memproses data: {e}")
    else:
        st.warning("Masukkan data yang valid untuk X dan Y dalam tabel di atas.")

if __name__ == '__main__':
    main()

