import time
import random
print("'Sayı Tahmini Oyunu'")
name = input("Lütfen istediğiniz kullanıcı adını giriniz: ")
time.sleep(1)
print("""////////////////////////////////////////////////////////////////////////////////////////////////////////
                                Hoşgeldin {}. Sayı tahmini oyunu başlıyor...                                                           
                                                                                                        
* Oyunun amacı adından da anlayacağın gibi benim seçtiğim bir sayıyı tahmin etmek.                       *
* Toplamda 10 tahmin hakkın var ve sayı 1 ile 1000 arasında.                                             *
* Her tahmininden sonra sana ipucu vereceğim.                                                            *           
* Eğer 1 ile 1000 arası bir sayı girmezsen değerlendirmeye alınmayacak fakat tahmin haklarından düşecek. *
* Hakların bittiğinde oyun kendiliğinden sonlanacak                                                      *
                                                                                                       
////////////////////////////////////////////////////////////////////////////////////////////////////////""".format(name))
time.sleep(1)

print("Şimdi ilk tahminini yazabilirsin: ")
random = random.randint(1,1000)
for i in range(10):
    try:
        tahmin = int(input())
        deneme = 0
        if tahmin < 0 or tahmin > 1000:
            print("Lütfen 1-1000 arası bir sayı gir {}. Hakların boşa gidiyor...".format(name))
        elif tahmin < random:
            print("Sayıyı biraz daha yükselt :)")
        elif tahmin > random:
            print("Sayıyı biraz küçült :)")
        else:
            print("Tebrikler {}. Sayımız {} idi.".format(name, random))
            break
    except:
        print("Lütfen sadece sayı giriniz!!")

print("Oyun Sonra erdi...")