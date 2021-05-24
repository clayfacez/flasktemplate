import qrcode
import random

def create_qr_code(tracking_num):
    url_qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
    url_qr_code.add_data(tracking_num) # ? what should input_data be?
    url_qr_code.make(fit=True)
    img = url_qr_code.make_image(fill='black', back_color='white')
    num_only = tracking_num[26:]  # Slide off just the number
    img.save(f'static/qr_{num_only}.png')
    return num_only

    
tracking_num = ''
for i in range(8):
  tracking_num += random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ])
print('Here is your order number', tracking_num)
tracking_url = 'https://some.com/track?id=' + tracking_num
print('Here is your tracking url', tracking_url)  # Into QR code
code = create_qr_code(tracking_url)  # Call the function
print('Check the files area for the QR image.')

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", code=code)

app.run(host='0.0.0.0', port=8080)

# def create_qr_code(tracking_num):
#     url_qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
#     url_qr_code.add_data(tracking_num) # ? what should input_data be?
#     url_qr_code.make(fit=True)
#     img = url_qr_code.make_image(fill='black', back_color='white')
#     num_only = tracking_num[26:]  # Slide off just the number
#     img.save(f'qr_{num_only}.png')

# tracking_num = ''
# for i in range(8):
#   tracking_num += random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ])
# print('Here is your order number', tracking_num)
# tracking_url = 'https://some.com/track?id=' + tracking_num
# print('Here is your tracking url', tracking_url)  # Into QR code
# create_qr_code(tracking_url)  # Call the function
# print('Check the files area for the QR image.')


  