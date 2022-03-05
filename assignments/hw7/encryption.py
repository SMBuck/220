def encode(message, key):
    for letter in message:
        secret = ord(letter)
        secret_enc = secret + key
        uncovered_enc = chr(secret_enc)
        return uncovered_enc


def encode_better(message, key):
    length = len(message)
    length_2 = len(key)
    for i in range(length):
        letters = message[i]
        cipher = i % length_2
        cipher_message = key[cipher]
        encrypt_1 = ord(letters) - 65
        encrypt_2 = ord(cipher_message) - 65
        full_encrypt = encrypt_1 + encrypt_2
        unknown = (full_encrypt % 58) + 65
        discovered = chr(unknown)
        print(discovered, end="")
