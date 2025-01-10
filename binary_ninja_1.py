data = bytearray(b'\x85\x95\x99\xb6\x95\x82\x9f\xe0\xb9\xa2\xe0\xb9\xa5\xa8\xe0\x8b\xa1\xac\xaa\xb0')

for i in range(0, len(data)):
    data[i] = data[i] ^ 0xcd

print(data)

print(int(0x926))