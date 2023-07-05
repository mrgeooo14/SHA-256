from basic_operations import *
from functions import add_words, message_blocks

# ~~~~~~~~~~~~~Message Schedule ~~~~~~~~~~~~~~~~~~~~~
### The SHA-256 algorithm processes input messages in blocks of 512 bits.
### However, messages can vary in length, so before the main hash computation begins, the message needs to be preprocessed and padded to fit this block size. 
### The message scheduling step handles this process.

def message_schedule(blockedup_msg):  # Function to create the message schedule (array holding the Ws)
    for block in blockedup_msg: # For every block sized 512
        block_number = 1
        print("                Block:", block_number, "          ")
        print("         ==> Message Schedule <==           ")
        w = message_blocks(block, 32)  # Split into 32 bits words
        add_words(w)
        for i in range(0, 16):  # First 15 Ws are our message into binary bits
            print('w', i, ': ', w[i])
        for i in range(16, 64):  # W[16 to 63] are computed from the formula below
            s0 = XOR(XOR(rightRotate(w[i - 15], 7), rightRotate(w[i - 15], 18)), shift_right(w[i - 15], 3))
            s1 = XOR(XOR(rightRotate(w[i - 2], 17), rightRotate(w[i - 2], 19)), shift_right(w[i - 2], 10))

            w[i] = addition(addition(addition(w[i - 16], s0), w[i - 7]), s1)
            print('w', i, ': ', w[i])
    return w  # Return the array holding all the words which will be used in the next part of the algorithm


# ~~~~~~~~~~~~~Message Compression ~~~~~~~~~~~~~~~~~~~~~
#### Once the message scheduling is completed, the message compression step begins. 
#### In this step, the actual hash computation takes place using the expanded message schedule generated earlier.

def msg_compression(hv, w, k):  # Message Compression using Hash Values, Words from the Schedule, and Constants

    # Initialize variables a, b, c, d, e, f, g, h and set them equal to the current hash values
    a, b, c, d, e, f, g, h = [value for value in hv]

    print(' ')
    print('          ==> Message Compression <==           ')
    # The Compression Loop to mutate our hash values
    for i in range(0, 64):
        s1 = XOR(XOR(rightRotate(e, 6), rightRotate(e, 11)), rightRotate(e, 25))
        ch = XOR(AND(e, f), AND(NOT(e), g))
        temp1 = addition(h, addition(s1, addition(ch, addition(k[i], w[i]))))
        s0 = XOR(XOR(rightRotate(a, 2), rightRotate(a, 13)), rightRotate(a, 22))
        maj = XOR(XOR(AND(a, b), AND(a, c)), AND(b, c))
        temp2 = addition(s0, maj)
        h = g
        g = f
        f = e
        e = addition(d, temp1)
        d = c
        c = b
        b = a
        a = addition(temp1, temp2)

    x = [a, b, c, d, e, f, g, h]
    print(' ')
    return x  # Return the array holding the compressed hash values