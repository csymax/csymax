
import base64
f = open(r'C:\Users\Administrator\Desktop\0408\js-TwoWayDataBinding-1.png', 'rb')
ls_f = base64.b64encode(f.read())
f.close()
print(ls_f)