import tkinter as tk
import math

def hitung_limas_segiempat():
    panjang_alas = float(entry_panjang_alas.get())
    lebar_alas = float(entry_lebar_alas.get())
    tinggi = float(entry_tinggi.get())
    luas_alas = panjang_alas * lebar_alas
    volume = (luas_alas * tinggi) / 3
    luas_permukaan = luas_alas + (panjang_alas * math.sqrt((lebar_alas/2)**2 + tinggi**2)) + (lebar_alas * math.sqrt((panjang_alas/2)**2 + tinggi**2))
    
    hasil_volume.config(text=f"Volume Limas Segiempat: {volume:.2f}")
    hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Limas Segiempat")

# Label dan input untuk panjang alas, lebar alas, dan tinggi
label_panjang_alas = tk.Label(app, text="Panjang Alas Limas:")
label_panjang_alas.pack()
entry_panjang_alas = tk.Entry(app)
entry_panjang_alas.pack()

label_lebar_alas = tk.Label(app, text="Lebar Alas Limas:")
label_lebar_alas.pack()
entry_lebar_alas = tk.Entry(app)
entry_lebar_alas.pack()

label_tinggi = tk.Label(app, text="Tinggi Limas:")
label_tinggi.pack()
entry_tinggi = tk.Entry(app)
entry_tinggi.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_limas_segiempat)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()
