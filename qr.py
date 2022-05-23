import qrcode
from PIL import Image, ImageDraw



img = qrcode.make(

'https://aditya-pratap.github.io/portfolio.github.io/')

img.save('myQRcode.png')
img.show()