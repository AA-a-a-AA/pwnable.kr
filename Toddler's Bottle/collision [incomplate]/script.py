
import struct
import sys
HASH = 0x21DD09EC
part = HASH // 5 #113626824 0x6c5cec8
remainder = part + HASH % 5 #113626828 0x6c5cecc

b = 0x41414141 
a = 0x1cd804e8
c = HASH - a - b*4
###test###
print(part, remainder)
print(hex(part), hex(remainder))
print(part*4 + remainder == HASH)
exit()
###test###

bytes = struct.pack(">IIIII",part,part,part,part,remainder) 
print("\nbytes: \n", bytes, len(bytes), "\n")

print(sys.stdout.buffer.write(bytes))
read = sys.stdin.buffer.read(20)
unpacked = struct.unpack(">IIIII", read)
print("\nunpacked:\n" + str(unpacked))
print("\nsum unpacked:\n" + str(sum(unpacked)))
print("\ncheck:\n" , sum(unpacked) == HASH)

exit()


sys.stdin.flush()
sys.stdout.flush()

print("\nargv: \n" + str(sys.argv))
print(bytes)
import subprocess
subprocess.run(["./col", sys.stdout.buffer.write(struct.pack(">IIIII",part,part,part,part,remainder))])
#print(bytes == b'\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xcc')
#print(b'\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xcc')


#b'\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xc8\x06\xc5\xce\xc8\r\x8b\x9d\x94'