import qrcode
from qrcode.image.svg import SvgPathImage

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(image_factory=SvgPathImage)
    
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(img.to_string().decode('utf-8'))

def generate_qr_codes(input_filename):
    with open(input_filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # eltávolítja a felesleges szóközöket és újsor jeleket
            if line:  # csak akkor hozza létre a QR kódot, ha a sor nem üres
                output_file = f"{line}.svg"
                generate_qr_code(line, output_file)

generate_qr_codes("kodok.txt")
