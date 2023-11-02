import tkinter as tk
import math

def hitung_kerucut():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())

        # Menghitung volume kerucut
        volume = (1/3) * math.pi * jari_jari**2 * tinggi

        # Menghitung luas permukaan kerucut
        s = math.sqrt(jari_jari**2 + tinggi**2)
        luas_permukaan = math.pi * jari_jari * (jari_jari + s)

        hasil_volume.config(text=f"Volume Kerucut: {volume:.2f}")
        hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")
    except ValueError:
        hasil_volume.config(text="Masukkan angka yang valid")
        hasil_luas_permukaan.config(text="Masukkan angka yang valid")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Kerucut")

# Label dan input untuk jari-jari dan tinggi
label_jari_jari = tk.Label(app, text="Jari-Jari Kerucut:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(app)
entry_jari_jari.pack()

label_tinggi = tk.Label(app, text="Tinggi Kerucut:")
label_tinggi.pack()
entry_tinggi = tk.Entry(app)
entry_tinggi.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_kerucut)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()