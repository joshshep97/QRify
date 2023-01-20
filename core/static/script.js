imgWrapper = document.querySelector('#imgs')
qrImg = document.querySelector('#qr_img')
qrImgBlue = document.querySelector('#qr_img_blue')

images = [
    "static/img/qr.png",
    "static/img/qr_red.png",
    "static/img/qr_blue.png",
]

let imageIndex = 0;

imgWrapper.addEventListener('mouseover', () => {
    qrImg.setAttribute('src', images[1])
    // qrImg.setAttribute('height', '200')
    // qrImgBlue.style.display = 'inline'

    })
imgWrapper.addEventListener('click', () => {
    qrImg.setAttribute('src', images[2])
    // qrImg.setAttribute('height', '200')
    // qrImgBlue.style.display = 'none'
    })
imgWrapper.addEventListener('mouseout', () => {
    qrImg.setAttribute('src', images[0])
    // qrImg.setAttribute('height', '200')
    // qrImgBlue.style.display = 'none'
    })

// http://127.0.0.1:5050/static/img/qr.png