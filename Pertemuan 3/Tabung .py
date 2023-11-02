import tkinter as tk
import math

def hitung_tabung():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())

        # Menghitung volume tabung
        volume = math.pi * jari_jari**2 * tinggi

        # Menghitung luas permukaan tabung
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

        hasil_volume.config(text=f"Volume Tabung: {volume:.2f}")
        hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")
    except ValueError:
        hasil_volume.config(text="Masukkan angka yang valid")
        hasil_luas_permukaan.config(text="Masukkan angka yang valid")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Tabung")

# Label dan input untuk jari-jari dan tinggi
label_jari_jari = tk.Label(app, text="Jari-Jari Tabung:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(app)
entry_jari_jari.pack()

label_tinggi = tk.Label(app, text="Tinggi Tabung:")
label_tinggi.pack()
entry_tinggi = tk.Entry(app)
entry_tinggi.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_tabung)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()