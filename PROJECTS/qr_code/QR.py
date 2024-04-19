import qrcode as qr
from PIL import Image


print(" Customized QRCode ? ")
option=input(' YES/NO ')

def normal_QRCode(input_text,title):
 img= qr.make(input_text)

 img.save(title+".png") 

def customized_QRCode(input_text,title):
 print("Custom qr code generator ***`Enter size and border in number`***")
 size=input('Enter size of the QR Code:')
 QR_Border=input('Enter border for the QR Code:')
 color=input('Enter color for the QR Code:')
 background=input('Enter background color for the QR Code:')


 QR= qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H,box_size=size,border=QR_Border,)

 QR.add_data(input_text)
 QR.make(fit=True)
 img=QR.make_image(fill_color=color,back_color=background)
 img.save(title+".png")

input_text=input("Enter your text, link or image :")
title=input("enter your QR code title:")

if option=="NO":
 normal_QRCode(input_text,title)
elif option=="YES":
 customized_QRCode(input_text,title)
else:
 print("Wrong input")