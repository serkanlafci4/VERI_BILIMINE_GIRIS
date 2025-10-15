import random
from typing import List, Tuple

# 1) 1-100 arasında rastgele 10 tam sayı üretip diziye ekleme
def rastgele_sayilar_1_100(adet: int = 10) -> List[int]:
    return [random.randint(1, 100) for _ in range(adet)]

# 2) -100 ile +100 arasında 5’e tam bölünen sayıları yan yana gösterme (liste olarak döner)
def bese_bolunenler_minus100_100() -> List[int]:
    return [n for n in range(-100, 101) if n % 5 == 0]

# 3) Üç adet sayıyı karşılaştırıp sıralama
def uc_sayiyi_sirala(a: float, b: float, c: float, artan: bool = True) -> List[float]:
    return sorted([a, b, c], reverse=not artan)

# 4) Faktöriyel hesaplama ve açılımını yazdırma (0! = 1, negatifler için uyarı)
def faktoriyel_acilim(n: int) -> Tuple[int, str]:
    if n < 0:
        raise ValueError("Faktöriyel yalnızca negatif olmayan tam sayılar için tanımlıdır.")
    if n in (0, 1):
        return 1, f"{n}! = 1"
    carpim = 1
    terimler = []
    for k in range(n, 0, -1):
        carpim *= k
        terimler.append(str(k))
    acilim = f"{n}! = " + " * ".join(terimler) + f" = {carpim}"
    return carpim, acilim

# 5) Metindeki ilk kelime ile son kelimeyi bulma
def ilk_ve_son_kelime(metin: str) -> Tuple[str, str]:
    # Basit yaklaşım: boşluklara göre böl. (İşaretleme/yağlama varsa strip ile kırpılabilir.)
    kelimeler = metin.strip().split()
    if not kelimeler:
        return "", ""
    return kelimeler[0], kelimeler[-1]


# -------------------------
# Küçük bir demo / örnek kullanım
# -------------------------
if __name__ == "__main__":
    # 1) Rastgele sayılar
    sayilar = rastgele_sayilar_1_100(10)
    print("1) Rastgele 10 sayı (1-100):", sayilar)

    # 2) 5'e tam bölünenler
    bolunenler = bese_bolunenler_minus100_100()
    print("2) -100..100 arası 5'e bölünenler:")
    print(*bolunenler)  # yan yana yazdırma

    # 3) Üç sayıyı sıralama
    a, b, c = 12, -3, 7
    print("3) Üç sayıyı artan sırala:", uc_sayiyi_sirala(a, b, c, artan=True))
    print("   Üç sayıyı azalan sırala:", uc_sayiyi_sirala(a, b, c, artan=False))

    # 4) Faktöriyel ve açılım
    n = 5
    deger, acilim = faktoriyel_acilim(n)
    print("4)", acilim)

    # 5) İlk ve son kelime
    metin = "Python ile algoritma çalışmak çok faydalıdır."
    ilk, son = ilk_ve_son_kelime(metin)
    print(f"5) Metin: {metin}")
    print(f"   İlk kelime: {ilk} | Son kelime: {son}")
