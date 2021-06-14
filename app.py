# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
# String which represents the QR code 
s = "https://www.instagram.com/python_wisdom/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png('qrcode.png', scale = 6) 
