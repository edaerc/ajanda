import tkinter as tk
from tkinter import messagebox

gorevler = []

def gorev_ekle():
    isim = entry_gorev.get()
    if isim:
        gorevler.append(isim)
        entry_gorev.delete(0, tk.END)
        liste_guncelle()
    else:
        messagebox.showwarning("Uyarı", "Görev ismi boş olamaz!")

def gorev_sil():
    secilen = listebox.curselection()
    if secilen:
        index = secilen[0]
        filtreli_gorevler = filtrele_gorevler(entry_ara.get())
        orijinal_index = gorevler.index(filtreli_gorevler[index])
        gorevler.pop(orijinal_index)
        liste_guncelle()
    else:
        messagebox.showinfo("Bilgi", "Lütfen silinecek bir görev seçin.")

def liste_guncelle():
    listebox.delete(0, tk.END)
    filtre = entry_ara.get().lower()
    filtreli = filtrele_gorevler(filtre)
    for i, gorev in enumerate(filtreli, start=1):
        listebox.insert(tk.END, f"{i}. {gorev}")

def filtrele_gorevler(aranan):
    return [g for g in gorevler if aranan.lower() in g.lower()]

def arama_guncelle(event):
    liste_guncelle()

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Görev Takip Uygulaması")
pencere.geometry("500x500")
pencere.configure(bg="#f0f0f0")  # Gri arka plan

# Başlık
etiket_baslik = tk.Label(pencere, text="📋 Görev Listesi", font=("Segoe UI", 16, "bold"), bg="#f0f0f0")
etiket_baslik.pack(pady=10)

# Görev ekleme girişi
entry_gorev = tk.Entry(pencere, font=("Segoe UI", 12), width=40)
entry_gorev.pack(pady=5)

# Buton çerçevesi
buton_cerceve = tk.Frame(pencere, bg="#f0f0f0")
buton_cerceve.pack(pady=10)

buton_ekle = tk.Button(
    buton_cerceve, text="➕ Görev Ekle", font=("Segoe UI", 11),
    bg="#d0e0f0", fg="black", relief="flat", width=15, command=gorev_ekle
)
buton_ekle.pack(side="left", padx=10)

buton_sil = tk.Button(
    buton_cerceve, text="🗑️ Görev Sil", font=("Segoe UI", 11),
    bg="#f0d0d0", fg="black", relief="flat", width=15, command=gorev_sil
)
buton_sil.pack(side="left", padx=10)

# 🔍 Arama kutusu
entry_ara = tk.Entry(pencere, font=("Segoe UI", 11), width=40)
entry_ara.pack(pady=5)
entry_ara.insert(0, "")  # Boş başlasın
entry_ara.bind("<KeyRelease>", arama_guncelle)  # Her tuşta filtrele

# Görev listesi
listebox = tk.Listbox(pencere, font=("Segoe UI", 12), width=50, height=12, bd=1, relief="solid")
listebox.pack(pady=10)

# Başlat
pencere.mainloop()
