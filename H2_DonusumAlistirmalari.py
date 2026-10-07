# Soru 1: 1101,011 (taban 2 -> taban 10)
tam = int('1101', 2)
kesir = 0*0.5 + 1*0.25 + 1*0.125
print("1. Doğrulama:", tam + kesir)  # 13.375

# Soru 2: 156 (taban 10 -> 2, 8, 16)
print("2. Doğrulama:", bin(156), oct(156), hex(156))  # 0b10011100, 0o234, 0x9c

# Soru 3: 0.3 (taban 10 -> taban 2, 6 basamak)
# 0.010011_2 değeri kontrolü
kesir_deger = 0/2 + 1/4 + 0/8 + 0/16 + 1/32 + 1/64
print("3. Doğrulama (ikili karşılık değeri):", kesir_deger)  # 0.296875 (0.3'e yaklaşım)

# Soru 4: 3C9,8 (taban 16 -> 2 ve 8)
tam_ikili = format(int('3C9', 16), 'b')
print("4. Doğrulama (İkili Tam):", tam_ikili)        # 1111001001 (kesir: ,1)
print("4. Doğrulama (Sekizli Tam):", oct(int('3C9', 16)))  # 0o1711 (kesir: ,4)

# Soru 5: 725 (taban 8 -> taban 16)
print("5. Doğrulama:", hex(int('725', 8)))  # 0x1d5

# Soru 6: 212 (taban 3 -> taban 5)
onluk_deger = int('212', 3)  # 23
# 23'ün 5 tabanındaki karşılığı
besli_rakamlar = []
n = onluk_deger
while n > 0:
    besli_rakamlar.append(str(n % 5))
    n //= 5
print("6. Doğrulama:", "".join(reversed(besli_rakamlar)))  # 43