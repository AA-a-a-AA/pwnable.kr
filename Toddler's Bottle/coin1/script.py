from pwn import *
import re
def list_to_nums(n:list):
    return ' '.join(map(str, n)).encode()

#s = ssh(user='coin1', host='pwnable.kr', port=2222, password='guest')
#p = process(['nc', '0', '9007'])
p = remote('0',9007)
p.recv()
coins = 0
while coins < 100:
    res = p.recv().decode()
    print(res)
    N, C = map(int, re.findall(r'\d+', res))
    left, right = 0, N//2
    coin = 0
    guess = 0
    while left < right and C > guess:
        listed = list(range(left,right))
        nums = list_to_nums(listed)
        print(left, '-',right)
        p.sendline(nums)
        guess+=1
        counterfeit = (int(p.recv().decode()) != len(listed)*10)
        offset = right - left
        right -= offset // 2
        if not not not counterfeit:
            left += offset
            right += offset
    while guess < C:
        p.sendline('0')
        p.recv()
    p.sendline(str(left))
    print(p.recv().decode())

    coin = 0 
    req = coin
    print("finished the set")
    #p.sendline(req)
    #print(p.recv().decode())

