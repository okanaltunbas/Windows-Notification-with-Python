from plyer import notification
import time

baslik = input("Lütfen bildirim için başlık giriniz : ")
icerik = input("Lütfen bildirim için içerik giriniz : ")

while True:
    try:
        bildirim_sure = int(input("Bildirim için süre belirleyiniz : "))
        break
    except:
        print("Hatalı giriş! Tekrar deneyiniz!")
def bildirim_gonder():

    notification.notify(title=baslik, message = icerik, app_icon = None, timeout = bildirim_sure)


bildirim_gonder()
time.sleep(bildirim_sure)
print("Bildirim süresi doldu!")