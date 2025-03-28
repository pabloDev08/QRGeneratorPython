import qrcode 
from PIL import Image 

def generate_qr_code(text,file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 20,
        border = 4,       
    )

    qr.add_data(text)
    qr.make(fit = True)

    img = qr.make_image(fill_color = "#000000", back_color = "#FFFFFF")

    img.save(file_name)
    print(f"QR code guardado como {file_name}")

if __name__ == "__main__":
    text = input("Introduce un texto o una URL para generar el código QR: ")
    file_name = input("Introduce el nombre del código QR que contenga SIEMPRE la extensión .png: ")
    generate_qr_code(text,file_name)

