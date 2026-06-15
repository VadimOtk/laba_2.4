def encrypt_file(input_file, output_file, key):
    key = key & 0xFF
    with open(input_file, 'rb') as f:
        data = f.read()

    result = bytearray()
    for byte in data:
        byte = ((byte << 2) | (byte >> 6)) & 0xFF
        byte = byte ^ key
        result.append(byte)

    with open(output_file, 'wb') as f:
        f.write(result)


def decrypt_file(input_file, output_file, key):
    key = key & 0xFF
    with open(input_file, 'rb') as f:
        data = f.read()

    result = bytearray()
    for byte in data:
        byte = byte ^ key
        byte = ((byte >> 2) | (byte << 6)) & 0xFF
        result.append(byte)

    with open(output_file, 'wb') as f:
        f.write(result)


test = bytes([10, 20, 30, 40, 50, 100, 200, 255])
with open('resource/original.bin', 'wb') as f:
    f.write(test)

encrypt_file('resource/original.bin', 'resource/encrypted.bin', 42)
decrypt_file('resource/encrypted.bin', 'resource/decrypted.bin', 42)

with open('resource/original.bin', 'rb') as f1, open('resource/decrypted.bin', 'rb') as f2:
    if f1.read() == f2.read():
        print('Проверка пройдена успешно')
    else:
        print('Ошибка: файлы не совпадают!')