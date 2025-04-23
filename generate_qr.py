import qrcode

data = ("https://www.instagram.com/suryansh_tripathii/?hl=en")

qr = qrcode.make(data)

qr.save("my_qrcode.png")

print("QR code generated and saved as my_qrcode.png")
