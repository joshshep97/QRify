from core.main import bp
from flask import render_template, request
from .create_qr import create_qrcode


@bp.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        link = request.form.get('link')
        filename = request.form.get('filename')
        create_qrcode(link, filename)

    return render_template(
        'index.html',
        title='QRify'
    )