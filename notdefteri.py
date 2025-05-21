import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Notlar:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajanda")
        self.root.geometry("400x400")

        self.notlar = []

        # Başlık ve Not için giriş alanları
        self.title_label = tk.Label(self.root, text="Başlık:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self.root, width=30)
        self.title_entry.pack()

        self.not_label = tk.Label(self.root, text="Not:")
        self.not_label.pack()

        self.not_text = tk.Text(self.root, height=10, width=30)
        self.not_text.pack()

        # Not kaydetme butonu
        self.save_button = tk.Button(self.root, text="Notu Kaydet", command=self.save_note)
        self.save_button.pack()

        # Notları gösterme alanı
        self.not_listbox = tk.Listbox(self.root, height=10, width=50)
        self.not_listbox.pack()

    def save_note(self):
        title = self.title_entry.get()
        note = self.not_text.get("1.0", tk.END).strip()

        if title and note:
            # Tarih bilgisini al
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.notlar.append({"title": title, "note": note, "date": current_time})

            # Listbox'a yeni notu ekle
            self.not_listbox.insert(tk.END, f"{title} - {current_time}")

            # Giriş alanlarını temizle
            self.title_entry.delete(0, tk.END)
            self.not_text.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Eksik Veri", "Başlık ve Not kısmını doldurduğunuzdan emin olun.")

# Ana pencereyi oluştur
root = tk.Tk()
notlar_programi = Notlar(root)

root.mainloop()
