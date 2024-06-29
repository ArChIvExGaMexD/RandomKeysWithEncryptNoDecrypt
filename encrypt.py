import random
import os
from string import ascii_letters
digitals = [1,2,3,4,5,6,7,8,9,0]
class encrypt:
    def main():
        a = input("file name for encrypt:")
        f = open(a)
        p = f.read()
        dec = random.seed(p)
        f.close()
        f = open("file.txt", "x")
        decstr = str(dec)
        f.write(decstr)
        f.close()
        name = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
        ext = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
        fullname = name+"."+ext
        os.rename("file.txt", fullname)
    def encrypt():
        f = open(encrypt)
        p = f.read()
        dec = random.seed(p)
        f.close()
        f = open("file.txt", "x")
        decstr = str(dec)
        f.write(decstr)
        f.close()
        name = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
        ext = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
        fullname = name+"."+ext
        os.rename("file.txt", fullname)


a = input("file name for encrypt:")
f = open(a)
p = f.read()
dec = random.seed(p)
f.close()
f = open("file.txt", "x")
decstr = str(dec)
f.write(decstr)
f.close()
name = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
ext = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
fullname = name+"."+ext
os.rename("file.txt", fullname)