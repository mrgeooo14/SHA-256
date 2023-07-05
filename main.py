from algorithm_structure import message_schedule, msg_compression
from basic_operations import *
from functions import add_words, message_blocks, padding
from generate_hash_values import create_constants, hash_values

# ~~~~~~~~~~~~~~~~~~~~Command Line Visualization~~~~~~~~~~~~~~~~~~~~~~~
def printing(values1, values2, finalvalues):  # Function to print what happened during the algorithm
    chars1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    chars2 = ['h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7']

    print('               Initial Values: ')
    for i in range(len(values1)):
        print(chars1[i], ':', values1[i], '|', hex(int(values1[i], 2)))

    print(' ')
    print('               Final Values: ')
    for i in range(len(values2)):
        print(chars1[i], ':', values2[i], '|', hex(int(values2[i], 2)))

    print(' ')
    print('                                             Concatinate Final Hash: ')
    for i in range(len(finalvalues)):
        print(chars2[i], ':', values1[i], '+', values2[i], '=', finalvalues[i], ' <=> ', hex(int(finalvalues[i], 2)))

# ~~~~~~~~~~~~~~~~~~~~Main Function ~~~~~~~~~~~~~~~~~~~~~~~

#### SHA-256 Algorithm function to only take the message as input
#### This function makes up the full overall structure and functionality of the SHA-256 algorithm.
def final_sha256(msg):
    print(' ')
    print('                                SHA-256 Cryptographic Hash Function                               ')
    print(' ')
    digest = ''  # Final Digested String
    fv = []  # Array to hold the final hash values [for printing purposes]
    msg_in_bits = to_bits(msg) + '1'  # 1.1 - Convert the message to bits and append a single '1' at the end
    padded_msg = padding(msg_in_bits)  # 1.2 - Pad the message to size 512 and the last 64 bits representing its length

    print('Original Message: ', msg, '| Binary (+1): ', msg_in_bits)
    print(' ')
    print('Padded Message: ', padded_msg, '| Length: ', len(padded_msg))
    print(' ')

    blocked = message_blocks(padded_msg, 512)  # 2.1 - Split the message into blocks of 512
    scheduled_message = message_schedule(blocked)  # 2.2 - Message Schedule Loop

    hash_v = hash_values()  # 3.1.1 - Get the Hash Values
    constants = create_constants()  # 3.1.2 - Get the hash constants

    # 3.2 - Message Compression Loop to get the compressed hash values:
    alphabet_values = msg_compression(hash_v, scheduled_message, constants)

    if len(hash_v) != len(alphabet_values):
        return ValueError("Initial Hash Values don't match Final Hash Values")
    else:
        for i in range(len(hash_v)):  # For every h[h0..h7] hash value
            hash_v[i] = addition(hash_v[i], alphabet_values[i])  # Add it to the compressed values [a..g]
            fv.append(hash_v[i])
            hexify = hex(int(hash_v[i], 2))
            digest += hexify.strip('0x')  # Concatinate it to the final digest string

    # Function for printing
    printing(hash_v, alphabet_values, fv)
    print(' ')
    print('Final Hash: ', digest) # Final Hash Value


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    print("Please enter the text you would like to hash: ")
    message = str(input())
    # message = 'drake - the motion'

final_sha256(message)
