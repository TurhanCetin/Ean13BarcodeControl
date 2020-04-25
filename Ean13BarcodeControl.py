

import re

dosya = open("barkodlar.txt")
newDosya = open("geçerliBarkod.txt","w+")#burda istediğimiz barkodlara ulaşmak için yeni txt dosyaları açıp oraya kaydettik#
turkBarkod = open("turkBarkod.txt","w+")

tek = 0
cift = 0
toplam = 0
yakinSayi = 0
fark = 0


def YakinSayi(toplam,list,number): # en yakın onun katını bulmak için while döngüsü kullandık ve o sayıyı toplamdan çıkararak txtdeki şartı sağlayıp sağlamamasına baktık#
    yakinSayi = toplam
    while yakinSayi %10 != 0:
        yakinSayi += 1

    fark = yakinSayi - toplam
    onucKontrol(fark,list,number)

def TurkMali(number): #Düzenli ifadeler kullanarak 869la başlayan barkodaları aldık#
    turkMali = re.findall("869\S+",number)
    if turkMali != []:
        print("Türk Malı Olan Barkodlar : ", turkMali)
        turkBarkod.write(str(turkMali)+"\n")


def onucKontrol(fark,list,number):#Yukarda yakınsayı fonksiyonundaki fark değişkenini burda barkodun sonuncu basamağı ile karşılaştırdık buda txt dosyasındaki şartlardan biriydi#
    if fark == list[12]:

        print(fark,"=", list[12]," Olduğu için geçerli barkod")
        newDosya.write(str(barkod)+"\n")
        TurkMali(str(number),)
        return True
    else:
        print(fark ,"!=", list[12]," Oldugu icin geçersiz barkod")
        return False



for line in dosya:
    line = re.findall("(\d{13})", line)
    for word in line:
        tek = 0
        cift = 0
        if word != []:# burada string olarak txtden aldığımız barkodları array(liste) haline dönüştürdük buda bana basamaklarlar uğraşırken kolaylık sağladı her indexe ulaşmak için array(liste) haline getirdim#
            number = str(word)
            barkod = list(number)
            map_object = map(int, barkod)
            barkod = list(map_object)
            for eleman in range(0,12):
                if eleman % 2 == 0:
                    tek += barkod[eleman]
                else:
                    cift += barkod[eleman]
            cift = cift *3
            toplam = tek + cift
            YakinSayi(toplam, barkod,number)



