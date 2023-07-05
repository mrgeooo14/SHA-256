import numpy as np

#### Convert int to bytes
def int_to_bytes(x: int) -> bytes:  
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

#### Convert message to a binary string
def to_bits(str):  
    return ''.join(format(ord(i), '08b') for i in str)

#### Small Padding
def get_bin(x, n=0):  
    return format(x, 'b').zfill(n)

#### Shift Right Operation
def shift_right(x, y):  
    z = int(x, 2) >> y
    # print('ok', z)
    return "{0:b}".format(z).zfill(32)


def XOR(x, y):
    z = int(x, 2) ^ int(y, 2)
    return "{0:b}".format(z).zfill(32)

#### Addition between two binary numbers strings
def addition(x, y): 
    z = int(x, 2) + int(y, 2)
    z2 = np.mod(z, 2 ** 32)  # As per usual, all addition is modulo 2^32
    return "{0:b}".format(z2).zfill(32)

#### Right Rotate Operation
def rightRotate(msg, n):  
    r_first = msg[0: len(msg) - n]
    r_second = msg[len(msg) - n:]
    return r_second + r_first


def NOT(x):  # 'NOT' Operation
    return ''.join(['1' if i == '0' else '0' for i in x])


def AND(x, y):  # 'AND' Operation
    z = int(x, 2) & int(y, 2)
    return "{0:b}".format(z).zfill(32)