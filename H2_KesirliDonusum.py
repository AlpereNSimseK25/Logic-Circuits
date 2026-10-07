def kesirDonustur(kesir: float, hedefTaban: int, maxBasamak: int = 10) -> str:

    if not (0 <= kesir < 1):
        raise ValueError("Kesir değeri [0, 1) aralığında olmalıdır.")

    rakamlar = "0123456789ABCDEF" # 10'dan büyükler

    sonuc = []
    guncelKesir = kesir

    for _ in range(maxBasamak):
        if guncelKesir == 0:
            break

        carpim = guncelKesir * hedefTaban
        tamKisim = int(carpim)
        sonuc.append(rakamlar[tamKisim])

        guncelKesir = carpim - tamKisim  # Virgülden sonraki yeni kesirle devam edilir

        guncelKesir = round(guncelKesir, 10) # Python'ın kayan nokta hassasiyet hatalarını yuvarlamak için

    return "0." + "".join(sonuc) if sonuc else "0.0"

print("0.625 -> Taban 2 :", kesirDonustur(0.625, 2)) # 0.625 -> 0.101

print("0.75  -> Taban 16:", kesirDonustur(0.75, 16))# 0.75 -> Beklenen: 0.C

print("0.1   -> Taban 2 :", kesirDonustur(0.1, 2, maxBasamak=10)) # 0.1 -> beklenen: 0.0001100110...

print("0.3   -> Taban 2 (6 basamak):", kesirDonustur(0.3, 2, maxBasamak=6)) # 0.3 -> 6 basamak