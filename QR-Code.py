# QR Code erzeugen
# pip install --upgrade pip
# pip install qrcode
# pip install pillow

import qrcode

def make_qr(filename, msg):
    img = qrcode.make(msg)
    img.save(filename)
    img.show()

def make_qr_color():
    qr = qrcode.QRCode()
    qr.add_data("Dies ist ein Test!")
    img = qr.make_image(fill_color="blue", back_color="yellow")
    img.save("test.png")
    img.show()    

import qrcode.image.svg # Als Vectorgrafik
def make_qr_svg():
    img = qrcode.make("Dies ist ein Test", image_factory = qrcode.image.svg.SvgPathImage)
    img.save("test.svg")

make_qr_svg()