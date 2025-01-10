data = bytearray(b'\xf3\xe3\xef\xc0\xfc\xd3\xd2\xdf\xc9\xda\xe8\xcf\xda\xd8\xd0\xfa\xd5\xdf\xf3\xde\xda\xcb\xe4\xf3\xd2\xcb\x89\xd4\xc6')

for i in range(0, len(data)):
    data[i] = data[i] ^ 0xbb

print(data)


# Given values
mask = 0xc0dec0de
desired_output = 0x0c5e7bf6

# Find the input value
input_value = mask ^ desired_output

# Print the result
print(f'The input value is: {input_value:#010x}')
