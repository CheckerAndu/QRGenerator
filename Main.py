import segno
import time 

def generate_qr():
    # ask for the URL
    link = input("Enter the URL Link you want to convert to QR Code: \n")
    time.sleep(2)
    filename = input("What do you want to name the file? e.g. my_qr_code \n")

    # create QR code
    print (f"Generating QR Code for: {link} ...")
    qrcode = segno.make_qr(link)
    time.sleep(2)

    # save QR code as PNG
    # add .png to the filename and make it a bit bigger (scale=10)
    qrcode.save(f"{filename}.png", scale=10)

    print(f"Success! Check your folder for the file: {filename}.png")

generate_qr()