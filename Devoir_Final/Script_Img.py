from main import *
from PIL import Image

# coding: utf8

#Chiffrment et insertions

if __name__ == '__main__':
    main()

msg = "ça va frère le boss ? t'es en mode Lacoste Tn et tout, car moi ouai"

img = Image.open("img.jpg")

w,h = img.size

r,g,b = img.split()

r = list(r.getdata())

"""Convertir la chaine de caractère en binaire en rajoutant des '0' si jamais on arrive pas à 8 caractères,
récupérer  sa taille (décimal et binaire),
puis l'affiche""""

taille = len(msg)
taille_msg_binaire = bin(len(msg))[2:].rjust(8, "0")
msg_binaire = [bin(ord(x))[2:].rjust(8, "0") for x in msg]
str_binaire = ''.join(msg_binaire)
print(str_binaire)


"""Récupère les bits de l'image et insére le msg"""

for j in range(8):
    r[j]=2*int(r[j]//2)+int(taille_msg_binaire[j])
for i in range(8*taille):
    r[i+7]=2*int(r[i+7]//2)+int(str_binaire[i])

nr = Image.new("L",(16,16))
nr = Image.new("L",(w,h))
print(w,h)
print(taille,"= "+ taille_msg_binaire)
nr.putdata(r)

imgnew = Image.merge('RGB',(nr,g,b))
imgnew.save("img_msg.jpg")


#Déchiffrement

img_cacher = Image.open("img_msg.jpg")
r,g,b = img_cacher.split()
r = list(r.getdata())









