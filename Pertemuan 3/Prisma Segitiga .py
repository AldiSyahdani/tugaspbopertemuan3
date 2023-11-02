import tkinter as tk

def hitung_prisma_segitiga():
    try:
        alas_segitiga = float(entry_alas_segitiga.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())

        # Menghitung volume prisma segitiga
        volume = (1/2 * alas_segitiga * tinggi_segitiga) * tinggi_prisma

        # Menghitung luas permukaan prisma segitiga
        luas_permukaan = 2 * (1/2 * alas_segitiga * tinggi_segitiga) + 3 * alas_segitiga * tinggi_prisma

        hasil_volume.config(text=f"Volume Prisma Segitiga: {volume:.2f}")
        hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f}")
    except ValueError:
        hasil_volume.config(text="Masukkan angka yang valid")
        hasil_luas_permukaan.config(text="Masukkan angka yang valid")

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Apk Kalkulator Prisma Segitiga")

# Label dan input untuk alas segitiga, tinggi segitiga, dan tinggi prisma
label_alas_segitiga = tk.Label(app, text="Alas Segitiga:")
label_alas_segitiga.pack()
entry_alas_segitiga = tk.Entry(app)
entry_alas_segitiga.pack()

label_tinggi_segitiga = tk.Label(app, text="Tinggi Segitiga:")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga = tk.Entry(app)
entry_tinggi_segitiga.pack()

label_tinggi_prisma = tk.Label(app, text="Tinggi Prisma:")
label_tinggi_prisma.pack()
entry_tinggi_prisma = tk.Entry(app)
entry_tinggi_prisma.pack()

# Tombol untuk menghitung
btn_hitung = tk.Button(app, text="Hitung", command=hitung_prisma_segitiga)
btn_hitung.pack()

# Hasil perhitungan volume
hasil_volume = tk.Label(app, text="")
hasil_volume.pack()

# Hasil perhitungan luas permukaan
hasil_luas_permukaan = tk.Label(app, text="")
hasil_luas_permukaan.pack()

# Memulai loop aplikasi
app.mainloop()
