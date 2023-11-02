import tkinter as tk

def hitung_kubus():
    sisi = float(entry_sisi.get())
    volume = sisi ** 3
    luas_permukaan = 6 * sisi ** 2
    hasil_volume.config(text=f"Volume Kubus: {volume:.2f}")
    hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Kubus")

# Label dan input untuk panjang sisi
label_sisi = tk.Label(app, text="Panjang Sisi Kubus:")
label_sisi.pack()
entry_sisi = tk.Entry(app)
entry_sisi.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_kubus)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()
