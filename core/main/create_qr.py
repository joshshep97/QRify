import qrcode


def create_qrcode(data, filename, fill_color, back_color):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img =qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f'{filename}.png')

    from PIL import Image
    with Image.open(f'{filename}.png') as im:
        im.show()

# qr_img = create_qrcode('https://open.spotify.com/track/62IoTzCiaYw1CQTMkN5u2c?si=41a9663510c348f8')
# print(qr_img)