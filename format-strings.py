chunks_64 = ['7b4654436f636970','355f31346d316e34','3478345f33317937','65355f673431665f','7d346263623736']
flag = ''
for chunk in chunks_64:
    decoded_chunk = ''
    for i in range(0, len(chunk), 2):
        c = chr(int(chunk[i]+chunk[i+1],16))
        decoded_chunk += c
    flag += decoded_chunk[::-1]
print(flag)
