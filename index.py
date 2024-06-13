import qrcode 

from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://x.com/harshit_bk");

qr.make(fit=True)

img = qr.make_image(back_color=(0, 0, 0), fill_color=(96, 255, 71))

img.save("harshit_X.png");
