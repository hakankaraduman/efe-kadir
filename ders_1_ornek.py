ben = "hakan"
yegen_1 = "efe"
yegen_2 = "kadir"
yas = 5
kimi = "yaşında ufak bir çocuk"
# bayildimi = True
bayildimi = False

# bool -> Evet hayır tipindeki veri, sadece True ya da False değerini alabilir
# number -> numara tipinde veri
# string -> " " çift tırnak içine yazılan yazı
print(f"benim adım {ben}, {yegen_1} ve {yegen_2}le {yas} {kimi} dövüyorum. Bayıldı mı? {bayildimi}");

cevap = input("Sen de 5 yaşındaki ufak bir çocuğu dövebilir misin?"); # normalde string tipine sahiptir
print(f"Kullanıcının cevabı: {cevap}");


### Bu kısmı okuyup anlamaya çalış
cevap = input("Sen kaç yaşındasın? \n"); # string
# \n karakteri, terminalde bir alt satıra geçer
cevapNumara = int(cevap) # int

print(f"Kullanıcının yaşı: {cevapNumara}");

if cevapNumara == 5: # noktalı virgül değil, iki nokta üst üste, alt satırda iki tane space olmak zorunda
  print("ufak bir çocuk gördün, döv onu");
else: # if, else'den sonra iki nokta gelir.
  print("okula git");
