import random
import string

rakamlar="0123456789"
semboller=string.punctuation
kucukHarf=string.ascii_lowercase
buyukHarf=string.ascii_uppercase


sifre=""

for i in range(2):
 sifre+=rakamlar[random.randint(0,9)]

for i in range(1):
 sifre+=semboller[random.randint(0,9)]

for i in range(2):
  sifre+=kucukHarf[random.randint(0,9)]

for i in range(1):
   sifre+=semboller[random.randint(0,9)]

for i in range(2):
   sifre+=buyukHarf[random.randint(0,9)]

print("güvenli şifre oluştur:",sifre)