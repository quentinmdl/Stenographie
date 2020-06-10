from main import *
from PIL import Image
from Script_Img import *

if __name__ == '__main__':
    main()

img = Image.open("img_msg.jpg")
r,g,b = img.split()
r = list(r.getdata())

p=[str(x%2) for x in r[0:8]]
q="".join(p)
q=int(q,2)

n=[str(x%2) for x in r[8:8*(q+1)]]

b="".join(n)
message=""

for k in range(0,q):
    l=b[8*k:8*k+8]
    message=message+chr(int(l,2))
print(message)