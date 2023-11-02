import tkinter as tk
import math

def hitung_bola():
    try:
        jari_jari = float(entry_jari_jari.get())

        # Menghitung volume bola
        volume = (4/3) * math.pi * jari_jari**3

        # Menghitung luas permukaan bola
        luas_permukaan = 4 * math.pi * jari_jari**2

        hasil_volume.config(text=f"Volume Bola: {volume:.2f}")
        hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")
    except ValueError:
        hasil_volume.config(text="Masukkan angka yang valid")
        hasil_luas_permukaan.config(text="Masukkan angka yang valid")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Bola")

# Label dan input untuk jari-jari
label_jari_jari = tk.Label(app, text="Jari-Jari Bola:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(app)
entry_jari_jari.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_bola)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()
