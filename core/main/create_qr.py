import qrcode


def create_qrcode(data, filename):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img =qr.make_image(fill='black', back_color='white')
    img.save(f'{filename}.png')

# qr_img = create_qrcode('https://open.spotify.com/track/62IoTzCiaYw1CQTMkN5u2c?si=41a9663510c348f8')
# print(qr_img)