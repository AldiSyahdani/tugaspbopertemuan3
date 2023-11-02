import tkinter as tk

def hitung_balok():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())
    
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    
    hasil_volume.config(text=f"Volume Balok: {volume:.2f}")
    hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Balok")

# Label dan input untuk panjang, lebar, dan tinggi
label_panjang = tk.Label(app, text="Panjang Balok:")
label_panjang.pack()
entry_panjang = tk.Entry(app)
entry_panjang.pack()

label_lebar = tk.Label(app, text="Lebar Balok:")
label_lebar.pack()
entry_lebar = tk.Entry(app)
entry_lebar.pack()

label_tinggi = tk.Label(app, text="Tinggi Balok:")
label_tinggi.pack()
entry_tinggi = tk.Entry(app)
entry_tinggi.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_balok)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()