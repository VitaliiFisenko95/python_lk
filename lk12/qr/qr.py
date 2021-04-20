import qrcode


def build_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode001.png')


build_qr({'1': 1})


def decode_qr(fp: str):
    pass


decode_qr('qrcode001.png')
