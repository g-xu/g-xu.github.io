import binascii
import struct

# 'f61563e82305'    -->>  '0xf6,0x15,0x63,0xe8,0x23,0x05'
def cont_str_2_0xstr(hex_str):
    if len(hex_str)%2:
        print("not even num for hex")
    print ('0x' + ',0x'.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2)))

# 'f61563e82305'   -->>   '0xf6,0x15,0x63,0xe8,0x23,0x05', 16B every line
def cont_str_2_line_0xstr(hex_str):
    l = ['0x'+hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    print ','.join('\n' * (n % 16 == 0) + l  for n, l in enumerate(l))

# 'f61563e82305'   -->>   '\xf6\x15\x63\xe8\x23\x05'
def cont_str_2_bytes(hex_str):
    if len(hex_str)%2:
        print "not even num for hex"
    print '\\x' + '\\x'.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2)) 

# 'f61563e82305'   -->>   bytes '\xf6\x15\x63\xe8\x23\x05' 
def cont_str_2_binary(hex_str):
	return binascii.unhexlify(hex_str)


# '48 80 73 a0 08 f1'   -->>   '\x48\x80\x73\xa0\x08\xf1'
def hex_2_bytes(hex_str):
    print '\\x'+"\\x".join(hex_str.split())

# '48 80 73 a0 08 f1'   -->>   '0x48,0x80,0x73,0xa0,0x08,0xf1'
def hex_2_0xstr(hex_str, split_line=False):
    hl = ['0x'+x+',' for x in hex_str.split()]
    #each line 16B
    if split_line:
        for i in range(16,len(hl),17):
            hl.insert(i,'\n')
    print ''.join(hl)            

# 'uio201Jx'  -->>  '0x75,0x69,0x6f,0x32,0x30,0x31,0x4a,0x78'
def ascii_2_array(ascii_str):
    print ','.join(['0x{:02x}'.format(ord(d)) for d in ascii_str])

# bytes  ''  -->> '0xaa,0xbb,0xcc'...
def bytes_2_0xstr(bin):
    nstr = [hex(ord(bin[i])) for i in range(len(bin))]
    print ','.join(nstr)

# read file, and print in '0xaa,0xbb' format, 16Byte every line    
def file_2_0xstr(fin):
    data = open(fin,'rb').read()
    print ','.join('\n' * (n % 16 == 0) + '0x{:02x}'.format(ord(l))  for n, l in enumerate(data))

if "__main__" == __name__:
    hstr = 'f61563e82305f61563e82305f61563e82305f61563e82305f61563e82305f61563e82305'
    cont_str_2_0xstr(hstr)
    cont_str_2_bytes(hstr)
    cont_str_2_line_0xstr(hstr)
    #cont_str_2_char(hstr)

    hstr2 = '48 80 73 a0 08 f1 48 80 73 a0 08 f1 48 80 73 a0 08 f1 48 80 73 a0 08 f1 48 80 73 a0 08 f1'
    hex_2_bytes(hstr2)
    hex_2_0xstr(hstr2, 1)

    test1='1234567890'
    ascii_2_array(test1)

    test2 = '\x11\x22\x33\x44\x55\x66\x77\x88'
    bytes_2_0xstr(test2)

    #file_2_0xstr('test.bin')
    