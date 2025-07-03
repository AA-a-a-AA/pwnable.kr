#key1
pc = 0x00008cdc + 0x8
key1 = pc
print("key1: ", key1)
#key2
pc = 0x00008d00 
r6 = pc + 0x1
###thumb mode
pc = 0x00008d08
r3 = pc
r3 += 4
pc = r3
key2 = r3
print("key2: ", key2)

#key3
rl = 0x00008d7c + 0x4
key3 = rl
print("key3: ", key3)

#num
num = key1+key2+key3
print('num: ', num)

#flag: daddy_has_lot_of_ARM_muscl3