#before code
import random
global key1
global key2
global key3
global key4
global key5
global keyfordecrypt
global name
global ext
global seed
global skey
global skey1
global skey2
global skey3
global skey4
global skey5
global fullname
digitals = ['1,2,3,4,5,6,7,8,9,0']
import os
from string import ascii_letters
# end

#check for a file
exits = os.path.isfile("KEYS.txt")
if exits == True:
    save = open("KEYS.txt", "a")
    print('it is here')
elif exits == False:
    save = open("KEYS.txt", "x")
    print("we created it")
else:
    raise UserWarning("Uncommon error")
#code
key1 = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
key2 = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
key3 = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
key4 = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
key5 = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
keyfordecrypt = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
skey = input("seed1:")
random.seed(skey)
save.write(str(random.random()))
skey1 = input("seed2:")
random.seed(skey1)
save.write(str(random.random()))
skey2 = input("seed3:")
random.seed(skey2)
save.write(str(random.random()))
skey3 = input("seed4:")
random.seed(skey3)
save.write(str(random.random()))
skey4 = input("seed5:")
random.seed(skey4)
save.write(str(random.random()))
skey5 = input("seed6:")
random.seed(skey5)
save.write(str(random.random()))
print(key1,key2,key3,key4,key5,keyfordecrypt)
name = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
ext = random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)+random.choice(digitals)+random.choice(ascii_letters)
fullname = name+"."+ext
save.close()
os.rename("KEYS.txt", fullname)
input("Press enter to exit")
#end of code