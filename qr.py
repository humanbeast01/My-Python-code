'''import qrcode as qr
img=qr.make("https://www.instagram.com/human_beast01?igsh=MXZ5N200MnRoZDJ1NQ==")
img.save("Mukul_intagram.png")'''
import qrcode
 
# Data to encode
data = "GeeksforGeeks"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
 
img.save('MyQRCode2.png')
