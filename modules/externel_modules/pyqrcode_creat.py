"""
generate qr code:- pyqrcode #install pip
"""
import pyqrcode
import png
x="hai dears"
url=pyqrcode.create(x)
url.svg("my_qrcode.svg",scale=8)


url=pyqrcode.create(r"C:\Users\ANAGHA\PycharmProjects\pythoncourse\modules\externel_modules\pic.png")
url.png("my_qrcode2.png",scale=8)


