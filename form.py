import utkangalaxy
print("Form Sistemine hoş geldiniz")

data_ad = []
data_soyad = []

while True:
    ad = input("Adınızı girin :")

    print("Sisteme Adınız kaydediliyor ", ad)

    data_ad.append(ad)

    utkangalaxy.wait(3)

    print("Veri kaydedildi")

    utkangalaxy.wait(1)

    utkangalaxy.cmd("clear")

    soyad = input("Soyadınız girin : ")

    print("Sisteme SoyAdınız kaydediliyor ", soyad)

    data_soyad.append(soyad)

    utkangalaxy.wait(3)

    print("Veri kaydedildi")

    utkangalaxy.wait(1)

    utkangalaxy.cmd("clear")

    print("Mevcut kişilerin adı : ", data_ad)
    print("Mevcut kişilerin soyadı : ", data_soyad)