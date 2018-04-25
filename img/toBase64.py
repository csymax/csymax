
import base64
f = open(r'C:\Users\Administrator\Desktop\0426\2.png', 'rb')
ls_f = base64.b64encode(f.read())
f.close()
print(ls_f)