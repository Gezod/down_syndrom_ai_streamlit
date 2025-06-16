import streamlit as st
import io
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ Konfigurasi awal
st.set_page_config(
    page_title="AI Prediksi Down Syndrome",
    layout="wide"
)

st.title("\U0001F4CA Prediksi Down Syndrome Menggunakan Neural Network")

@st.cache_data
def load_data():
    df = pd.read_csv("data/down_syndrom.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

if "ID" in df.columns:
    df = df.drop(columns=["ID"])

target = "down_syndrom"
if target not in df.columns:
    st.error(f"Kolom target '{target}' tidak ditemukan.")
    st.stop()

numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if target in numerical_cols:
    numerical_cols.remove(target)

features = df[numerical_cols].fillna(df[numerical_cols].mean())
target_data = df[target].fillna(df[target].mode()[0])

# Neural Network
X_train, X_test, y_train, y_test = train_test_split(features, target_data, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

nn_model = MLPClassifier(hidden_layer_sizes=(50, 25), max_iter=500, random_state=42)
nn_model.fit(X_train_scaled, y_train)

y_pred = nn_model.predict(X_test_scaled)
y_proba = nn_model.predict_proba(X_test_scaled)

# Evaluasi
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

st.subheader("🎯 Evaluasi Model Neural Network")
st.write(f"- Akurasi: {accuracy:.4f}")
st.write("Confusion Matrix:")
fig1, ax1 = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax1)
ax1.set_xlabel("Prediksi")
ax1.set_ylabel("Aktual")
st.pyplot(fig1)

st.subheader("📊 Classification Report")
report = classification_report(y_test, y_pred, output_dict=True)
st.dataframe(pd.DataFrame(report).transpose())

# Input manual
st.subheader("✍️ Prediksi Manual (Masukkan Data Baru)")

# Gunakan session_state untuk menyimpan hasil sebelumnya
if "riwayat_prediksi" not in st.session_state:
    st.session_state.riwayat_prediksi = []

manual_input = {}
for col in numerical_cols:
    manual_input[col] = st.number_input(
        f"Masukkan nilai {col}",
        min_value=float(features[col].min()),
        max_value=float(features[col].max()),
        value=float(features[col].mean())
    )

if st.button("🔮 Prediksi Sekarang"):
    input_df = pd.DataFrame([manual_input])
    input_scaled = scaler.transform(input_df)
    prediksi_nn = nn_model.predict(input_scaled)[0]
    proba_nn = nn_model.predict_proba(input_scaled)[0]
    status = "Mengidap Down Syndrome" if prediksi_nn == 1 else "Tidak Mengidap Down Syndrome"

    st.session_state.riwayat_prediksi.append({
        **manual_input,
        "Prediksi": status,
        "Probabilitas_Tidak (%)": round(proba_nn[0]*100, 2),
        "Probabilitas_Mengidap (%)": round(proba_nn[1]*100, 2)
    })

# Tampilkan hasil terakhir
if st.session_state.riwayat_prediksi:
    st.subheader("🧾 Riwayat Prediksi")
    st.dataframe(pd.DataFrame(st.session_state.riwayat_prediksi))

    # Jika prediksi terakhir mengidap, tampilkan saran
    if st.session_state.riwayat_prediksi[-1]["Prediksi"] == "Mengidap Down Syndrome":
        st.markdown("---")
        st.subheader("🩺 Saran Penanganan untuk Down Syndrome")
        st.markdown("""
**Jika seseorang didiagnosis atau diprediksi mengidap Down Syndrome, berikut adalah beberapa langkah dan solusi penanganan yang dapat dilakukan:**

1. **Diagnosis Lanjutan:**
   - Lakukan pemeriksaan medis lanjutan oleh tenaga medis profesional, termasuk tes genetik dan evaluasi perkembangan.

2. **Pendampingan Medis Berkala:**
   - Lakukan check-up rutin untuk memantau kesehatan jantung, pendengaran, penglihatan, dan sistem pencernaan.

3. **Terapi Dini (Early Intervention):**
   - Terapi fisik, okupasi, dan wicara sejak dini dapat membantu meningkatkan kemampuan motorik, sosial, dan komunikasi.

4. **Pendidikan Inklusif:**
   - Anak-anak dengan Down Syndrome sebaiknya mendapatkan pendidikan yang disesuaikan, baik di sekolah reguler dengan dukungan maupun sekolah khusus.

5. **Dukungan Keluarga dan Psikososial:**
   - Keluarga berperan penting dalam perkembangan anak. Bergabung dalam komunitas atau support group juga sangat disarankan.

6. **Gaya Hidup Sehat:**
   - Diet seimbang, aktivitas fisik ringan, dan rutinitas tidur yang baik sangat penting.

7. **Pantau Perkembangan dan Kemandirian:**
   - Latih keterampilan hidup mandiri dan dorong interaksi sosial secara positif.

> **Catatan:** Prediksi ini hanya alat bantu dan **bukan pengganti diagnosis medis**. Mohon konsultasikan hasil ini dengan dokter atau ahli genetika klinis.
        """)

# Download riwayat ke Excel
excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Data_Training")
    pd.DataFrame(st.session_state.riwayat_prediksi).to_excel(writer, index=False, sheet_name="Riwayat_Prediksi")

excel_buffer.seek(0)

st.download_button(
    label="⬇️ Download Riwayat Prediksi ke Excel",
    data=excel_buffer,
    file_name="riwayat_prediksi_down_syndrome.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
