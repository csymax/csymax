
import base64
f = open(r'C:\Users\Administrator\Desktop\0428\2.png', 'rb')
txtf = open(r'C:\Users\Administrator\Desktop\0428\1.txt', 'w')
ls_f = base64.b64encode(f.read())
f.close()
# print(ls_f)
txtf.write(str(ls_f))
txtf.close()