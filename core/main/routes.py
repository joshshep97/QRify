from core.main import bp
from flask import render_template, request
from .create_qr import create_qrcode


@bp.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        link = request.form.get('link')
        filename = request.form.get('filename')
        qr_fill_color = request.form.get('fill-color')
        qr_back_color = request.form.get('back-color')

        create_qrcode(link, filename, qr_fill_color, qr_back_color)

    return render_template(
        'index.html',
        title='QRify'
    )