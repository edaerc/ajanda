import json
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from colorama import init, Fore

# Başlatma
init(autoreset=True)

GOREV_DOSYASI = "gorevler.json"


# Görevleri yükle
def gorevleri_yukle():
    if os.path.exists(GOREV_DOSYASI):
        with open(GOREV_DOSYASI, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# Görevleri kaydet
def gorevleri_kaydet(gorevler):
    with open(GOREV_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(gorevler, f, ensure_ascii=False, indent=4)


# Görevleri listele
def gorevleri_listele(gorevler):
    for widget in frame_gorevler.winfo_children():
        widget.destroy()

    if not gorevler:
        Label(frame_gorevler, text="📭 Hiç görev yok.", font=("Arial", 14), fg="red").pack()
        return

    for i, gorev in enumerate(gorevler):
        durum = "✅" if gorev["tamamlandi"] else "❌"
        renk = {
            "yüksek": "red",
            "orta": "yellow",
            "düşük": "cyan"
        }.get(gorev["oncelik"], "black")

        Label(frame_gorevler, text=f"{gorev['isim']} [{gorev['oncelik']}] - {gorev['tarih']} {durum}",
              font=("Arial", 12), fg=renk).pack()


# Yeni görev ekle
def gorev_ekle(gorevler):
    def ekle():
        isim = entry_isim.get()
        tarih = entry_tarih.get()
        oncelik = combo_oncelik.get().lower()

        if isim and tarih and oncelik:
            gorevler.append({
                "isim": isim,
                "tamamlandi": False,
                "tarih": tarih,
                "oncelik": oncelik
            })
            gorevleri_kaydet(gorevler)
            messagebox.showinfo("Başarılı", "✅ Görev eklendi.")
            gorevleri_listele(gorevler)
            yeni_gorev_penceresi.destroy()
        else:
            messagebox.showerror("Hata", "Tüm alanları doldurduğunuzdan emin olun.")

    yeni_gorev_penceresi = Toplevel(root)
    yeni_gorev_penceresi.title("Yeni Görev Ekle")

    Label(yeni_gorev_penceresi, text="Görev adı:").pack()
    entry_isim = Entry(yeni_gorev_penceresi, width=40)
    entry_isim.pack()

    Label(yeni_gorev_penceresi, text="Son tarih (GG/AA/YYYY):").pack()
    entry_tarih = Entry(yeni_gorev_penceresi, width=40)
    entry_tarih.pack()

    Label(yeni_gorev_penceresi, text="Öncelik (yüksek/orta/düşük):").pack()
    combo_oncelik = Combobox(yeni_gorev_penceresi, values=["yüksek", "orta", "düşük"])
    combo_oncelik.pack()

    Button(yeni_gorev_penceresi, text="Ekle", command=ekle).pack()


# Görev sil
def gorev_sil(gorevler):
    secim = int(entry_sil.get())

    if 0 < secim <= len(gorevler):
        silinen = gorevler.pop(secim - 1)
        gorevleri_kaydet(gorevler)
        messagebox.showinfo("Başarılı", f"🗑️ '{silinen['isim']}' silindi.")
        gorevleri_listele(gorevler)
    else:
        messagebox.showerror("Hata", "Geçersiz görev numarası.")


# Ana program
def main():
    global root, frame_gorevler, entry_sil
    gorevler = gorevleri_yukle()

    # Tkinter GUI başlatma
    root = Tk()
    root.title("To-Do List Uygulaması")
    root.geometry("400x600")

    # Görevler frame'i
    frame_gorevler = Frame(root)
    frame_gorevler.pack(pady=20)

    # Görev listeleme
    gorevleri_listele(gorevler)

    # Görev ekleme butonu
    Button(root, text="Yeni Görev Ekle", font=("Arial", 12), command=lambda: gorev_ekle(gorevler)).pack(pady=5)

    # Görev silme
    Label(root, text="Silmek için görev numarası girin:").pack()
    entry_sil = Entry(root, width=10)
    entry_sil.pack(pady=5)
    Button(root, text="Görev Sil", font=("Arial", 12), command=lambda: gorev_sil(gorevler)).pack(pady=5)

    # Çıkış butonu
    Button(root, text="Çıkış", font=("Arial", 12), command=root.quit).pack(pady=20)

    # Tkinter ana döngüsü
    root.mainloop()


if __name__ == "__main__":
    main()
