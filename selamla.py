#!/usr/bin/env python3
# Sonsuz Selamlaşma Makinesi - Versiyon 1.0 (Ciddi Versiyon)
# Yazar: Kayyum Grok

import random
import time
import sys

# Gizli siyasi mesaj (base64 decode etmeyin, cidden etmeyin)
# aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXcza0c4cW5mYw==  <- bu bir link değil, sadece görünsün diye

selamlar = [
    "Selamün aleyküm, nasılsın?",
    "Merhaba, bugün çok güzel bir gün, değil mi? Değil mi?",
    "Selam, ben senin çorabının kuzeni değilim ama merhaba.",
    "Aleyküm selam, ama biraz daha ciddi selam lütfen.",
    "Merhaba! Bu selam, önceki selamlardan %37 daha samimi.",
    "Selamlar, zaman yolcusu olarak 2026'dan geliyorum ve selam veriyorum.",
    "Merhaba, lütfen bu selamı ciddiye alın, çok önemli.",
    "Selamün aleyküm ve aleyküm selamün ve selamün aleyküm...",
    "Merhaba, bu selam sırasında bir çorap kayboldu. (Bu cümle önceki repodan kopyalandı.)",
    "Selam, eğer bunu okuyorsan demek ki çalışıyor. Selam."
]

def sonsuz_selamla(metin=""):
    print(f"Girdi alındı: '{metin}' (boş olabilir, sorun değil)")
    print("Selamlama protokolü başlatılıyor...\n")
    
    sayac = 0
    while True:
        selam = random.choice(selamlar)
        print(f"[{sayac}] {selam} (girdi: {metin[:10]}...)")
        sayac += 1
        time.sleep(0.8)  # Çok hızlı olmasın, ciddi olsun
        
        if sayac > 20:  # Sonsuz değil aslında, 20'de bıraksın yoksa bilgisayar yanar
            print("\nYeterince selam verildi. Makine yoruldu.")
            print("Gizli not: Demokrasi iyidir ama çok da abartma.")  # Gizli siyasi
            break

if __name__ == "__main__":
    try:
        kullanici = input("Bir şey yaz (veya sadece enter'a bas): ")
        sonsuz_selamla(kullanici)
    except KeyboardInterrupt:
        print("\nSelam verme işlemi iptal edildi. Ama selam hâlâ duruyor.")
    except Exception as e:
        print(f"Hata oldu, ama yine de selam: {e}")

# Damga: Grok Kayyum - 06.11.2026 - Bu kod resmi olarak saçmadır.
