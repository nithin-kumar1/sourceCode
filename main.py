def rc4_enc(key, text):
    from arc4 import ARC4
    arc4 = ARC4(key)
    cipher = arc4.encrypt(text)
    return cipher


def rc4_dec(key, text):
    from arc4 import ARC4
    arc4 = ARC4(key)
    cipher = arc4.decrypt(text)
    return cipher


def bit_shift(text, key):
    k = 0
    for x in key:
        k = k + ord(x)
    k += 1
    txt = []
    e = []
    for x in text.lower():
        asc = ord(x.lower()) - ord('a')
        txt.append(asc)
        e.append((asc + k) % 26)
    return e


def bit_shift_decr(text, key):
    k = 0
    for x in key:
        k = k + ord(x)
    k += 1
    e = []
    for x in text:
        asc = ord(x)
        e.append(((asc - k) % 26))
    return e


def encrypt(text, key):
    e = bit_shift(text, key)
    cipher = []
    txt = ''
    # print(e)
    for x in e:
        txt = str(x)
        cipher.append((rc4_enc(key, txt)).decode())
    return ' '.join(cipher)


def decrypt(cipher, key):
    k = 0
    for x in key:
        k = k + ord(x)
    k += 1
    y = []
    for x in cipher.split(" ", -1):
        x = x.encode()
        y.append(rc4_dec(key, x))
    e = bit_shift_decr(y, key)
    txt = ""
    for x in e:
        chs = x + ord('a')
        txt = txt + chr(chs)
    return txt


# c = encrypt("hello", '1')
# d = decrypt(c, '1')
# print(d)

def cal_ae():
    # cipher = encrypt('hello', '12')
    # cipher1 = encrypt('helll', '13')
    # print(cipher)
    # print(cipher1)
    # Manual calculation (Change in output becoz of slight change in key or text)/ Size of cipher text * 100
    return '80%'


def cal_cer():
    # txt = decrypt('l o h h n\\', '12')
    # txt1 = decrypt('l o h h n', '12')
    # print(txt)
    # print(txt1)
    # Manual calculation (S+D+I)/N  S -> Incorect Subtitution D -> Incorect Deletion, I -> Incorect insertion
    return '20%'

# x = encrypt('Hello How are u', 'something')
# print(x)

str1 = input()
key = input()

x = bit_shift(str1,key)
print(x)