# SHA-256
SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that belongs to the SHA-2 (Secure Hash Algorithm 2) family. It is widely used for secure data integrity checks and digital signatures.
It takes an input message of any length and produces a fixed-size hash value of 256 bits (32 bytes). The hash value is unique to the input message, meaning even a small change in the input will result in a completely different hash value.

The SHA-256 algorithm consists of two main steps: message scheduling and message compression. Both of the steps are implemented through their corresponding functions in the *algorithm_structure.py* file.

## Message Scheduling:

The input message is divided into fixed-size blocks of 512 bits (64 bytes) and a padding function assures that inputs of any size will be represented as fixed-size blocks.
Each block is expanded into a 64-entry message schedule array.
The message schedule array introduces additional entropy into the hash algorithm at each round, ensuring the input message has a significant impact on the final hash value.

## Message Compression:

The compression function operates on a 256-bit state, divided into eight 32-bit words (A, B, C, D, E, F, G, H).
Each round of the compression function updates the state variables based on the current message schedule entry and the previous state variables.
The process continues for all message blocks, with each block updating the state variables through multiple rounds.
At the end of the compression step, the final state variables represent the computed hash value.

  **Note:** If you are interested in more theoretical information behind this cryptographic function, the official [NIST](https://drive.google.com/file/d/1DV14BTcAZMIW2E2fY8HWK9PymC0w54OF/view](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf) 
  documentation on Secure Hash Standards makes for an interesting read.

  ## Installation:
1. Clone the repository:

    git clone https://github.com/mrgeooo14/SHA-256.git

2. Navigate to the project directory.

3. Install the required dependencies:

    pip install -r requirements.txt

4. Run the program:

    python main.py

5. Provide the text you would like to hash as a command line prompt and observe the entire hashing process.

