import json
import os
from datetime import datetime
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


# Yeni görev ekle
def gorev_ekle(gorevler):
    isim = input("Görev adı: ")
    tarih = input("Son tarih (GG/AA/YYYY): ")
    oncelik = input("Öncelik (yüksek/orta/düşük): ").lower()

    # Görev verilerini listeye ekleyelim
    gorevler.append({
        "isim": isim,
        "tamamlandi": False,
        "tarih": tarih,
        "oncelik": oncelik
    })

    print(Fore.GREEN + "✅ Görev eklendi.")


# Görevleri listele
def gorevleri_listele(gorevler):
    if not gorevler:
        print("📭 Hiç görev yok.")
        return

    print("\n📋 Görevler:")
    for i, gorev in enumerate(gorevler):
        durum = Fore.GREEN + "✅" if gorev["tamamlandi"] else Fore.RED + "❌"
        renk = {
            "yüksek": Fore.RED,
            "orta": Fore.YELLOW,
            "düşük": Fore.CYAN
        }.get(gorev["oncelik"], Fore.WHITE)

        print(f"{i + 1}. {renk}{gorev['isim']} [{gorev['oncelik']}] - {gorev['tarih']} {durum}")


# Görevi tamamla
def gorev_tamamla(gorevler):
    gorevleri_listele(gorevler)
    secim = int(input("Tamamlanan görev numarası: "))

    if 0 < secim <= len(gorevler):
        gorevler[secim - 1]["tamamlandi"] = True
        print(Fore.BLUE + "🎉 Görev tamamlandı!")


# Görev sil
def gorev_sil(gorevler):
    gorevleri_listele(gorevler)
    secim = int(input("Silinecek görev numarası: "))

    if 0 < secim <= len(gorevler):
        silinen = gorevler.pop(secim - 1)
        print(Fore.MAGENTA + f"🗑️ '{silinen['isim']}' silindi.")


# Görevleri filtrele
def gorev_filtrele(gorevler):
    print("\nFiltre seçenekleri:\n1. Öncelik\n2. Tarih\n3. Tamamlanma Durumu")
    secim = input("Filtre türü (1/2/3): ")

    if secim == "1":
        seviye = input("Öncelik (yüksek/orta/düşük): ").lower()
        filtreli = [g for g in gorevler if g["oncelik"] == seviye]
    elif secim == "2":
        tarih = input("Tarih (GG/AA/YYYY): ")
        filtreli = [g for g in gorevler if g["tarih"] == tarih]
    elif secim == "3":
        durum = input("Tamamlandı mı? (evet/hayır): ").lower()
        durum_bool = durum == "evet"
        filtreli = [g for g in gorevler if g["tamamlandi"] == durum_bool]
    else:
        print(Fore.RED + "❌ Geçersiz seçim.")
        return

    gorevleri_listele(filtreli)


# Ana program
def main():
    gorevler = gorevleri_yukle()

    while True:
        print(Fore.LIGHTWHITE_EX + "\n📌 Menü:")
        print("1. Görevleri Listele")
        print("2. Yeni Görev Ekle")
        print("3. Görevi Tamamla")
        print("4. Görev Sil")
        print("5. Görevleri Filtrele")
        print("6. Çıkış")

        secim = input("Seçim: ")

        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            gorev_ekle(gorevler)
        elif secim == "3":
            gorev_tamamla(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            gorev_filtrele(gorevler)
        elif secim == "6":
            gorevleri_kaydet(gorevler)
            print("💾 Görevler kaydedildi. Çıkılıyor...")
            break
        else:
            print(Fore.RED + "❌ Geçersiz seçim.")


if __name__ == "__main__":
    main()
