import numpy as np
from basic_operations import get_bin

# ~~~~~~~~~~~~~~~~~Functions we will use~~~~~~~~~~~~~~~~~~~~~~~

def padding(msg):  # Function to perform padding
    length = len(msg)
    n_zeros = (512 - np.mod(length, 512)) - 64  # Wanted Final Length: A multiplier of 512 - 64 bits for the length
    zeros = get_bin(0, n_zeros)
    last64 = get_bin(length - 1, 64)  # Last 64 bits (-1 to not count the '1' we appended)
    return msg + zeros + last64


def message_blocks(msg, n):   # Split the message bits into blocks sized n, in our case n = 512
    message_block = []
    for index in range(0, len(msg), n):
        message_block.append(msg[index: index + n])
    return message_block


def add_words(blocks):  # Make sure that everything is size = 32
    while len(blocks) < 64:
        blocks.append(get_bin(0, 32))