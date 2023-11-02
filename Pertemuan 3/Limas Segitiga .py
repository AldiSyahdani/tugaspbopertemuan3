import tkinter as tk
import math

def hitung_limas_segitiga():
    try:
        alas = float(entry_alas.get())
        tinggi_alas = float(entry_tinggi_alas.get())
        tinggi_limas = float(entry_tinggi_limas.get())

        # Menghitung volume limas segitiga
        volume = (1/3) * (1/2 * alas * tinggi_alas) * tinggi_limas

        # Menghitung luas permukaan limas segitiga
        luas_permukaan = (1/2 * alas * tinggi_alas) + (3/2 * alas * tinggi_limas)

        hasil_volume.config(text=f"Volume Limas Segitiga: {volume:.2f}")
        hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")
    except ValueError:
        hasil_volume.config(text="Masukkan angka yang valid")
        hasil_luas_permukaan.config(text="Masukkan angka yang valid")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Limas Segitiga")

# Label dan input untuk alas, tinggi alas, dan tinggi limas
label_alas = tk.Label(app, text="Panjang Alas:")
label_alas.pack()
entry_alas = tk.Entry(app)
entry_alas.pack()

label_tinggi_alas = tk.Label(app, text="Tinggi Alas:")
label_tinggi_alas.pack()
entry_tinggi_alas = tk.Entry(app)
entry_tinggi_alas.pack()

label_tinggi_limas = tk.Label(app, text="Tinggi Limas:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(app)
entry_tinggi_limas.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_limas_segitiga)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()
