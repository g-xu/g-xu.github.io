import binascii
import zlib

# used for dvb ccitt
def crc_ccitt(data, init=0):
    crc_table=[0]*256
    #setup crc table
    for i in range(256):
        crc = i<<24
        for j in range(8):
            if(crc & 0x80000000):
                crc = (crc<<1)^0x04c11db7
            else:
                crc = crc<<1
        crc_table[i] = crc

    crc = init
    for i in range(len(data)):
        idx = ((crc>>24)&0xFF)^ord(data[i])
        crc = (crc_table[idx]^(crc<<8))&0xFFFFFFFF

    return crc

# mt crc32
def crc_32_mt(data, init=0):
    crc_table=[0]*256
    #setup crc table
    for i in range(256):
        crc = i
        for j in range(8):
            if(crc & 1):
                crc = (crc>>1)^0xedb88320
            else:
                crc = crc>>1
        crc_table[i] = crc&0xFFFFFFFF

    crc = init
    for i in range(len(data)):
        crc = (crc_table[(crc&0xFF)^ord(data[i])]^(crc>>8))&0xFFFFFFFF

    #print hex(crc)
    return crc

#same as mt crc32    
def crc_32_mt2(data, init=0):
    crc = binascii.crc32(data, ~init)
    return (~crc)&0xFFFFFFFF

# normal crc32
def crc_32(data, init=0):
    return binascii.crc32(data, init)&0xFFFFFFFF

# block crc
def block_crc(data, init=0):
    crc =  binascii.crc32(data, init)
    return (~crc)&0xFFFFFFFF

#same as binascii.crc32
def zlib_crc(data, init=0):
    return zlib.crc32(data, init)

if "__main__" == __name__:

    data = "e0cd29e3e0df29e5e07329e6e07e29e7e07f29e8e08029e9e08129eae08229ebe0832a0be1892a0ee18c2a0fe18d52ae2458"
    ndata = binascii.unhexlify(data)
    print('>>ccitt: 0x%x 0x%x' %(crc_ccitt(ndata, 0),crc_ccitt(ndata, 0xFFFFFFFF)))
    print('>>mt: 0x%x 0x%x' %(crc_32_mt(ndata, 0),crc_32_mt(ndata, 0xFFFFFFFF)))
    print('>>mt2: 0x%x 0x%x' %(crc_32_mt2(ndata, 0),crc_32_mt2(ndata, 0xFFFFFFFF)))
    print ('>>crc32: 0x%x 0x%x' %(crc_32(ndata, 0),crc_32(ndata, 0xFFFFFFFF)))
    print ('>>blockcrc: 0x%x 0x%x' %(block_crc(ndata, 0),block_crc(ndata, 0xFFFFFFFF)))
    print ('>>zlib_crc: 0x%x 0x%x' %(zlib_crc(ndata, 0),zlib_crc(ndata, 0xFFFFFFFF)))



