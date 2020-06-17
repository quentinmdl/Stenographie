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
puis l'affiche"""

taille = len(msg)
taille_msg_binaire = bin(len(msg))[2:].rjust(8, "0")
msg_binaire = [bin(ord(x))[2:].rjust(8, "0") for x in msg]
str_binaire = ''.join(msg_binaire)
print(str_binaire)

# Chiffrment affine

"""alphabet = [["A", 0], ["B", 1], ["C", 2], ["D", 3], ["E", 4], ["F", 5], ["G", 6], ["H", 7], ["I", 8], ["J", 9],
             ["K", 10], ["L", 11], ["M", 12], ["N", 13], ["O", 14], ["P", 15], ["Q", 16], ["R", 17], ["S", 18],
             ["T", 19], ["U", 20], ["V", 21], ["W", 22], ["X", 23], ["Y", 24], ["Z", 25]];

chaine_chiffre = ""
chaine = msg.upper()
a = 7
b = 8

for p in range(0,len(chaine)):

    for i in range(0,26):
        if (chaine[p] == alphabet[i][0]):
            y = ((a * alphabet[i][1]) + b)%26
            chaine_chiffre = chaine_chiffre+alphabet[y][0]

    if (chaine[p] == " "):
        chaine_chiffre = chaine_chiffre+" "

print(chaine_chiffre)"""


#Récupère les bits de l'image et insére le msg

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









