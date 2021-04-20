
import binascii
from pyDes import des,triple_des
import hashlib


#des encrypt or decrypt, pure data
def des_crypt(data, key, encrypt=1):
    k = des(key)
    if(encrypt):
        enc = k.encrypt(data)
    else:
        enc = k.decrypt(data)
    return enc

#triple des encrypt or decrypt, pure data
def triple_des_crypt(data, key, encrypt=1):
    k = triple_des(key)
    if(encrypt):
        enc = k.encrypt(data)
    else:
        enc = k.decrypt(data)
    return enc

def md5_rst(data):
    m = hashlib.md5()
    m.update(data)
    rst = m.digest()
    return rst

if "__main__" == __name__:

    key = '\x11\x22\x33\x44\x55\x66\x77\x88'
    d = des_crypt('\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40', key)
    print binascii.hexlify(d)
    p = des_crypt(d, key, 0)
    print binascii.hexlify(p)

    d = md5_rst("\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41")
    print binascii.hexlify(d)