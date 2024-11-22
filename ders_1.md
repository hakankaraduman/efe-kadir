
# **Python ile Eğlenceli Kodlama!**  
Merhaba! Bu rehberle Python öğrenmeye hazır mısın? Python, bilgisayarlara "ne yapacağını" söyleyebildiğin bir programlama dilidir. Bu rehberde her şeyi adım adım öğreneceksin ve sonunda kendi projeni yapabileceksin!

---

## **1. Python’a Giriş**

### **Merhaba Dünya!**
Kod yazmaya başlamadan önce, Python’un nasıl çalıştığını görmek için ilk kodumuzu yazacağız.

#### **Ne yapacağız?**  
Bilgisayara “Merhaba Dünya!” yazmasını söyleyeceğiz.

#### **Kod:**
```python
print("Merhaba Dünya!")
```

#### **Deneme Zamanı:**  
Şimdi kendi mesajını yazdırmayı dene:  
```python
print("Merhaba, benim adım [buraya adını yaz]!")
```

**Sonuç ne oldu? Tebrikler, ilk kodunu yazdın! 🎉**

---

## **2. Veri Tipleri ve Değişkenler**

### **Veri Tipleri Nedir?**
Bilgisayar, bilgileri farklı şekillerde saklar. İşte en yaygın veri tipleri:  
1. **Yazılar (String):** Harfler, kelimeler ve cümleler.  
   Örnek:  
   ```python
   isim = "Ahmet"
   print(isim)
   ```

2. **Tam Sayılar (Integer):** Sayılar.  
   Örnek:  
   ```python
   yas = 12
   print(yas)
   ```

3. **Ondalık Sayılar (Float):** Kesirli sayılar.  
   Örnek:  
   ```python
   pi = 3.14
   print(pi)
   ```

4. **Doğru/Yanlış (Boolean):** Bir şey doğru mu, yanlış mı?  
   Örnek:  
   ```python
   hava_gunesli = True
   print(hava_gunesli)
   ```

---

### **Değişkenler Nedir?**
Değişkenler, bilgiyi sakladığımız kutular gibidir. İşte bir örnek:  
```python
isim = "Efe"
yas = 10
print(f"Benim adım {isim} ve {yas} yaşındayım.")
```

#### **Deneme Zamanı:**  
Kendi adını ve yaşını bir değişkene yaz ve ekranda göster.

---

## **3. Matematiksel İşlemler**

Python ile matematik yapmak çok kolay! İşte temel işlemler:  

- **Toplama:** `+`  
- **Çıkarma:** `-`  
- **Çarpma:** `*`  
- **Bölme:** `/`  

#### **Örnek:**
```python
sayi1 = 10
sayi2 = 3
print(sayi1 + sayi2)  # Toplama
print(sayi1 - sayi2)  # Çıkarma
print(sayi1 * sayi2)  # Çarpma
print(sayi1 / sayi2)  # Bölme
```

#### **Deneme Zamanı:**  
Kendi sayılarını kullanarak bir toplama işlemi yap.

---

## **4. Kullanıcıdan Veri Alma**

Python, senden bilgi alabilir! İşte nasıl yapılacağı:  
```python
isim = input("Adın nedir? ")
print(f"Merhaba, {isim}!")
```

#### **Deneme Zamanı:**  
Kullanıcıdan bir sayı al ve ikiyle çarp:  
```python
sayi = int(input("Bir sayı gir: "))
print(f"Girdiğin sayının iki katı: {sayi * 2}")
```

---

## **5. Koşullu İfadeler (if, elif, else)**

Koşullar, Python’a "Eğer şu doğruysa bunu yap, değilse şunu yap" dememizi sağlar.

#### **Örnek:**
```python
yas = int(input("Kaç yaşındasın? "))
if yas < 12:
    print("Sen bir çocuksun!")
elif yas < 18:
    print("Sen bir gençsin!")
else:
    print("Sen bir yetişkinsin!")
```

#### **Deneme Zamanı:**  
Bir sayı al ve onun pozitif mi, negatif mi olduğunu kontrol et:  
```python
sayi = int(input("Bir sayı gir: "))
if sayi > 0:
    print("Bu sayı pozitiftir.")
elif sayi < 0:
    print("Bu sayı negatiftir.")
else:
    print("Bu sayı sıfırdır.")
```

---

## **6. Mantıksal Operatörler (and, or)**

Mantıksal operatörlerle birden fazla koşulu aynı anda kontrol edebilirsin:

#### **Örnek:**
```python
hava_gunesli = input("Hava güneşli mi? (evet/hayır): ") == "evet"
hafta_sonu = input("Bugün hafta sonu mu? (evet/hayır): ") == "evet"
if hava_gunesli and hafta_sonu:
    print("Hadi dışarı çıkalım!")
else:
    print("Evde kalalım.")
```

---

## **7. Ödev: Tüm Öğrendiklerini Kullan!**

### **Görev: Kendi Hesap Makinenizi Yapın**
Kendi hesap makinenizi yazın. Programınız şu işlemleri yapabilmeli:  
- Kullanıcıdan iki sayı almalı.  
- Kullanıcı hangi işlemi yapmak istediğini seçmeli (toplama, çıkarma, çarpma, bölme).  
- İşlemi yapıp sonucu göstermeli.

#### **İpucu:**
```python
print("Hesap Makinesi")
sayi1 = int(input("Birinci sayıyı gir: "))
sayi2 = int(input("İkinci sayıyı gir: "))
islem = input("Hangi işlemi yapmak istiyorsun? (+, -, *, /): ")

if islem == "+":
    print(f"Sonuç: {sayi1 + sayi2}")
elif islem == "-":
    print(f"Sonuç: {sayi1 - sayi2}")
elif islem == "*":
    print(f"Sonuç: {sayi1 * sayi2}")
elif islem == "/":
    print(f"Sonuç: {sayi1 / sayi2}")
else:
    print("Geçersiz işlem!")
```

### **Bonus Görev: Sayı Tahmin Oyunu**
Bilgisayar bir sayı tutsun, sen de onu tahmin et!  
İpucu: Kullan `random.randint()`.

---

## **Tebrikler! 🎉**
Bu rehberle Python'un temellerini öğrendin. Artık kendi oyunlarını, hesap makineni ve daha fazlasını yapabilirsin! Unutma, her şey denemek ve hata yapmakla başlar. 😊
